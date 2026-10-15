extends CharacterBody3D
class_name FPSPlayer

## FPS Controller untuk Game Eksplorasi & Interaksi Museum (Godot 4)
## Kontrol:
## - WASD: Bergerak (Walk)
## - Shift: Berlari (Sprint)
## - Spasi: Melompat (Jump)
## - E: Berinteraksi dengan Karya Seni / Plakat
## - Mouse: Kamera First-Person
## - Esc: Toggle Kursor Mouse / Tutup Info

# ==========================================
# PENGATURAN PERGERAKAN (MOVEMENT)
# ==========================================
@export_group("Pergerakan")
@export var walk_speed: float = 4.5          ## Kecepatan jalan santai museum (m/s)
@export var sprint_speed: float = 7.5        ## Kecepatan lari dengan tombol Shift (m/s)
@export var jump_velocity: float = 4.0       ## Kekuatan lompatan
@export var acceleration: float = 8.0        ## Akselerasi pergerakan
@export var deceleration: float = 10.0       ## Deselerasi saat berhenti
@export var air_control: float = 2.5         ## Kontrol saat di udara

# ==========================================
# PENGATURAN KAMERA & MOUSE
# ==========================================
@export_group("Kamera & Mouse")
@export var mouse_sensitivity: float = 0.0022 ## Sensitivitas rotasi mouse
@export var min_pitch: float = -88.0         ## Batas pandangan bawah
@export var max_pitch: float = 88.0          ## Batas pandangan atas

# ==========================================
# EFEK KAMERA
# ==========================================
@export_group("Efek Kamera")
@export var enable_headbob: bool = true      ## Goyangan langkah kaki alami
@export var headbob_freq: float = 2.2        ## Frekuensi langkah kaki
@export var headbob_amp: float = 0.035       ## Amplitudo goyangan
@export var enable_dynamic_fov: bool = true  ## FOV dinamis saat Shift
@export var base_fov: float = 75.0           ## FOV normal
@export var sprint_fov: float = 83.0         ## FOV lari
@export var fov_change_speed: float = 6.0    ## Kecepatan transisi FOV

# ==========================================
# NODE REFERENCES
# ==========================================
@onready var head: Node3D = $Head
@onready var camera: Camera3D = $Head/Camera3D
@onready var raycast: RayCast3D = $Head/Camera3D/InteractionRayCast
@onready var reticle: Control = $HUD/ReticleContainer/DotReticle
@onready var interact_prompt: Label = $HUD/InteractPrompt
@onready var info_card: PanelContainer = $HUD/InfoCard
@onready var info_title: Label = $HUD/InfoCard/Margin/VBox/TitleLabel
@onready var info_desc: Control = $HUD/InfoCard/Margin/VBox/DescLabel

# Status internal
var is_sprinting: bool = false
var bob_timer: float = 0.0
var initial_camera_pos: Vector3 = Vector3.ZERO
var gravity: float = ProjectSettings.get_setting("physics/3d/default_gravity", 9.8)
var current_interactable: Node = null

func _ready() -> void:
	_setup_fallback_inputs()
	
	if camera:
		initial_camera_pos = camera.position
		camera.fov = base_fov

	# Sembunyikan UI interaksi di awal agar layar bersih
	if interact_prompt:
		interact_prompt.visible = false
	if info_card:
		info_card.visible = false

	# Kunci mouse untuk mode FPS
	Input.mouse_mode = Input.MOUSE_MODE_CAPTURED


func _unhandled_input(event: InputEvent) -> void:
	# Tangkap kembali mouse jika klik saat kursor lepas
	if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT:
		if Input.mouse_mode != Input.MOUSE_MODE_CAPTURED:
			Input.mouse_mode = Input.MOUSE_MODE_CAPTURED
			get_viewport().set_input_as_handled()
			return

	# Tombol Escape: tutup info karya atau lepas kursor
	if event.is_action_pressed("ui_cancel"):
		if info_card and info_card.visible:
			close_exhibit_info()
			get_viewport().set_input_as_handled()
			return
		
		if Input.mouse_mode == Input.MOUSE_MODE_CAPTURED:
			Input.mouse_mode = Input.MOUSE_MODE_VISIBLE
		else:
			Input.mouse_mode = Input.MOUSE_MODE_CAPTURED
		get_viewport().set_input_as_handled()
		return

	# Tombol Interaksi (E)
	if event.is_action_pressed("interact"):
		if info_card and info_card.visible:
			close_exhibit_info()
			get_viewport().set_input_as_handled()
			return
		elif current_interactable and current_interactable.has_method("interact"):
			current_interactable.interact(self)
			get_viewport().set_input_as_handled()
			return

	# Rotasi Kamera FPS dengan mouse
	if event is InputEventMouseMotion and Input.mouse_mode == Input.MOUSE_MODE_CAPTURED:
		rotate_y(-event.relative.x * mouse_sensitivity)
		head.rotate_x(-event.relative.y * mouse_sensitivity)
		head.rotation.x = clamp(
			head.rotation.x,
			deg_to_rad(min_pitch),
			deg_to_rad(max_pitch)
		)


