extends Control

## Crosshair berbentuk Dot kecil minimalis untuk game eksplorasi & interaksi
@export var dot_radius: float = 2.5
@export var focused_radius: float = 4.0
@export var default_color: Color = Color(1.0, 1.0, 1.0, 0.65)
@export var focused_color: Color = Color(1.0, 1.0, 1.0, 0.95)

var current_radius: float = 2.5
var current_color: Color = Color(1.0, 1.0, 1.0, 0.65)
var is_focused: bool = false

func _draw() -> void:
	# Gambar lingkaran kecil lembut di titik tengah
	draw_circle(Vector2.ZERO, current_radius, current_color)

func set_focus(focused: bool, delta: float = 0.0) -> void:
	is_focused = focused
	var target_radius := focused_radius if focused else dot_radius
	var target_color := focused_color if focused else default_color
	
	if delta > 0.0:
		current_radius = lerp(current_radius, target_radius, 15.0 * delta)
		current_color = current_color.lerp(target_color, 15.0 * delta)
	else:
		current_radius = target_radius
		current_color = target_color
	
	queue_redraw()
