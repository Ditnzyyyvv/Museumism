extends StaticBody3D
class_name MuseumDoor

## Pintu Geser Museum Otomatis dengan Animasi Halus (Godot 4)
## Interaksi: Tombol E membuka/menutup pintu

@export var prompt_text: String = "Buka Pintu"
@export var slide_distance: float = 1.75          ## Jarak geser daun pintu ke samping (meter)
@export var open_duration: float = 0.85          ## Durasi animasi buka/tutup (detik)
@export var auto_close: bool = true              ## Otomatis menutup setelah pemain masuk
@export var auto_close_delay: float = 5.0        ## Waktu tunggu sebelum pintu otomatis menutup (detik)

@onready var left_leaf: Node3D = $LeftLeaf
@onready var right_leaf: Node3D = $RightLeaf
@onready var blocker_collision: CollisionShape3D = $BlockerCollision

var is_open: bool = false
var is_animating: bool = false
var left_closed_z: float = -0.9
var right_closed_z: float = 0.9
var timer: float = 0.0

func _ready() -> void:
	if left_leaf:
		left_closed_z = left_leaf.position.z
	if right_leaf:
		right_closed_z = right_leaf.position.z
	prompt_text = "Buka Pintu"


func _process(delta: float) -> void:
	if auto_close and is_open and not is_animating:
		timer += delta
		if timer >= auto_close_delay:
			close_door()


## Dipanggil oleh Player Controller saat tombol [E] ditekan
func interact(_player: Node = null) -> void:
	if is_animating:
		return
	if is_open:
		close_door()
	else:
		open_door()


## Membuka kedua daun pintu ke samping dengan animasi Tween
func open_door() -> void:
	if is_open or is_animating:
		return
	is_animating = true
	is_open = true
	timer = 0.0
	prompt_text = "Tutup Pintu"

	# Buka jalan bagi pemain (nonaktifkan collision fisik penutup)
	if blocker_collision:
		blocker_collision.set_deferred("disabled", true)

	var tween := create_tween().set_parallel(true).set_trans(Tween.TRANS_CUBIC).set_ease(Tween.EASE_OUT)
	if left_leaf:
		tween.tween_property(left_leaf, "position:z", left_closed_z - slide_distance, open_duration)
	if right_leaf:
		tween.tween_property(right_leaf, "position:z", right_closed_z + slide_distance, open_duration)

	tween.chain().tween_callback(func():
		is_animating = false
	)


## Menutup kembali kedua daun pintu dengan animasi Tween
func close_door() -> void:
	if not is_open or is_animating:
		return
	is_animating = true
	is_open = false
	prompt_text = "Buka Pintu"

	var tween := create_tween().set_parallel(true).set_trans(Tween.TRANS_CUBIC).set_ease(Tween.EASE_IN_OUT)
	if left_leaf:
		tween.tween_property(left_leaf, "position:z", left_closed_z, open_duration)
	if right_leaf:
		tween.tween_property(right_leaf, "position:z", right_closed_z, open_duration)

	tween.chain().tween_callback(func():
		is_animating = false
		if blocker_collision:
			blocker_collision.set_deferred("disabled", false)
	)