func _physics_process(delta: float) -> void:
	# 1. Gravitasi
	if not is_on_floor():
		velocity.y -= gravity * delta

	# 2. Input Lompat (Spasi)
	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = jump_velocity

	# 3. Input Arah (WASD)
	var input_dir := Input.get_vector("move_left", "move_right", "move_forward", "move_backward")
	var move_direction := (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()

	# 4. Input Berlari (Shift)
	var sprint_pressed := Input.is_action_pressed("sprint")
	is_sprinting = sprint_pressed and is_on_floor() and input_dir != Vector2.ZERO

	var target_speed := sprint_speed if is_sprinting else walk_speed

	# 5. Akselerasi / Deselerasi Halus
	var current_accel := acceleration if is_on_floor() else air_control
	if move_direction != Vector3.ZERO:
		velocity.x = lerp(velocity.x, move_direction.x * target_speed, current_accel * delta)
		velocity.z = lerp(velocity.z, move_direction.z * target_speed, current_accel * delta)
	else:
		velocity.x = lerp(velocity.x, 0.0, deceleration * delta)
		velocity.z = lerp(velocity.z, 0.0, deceleration * delta)

	# 6. Jalankan pergerakan
	move_and_slide()

	# 7. Efek Visual (Headbob & FOV)
	var horizontal_speed := Vector2(velocity.x, velocity.z).length()
	_handle_headbob(delta, horizontal_speed)
	_handle_dynamic_fov(delta, move_direction)

	# 8. Deteksi Interaksi Museum (Raycast dari mata)
	_check_interaction(delta)


## Goyangan kepala saat langkah kaki
func _handle_headbob(delta: float, horizontal_speed: float) -> void:
	if not enable_headbob or not camera:
		return

	if is_on_floor() and horizontal_speed > 0.2:
		var speed_ratio: float = horizontal_speed / (sprint_speed if is_sprinting else walk_speed)
		bob_timer += delta * speed_ratio * headbob_freq * PI * 2.0
		
		var target_offset_y := sin(bob_timer) * headbob_amp
		var target_offset_x := cos(bob_timer * 0.5) * (headbob_amp * 0.5)
		
		camera.position.y = lerp(camera.position.y, initial_camera_pos.y + target_offset_y, 10.0 * delta)
		camera.position.x = lerp(camera.position.x, initial_camera_pos.x + target_offset_x, 10.0 * delta)
	else:
		bob_timer = 0.0
		camera.position.y = lerp(camera.position.y, initial_camera_pos.y, 10.0 * delta)
		camera.position.x = lerp(camera.position.x, initial_camera_pos.x, 10.0 * delta)


## Perubahan FOV dinamis saat Shift
func _handle_dynamic_fov(delta: float, move_direction: Vector3) -> void:
	if not enable_dynamic_fov or not camera:
		return

	var target_fov := sprint_fov if (is_sprinting and move_direction != Vector3.ZERO) else base_fov
	camera.fov = lerp(camera.fov, target_fov, fov_change_speed * delta)


## Memeriksa apakah kamera sedang menatap objek yang dapat diinteraksi
func _check_interaction(delta: float) -> void:
	if not raycast:
		return

	if raycast.is_colliding():
		var collider := raycast.get_collider()
		if collider and collider.has_method("interact"):
			current_interactable = collider
			if reticle and reticle.has_method("set_focus"):
				reticle.set_focus(true, delta)
			
			if interact_prompt:
				var prompt: String = collider.prompt_text if "prompt_text" in collider else "Amati"
				interact_prompt.text = "[E] " + prompt
				interact_prompt.visible = true
			return

	# Jika tidak menatap objek interaktif
	current_interactable = null
	if reticle and reticle.has_method("set_focus"):
		reticle.set_focus(false, delta)
	if interact_prompt:
		interact_prompt.visible = false


## Menampilkan kartu deskripsi karya seni museum
func display_exhibit_info(title: String, description: String) -> void:
	if info_card and info_title and info_desc:
		info_title.text = title
		info_desc.text = description
		info_card.visible = true


## Menutup kartu deskripsi karya seni
func close_exhibit_info() -> void:
	if info_card:
		info_card.visible = false


## Registrasi fallback jika InputMap belum diset
func _setup_fallback_inputs() -> void:
	_register_key("move_forward", KEY_W)
	_register_key("move_backward", KEY_S)
	_register_key("move_left", KEY_A)
	_register_key("move_right", KEY_D)
	_register_key("sprint", KEY_SHIFT)
	_register_key("jump", KEY_SPACE)
	_register_key("interact", KEY_E)
	_register_key("ui_cancel", KEY_ESCAPE)


func _register_key(action: String, physical_key: Key) -> void:
	if not InputMap.has_action(action):
		InputMap.add_action(action)
	for event in InputMap.action_get_events(action):
		if event is InputEventKey and event.physical_keycode == physical_key:
			return
	var event := InputEventKey.new()
	event.physical_keycode = physical_key
	InputMap.action_add_event(action, event)
