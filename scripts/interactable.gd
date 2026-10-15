extends StaticBody3D
class_name Interactable

## Komponen untuk objek yang dapat diinteraksi di dalam museum (Lukisan, Patung, Plakat, dll.)
@export var prompt_text: String = "Amati"
@export var exhibit_title: String = "Nama Karya Seni"
@export_multiline var exhibit_description: String = "Deskripsi penjelasan tentang karya seni ini..."

func interact(player: Node) -> void:
	if player.has_method("display_exhibit_info"):
		player.display_exhibit_info(exhibit_title, exhibit_description)
