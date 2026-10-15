extends Area3D

## Menghubungkan interaksi Raycast kamera ke controller pintu induk
var prompt_text: String:
	get:
		var p := get_parent()
		return p.prompt_text if ("prompt_text" in p) else "Buka Pintu"

func interact(player: Node = null) -> void:
	var p := get_parent()
	if p and p.has_method("interact"):
		p.interact(player)
