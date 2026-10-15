"""
Museumism Scene Builder Script
Generates a complete, beautiful 3D museum level in Godot 4 format:
- Central Grand Hallway with custom lighting and red carpet runner
- 4 Dedicated Memorial Thematic Rooms (WALL-E, A Silent Voice, Kimi ni Todoke, Josee)
- Thematic Portal Outer Walls outside each room door with custom textures and glowing archways
- Movie posters with spot lights and frames
- Gallery character photos with spot lights and frames
- 3D Centerpiece Tributes (WALL-E robot with plant, Shoko's zen koi notebook, Sawako's classroom desk, Josee's wheelchair & easel)
- Detailed narrative plaques with personal reflections
- End-of-hallway Sanctuary of Stories
"""

import os

def generate_main_scene():
    out = []
    
    # Header
    out.append('[gd_scene load_steps=75 format=3]')
    out.append('')
    
    # ExtResources
    out.append('[ext_resource type="PackedScene" path="res://scenes/player.tscn" id="1_player"]')
    out.append('[ext_resource type="Script" path="res://scripts/interactable.gd" id="2_interactable"]')
    
    # Textures
    out.append('[ext_resource type="Texture2D" path="res://assets/themes/portal_walle.png" id="tex_portal_walle"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/themes/portal_silent_voice.png" id="tex_portal_silent_voice"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/themes/portal_kimi_ni_todoke.png" id="tex_portal_kimi_ni_todoke"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/themes/portal_josee.png" id="tex_portal_josee"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/themes/lobby_banner.png" id="tex_lobby_banner"]')
    
    out.append('[ext_resource type="Texture2D" path="res://assets/posters/poster_walle.png" id="tex_poster_walle"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/posters/poster_silent_voice.png" id="tex_poster_silent_voice"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/posters/poster_kimi_ni_todoke.png" id="tex_poster_kimi_ni_todoke"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/posters/poster_josee.png" id="tex_poster_josee"]')
    
    out.append('[ext_resource type="Texture2D" path="res://assets/photos/photo_walle_1.png" id="tex_photo_walle_1"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/photos/photo_walle_2.png" id="tex_photo_walle_2"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/photos/photo_silent_voice_1.png" id="tex_photo_silent_voice_1"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/photos/photo_silent_voice_2.png" id="tex_photo_silent_voice_2"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/photos/photo_kimi_ni_todoke_1.png" id="tex_photo_kimi_ni_todoke_1"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/photos/photo_kimi_ni_todoke_2.png" id="tex_photo_kimi_ni_todoke_2"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/photos/photo_josee_1.png" id="tex_photo_josee_1"]')
    out.append('[ext_resource type="Texture2D" path="res://assets/photos/photo_josee_2.png" id="tex_photo_josee_2"]')
    out.append('')
    
    # Environment
    out.append('[sub_resource type="Environment" id="Environment_museum"]')
    out.append('background_mode = 1')
    out.append('background_color = Color(0.04, 0.04, 0.06, 1)')
    out.append('ambient_light_source = 2')
    out.append('ambient_light_color = Color(0.4, 0.42, 0.46, 1)')
    out.append('ambient_light_energy = 0.9')
    out.append('tonemap_mode = 2')
    out.append('glow_enabled = true')
    out.append('glow_intensity = 0.6')
    out.append('glow_bloom = 0.25')
    out.append('')
    
    # Shared Architectural Materials
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_HallFloor"]')
    out.append('albedo_color = Color(0.1, 0.1, 0.13, 1)')
    out.append('roughness = 0.18')
    out.append('metallic = 0.15')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_RunnerCarpet"]')
    out.append('albedo_color = Color(0.52, 0.07, 0.12, 1)')
    out.append('roughness = 0.85')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_HallCeiling"]')
    out.append('albedo_color = Color(0.12, 0.12, 0.14, 1)')
    out.append('roughness = 0.9')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_HallWall"]')
    out.append('albedo_color = Color(0.92, 0.91, 0.88, 1)')
    out.append('roughness = 0.85')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Beam"]')
    out.append('albedo_color = Color(0.08, 0.08, 0.1, 1)')
    out.append('metallic = 0.5')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_GoldTrim"]')
    out.append('albedo_color = Color(0.9, 0.76, 0.32, 1)')
    out.append('metallic = 0.9')
    out.append('roughness = 0.2')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_BlackFrame"]')
    out.append('albedo_color = Color(0.06, 0.06, 0.08, 1)')
    out.append('metallic = 0.7')
    out.append('roughness = 0.25')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Pedestal"]')
    out.append('albedo_color = Color(0.95, 0.95, 0.97, 1)')
    out.append('roughness = 0.18')
    out.append('metallic = 0.05')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_WoodBench"]')
    out.append('albedo_color = Color(0.24, 0.15, 0.1, 1)')
    out.append('roughness = 0.35')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Lectern"]')
    out.append('albedo_color = Color(0.16, 0.13, 0.11, 1)')
    out.append('metallic = 0.4')
    out.append('roughness = 0.3')
    out.append('')
    
    # Thematic Portal Materials (HALLWAY WALLS)
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Portal_Walle"]')
    out.append('albedo_texture = ExtResource("tex_portal_walle")')
    out.append('roughness = 0.3')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Portal_SilentVoice"]')
    out.append('albedo_texture = ExtResource("tex_portal_silent_voice")')
    out.append('roughness = 0.3')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Portal_KimiNiTodoke"]')
    out.append('albedo_texture = ExtResource("tex_portal_kimi_ni_todoke")')
    out.append('roughness = 0.3')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Portal_Josee"]')
    out.append('albedo_texture = ExtResource("tex_portal_josee")')
    out.append('roughness = 0.3')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_LobbyBanner"]')
    out.append('albedo_texture = ExtResource("tex_lobby_banner")')
    out.append('roughness = 0.3')
    out.append('')
    
    # Archway Trims
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Arch_Walle"]')
    out.append('albedo_color = Color(0.0, 0.85, 1.0, 1)')
    out.append('emission_enabled = true')
    out.append('emission = Color(0.0, 0.85, 1.0, 1)')
    out.append('emission_energy_multiplier = 2.0')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Arch_SilentVoice"]')
    out.append('albedo_color = Color(0.95, 0.72, 0.8, 1)')
    out.append('roughness = 0.35')
    out.append('emission_enabled = true')
    out.append('emission = Color(0.95, 0.72, 0.8, 1)')
    out.append('emission_energy_multiplier = 0.5')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Arch_KimiNiTodoke"]')
    out.append('albedo_color = Color(1.0, 0.82, 0.35, 1)')
    out.append('metallic = 0.85')
    out.append('roughness = 0.2')
    out.append('emission_enabled = true')
    out.append('emission = Color(1.0, 0.82, 0.35, 1)')
    out.append('emission_energy_multiplier = 0.6')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Arch_Josee"]')
    out.append('albedo_color = Color(0.0, 0.75, 0.95, 1)')
    out.append('metallic = 0.8')
    out.append('roughness = 0.2')
    out.append('emission_enabled = true')
    out.append('emission = Color(0.0, 0.65, 0.9, 1)')
    out.append('emission_energy_multiplier = 1.2')
    out.append('')
    
    # Room Flooring Materials
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_RoomFloor_Walle"]')
    out.append('albedo_color = Color(0.07, 0.08, 0.12, 1)')
    out.append('metallic = 0.6')
    out.append('roughness = 0.3')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_RoomFloor_SilentVoice"]')
    out.append('albedo_color = Color(0.85, 0.78, 0.7, 1)')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_RoomFloor_KimiNiTodoke"]')
    out.append('albedo_color = Color(0.66, 0.48, 0.34, 1)')
    out.append('roughness = 0.32')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_RoomFloor_Josee"]')
    out.append('albedo_color = Color(0.04, 0.12, 0.22, 1)')
    out.append('roughness = 0.12')
    out.append('metallic = 0.3')
    out.append('')
    
    # Poster Materials
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Poster_Walle"]')
    out.append('albedo_texture = ExtResource("tex_poster_walle")')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Poster_SilentVoice"]')
    out.append('albedo_texture = ExtResource("tex_poster_silent_voice")')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Poster_KimiNiTodoke"]')
    out.append('albedo_texture = ExtResource("tex_poster_kimi_ni_todoke")')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Poster_Josee"]')
    out.append('albedo_texture = ExtResource("tex_poster_josee")')
    out.append('roughness = 0.4')
    out.append('')
    
    # Photo Materials
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Photo_Walle_1"]')
    out.append('albedo_texture = ExtResource("tex_photo_walle_1")')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Photo_Walle_2"]')
    out.append('albedo_texture = ExtResource("tex_photo_walle_2")')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Photo_SilentVoice_1"]')
    out.append('albedo_texture = ExtResource("tex_photo_silent_voice_1")')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Photo_SilentVoice_2"]')
    out.append('albedo_texture = ExtResource("tex_photo_silent_voice_2")')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Photo_KimiNiTodoke_1"]')
    out.append('albedo_texture = ExtResource("tex_photo_kimi_ni_todoke_1")')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Photo_KimiNiTodoke_2"]')
    out.append('albedo_texture = ExtResource("tex_photo_kimi_ni_todoke_2")')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Photo_Josee_1"]')
    out.append('albedo_texture = ExtResource("tex_photo_josee_1")')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_Photo_Josee_2"]')
    out.append('albedo_texture = ExtResource("tex_photo_josee_2")')
    out.append('roughness = 0.4')
    out.append('')
    
    # Tribute Special Materials
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_WalleYellow"]')
    out.append('albedo_color = Color(0.88, 0.68, 0.18, 1)')
    out.append('roughness = 0.4')
    out.append('metallic = 0.3')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_WalleEyes"]')
    out.append('albedo_color = Color(0.3, 0.85, 1.0, 1)')
    out.append('emission_enabled = true')
    out.append('emission = Color(0.3, 0.85, 1.0, 1)')
    out.append('emission_energy_multiplier = 2.5')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_PlantGreen"]')
    out.append('albedo_color = Color(0.2, 0.88, 0.25, 1)')
    out.append('emission_enabled = true')
    out.append('emission = Color(0.2, 0.88, 0.25, 1)')
    out.append('emission_energy_multiplier = 1.2')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_ZenWater"]')
    out.append('albedo_color = Color(0.18, 0.72, 0.82, 0.85)')
    out.append('roughness = 0.05')
    out.append('emission_enabled = true')
    out.append('emission = Color(0.15, 0.6, 0.7, 1)')
    out.append('emission_energy_multiplier = 0.6')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_SakuraPetals"]')
    out.append('albedo_color = Color(1.0, 0.72, 0.8, 1)')
    out.append('roughness = 0.5')
    out.append('emission_enabled = true')
    out.append('emission = Color(1.0, 0.75, 0.82, 1)')
    out.append('emission_energy_multiplier = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_JoseeRed"]')
    out.append('albedo_color = Color(0.68, 0.15, 0.18, 1)')
    out.append('roughness = 0.4')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_ChromeMetal"]')
    out.append('albedo_color = Color(0.9, 0.92, 0.95, 1)')
    out.append('metallic = 1.0')
    out.append('roughness = 0.1')
    out.append('')
    
    out.append('[sub_resource type="StandardMaterial3D" id="Mat_OceanBlue"]')
    out.append('albedo_color = Color(0.08, 0.48, 0.78, 1)')
    out.append('emission_enabled = true')
    out.append('emission = Color(0.08, 0.45, 0.75, 1)')
    out.append('emission_energy_multiplier = 0.8')
    out.append('')
    
    # Generic Meshes
    out.append('[sub_resource type="BoxMesh" id="Mesh_LecternStand"]')
    out.append('material = SubResource("Mat_Lectern")')
    out.append('size = Vector3(0.7, 1.0, 0.4)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_LecternTop"]')
    out.append('material = SubResource("Mat_GoldTrim")')
    out.append('size = Vector3(0.8, 0.1, 0.5)')
    out.append('')
    
    out.append('[sub_resource type="BoxShape3D" id="Shape_Lectern"]')
    out.append('size = Vector3(1.0, 1.4, 0.8)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_PosterFrame"]')
    out.append('material = SubResource("Mat_BlackFrame")')
    out.append('size = Vector3(2.6, 3.6, 0.08)')
    out.append('')
    
    out.append('[sub_resource type="BoxShape3D" id="Shape_Poster"]')
    out.append('size = Vector3(2.6, 3.6, 0.6)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_PhotoFrame"]')
    out.append('material = SubResource("Mat_BlackFrame")')
    out.append('size = Vector3(2.6, 1.8, 0.08)')
    out.append('')
    
    out.append('[sub_resource type="BoxShape3D" id="Shape_Photo"]')
    out.append('size = Vector3(2.6, 1.8, 0.6)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_WoodBench"]')
    out.append('material = SubResource("Mat_WoodBench")')
    out.append('size = Vector3(2.4, 0.45, 0.9)')
    out.append('')
    
    out.append('[sub_resource type="BoxShape3D" id="Shape_Bench"]')
    out.append('size = Vector3(2.4, 0.45, 0.9)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_RoomCeiling"]')
    out.append('material = SubResource("Mat_HallCeiling")')
    out.append('size = Vector3(14.0, 0.4, 14.0)')
    out.append('')
    
    out.append('[sub_resource type="BoxShape3D" id="Shape_RoomFloor"]')
    out.append('size = Vector3(14.0, 0.5, 14.0)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_RoomFloor_Walle"]')
    out.append('material = SubResource("Mat_RoomFloor_Walle")')
    out.append('size = Vector3(14.0, 0.5, 14.0)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_RoomFloor_SilentVoice"]')
    out.append('material = SubResource("Mat_RoomFloor_SilentVoice")')
    out.append('size = Vector3(14.0, 0.5, 14.0)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_RoomFloor_KimiNiTodoke"]')
    out.append('material = SubResource("Mat_RoomFloor_KimiNiTodoke")')
    out.append('size = Vector3(14.0, 0.5, 14.0)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_RoomFloor_Josee"]')
    out.append('material = SubResource("Mat_RoomFloor_Josee")')
    out.append('size = Vector3(14.0, 0.5, 14.0)')
    out.append('')
    
    # Wall meshes
    out.append('[sub_resource type="BoxMesh" id="Mesh_RoomWallNS"]')
    out.append('material = SubResource("Mat_HallWall")')
    out.append('size = Vector3(14.0, 5.2, 0.4)')
    out.append('')
    
    out.append('[sub_resource type="BoxShape3D" id="Shape_RoomWallNS"]')
    out.append('size = Vector3(14.0, 5.2, 0.4)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_RoomWallEW"]')
    out.append('material = SubResource("Mat_HallWall")')
    out.append('size = Vector3(0.4, 5.2, 14.0)')
    out.append('')
    
    out.append('[sub_resource type="BoxShape3D" id="Shape_RoomWallEW"]')
    out.append('size = Vector3(0.4, 5.2, 14.0)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_RoomDoorWall"]')
    out.append('material = SubResource("Mat_HallWall")')
    out.append('size = Vector3(0.4, 5.2, 5.2)')
    out.append('')
    
    out.append('[sub_resource type="BoxShape3D" id="Shape_RoomDoorWall"]')
    out.append('size = Vector3(0.4, 5.2, 5.2)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_DoorLintel"]')
    out.append('material = SubResource("Mat_HallWall")')
    out.append('size = Vector3(0.4, 2.0, 3.6)')
    out.append('')
    
    out.append('[sub_resource type="BoxShape3D" id="Shape_DoorLintel"]')
    out.append('size = Vector3(0.4, 2.0, 3.6)')
    out.append('')

    # Specific Poster Meshes
    out.append('[sub_resource type="BoxMesh" id="Mesh_Canvas_Poster_Walle"]')
    out.append('material = SubResource("Mat_Poster_Walle")')
    out.append('size = Vector3(2.4, 3.4, 0.09)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_Canvas_Poster_SilentVoice"]')
    out.append('material = SubResource("Mat_Poster_SilentVoice")')
    out.append('size = Vector3(2.4, 3.4, 0.09)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_Canvas_Poster_KimiNiTodoke"]')
    out.append('material = SubResource("Mat_Poster_KimiNiTodoke")')
    out.append('size = Vector3(2.4, 3.4, 0.09)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_Canvas_Poster_Josee"]')
    out.append('material = SubResource("Mat_Poster_Josee")')
    out.append('size = Vector3(2.4, 3.4, 0.09)')
    out.append('')
    
    # Specific Photo Meshes
    out.append('[sub_resource type="BoxMesh" id="Mesh_Canvas_Photo_Walle_1"]')
    out.append('material = SubResource("Mat_Photo_Walle_1")')
    out.append('size = Vector3(2.4, 1.6, 0.09)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_Canvas_Photo_Walle_2"]')
    out.append('material = SubResource("Mat_Photo_Walle_2")')
    out.append('size = Vector3(2.4, 1.6, 0.09)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_Canvas_Photo_SilentVoice_1"]')
    out.append('material = SubResource("Mat_Photo_SilentVoice_1")')
    out.append('size = Vector3(2.4, 1.6, 0.09)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_Canvas_Photo_SilentVoice_2"]')
    out.append('material = SubResource("Mat_Photo_SilentVoice_2")')
    out.append('size = Vector3(2.4, 1.6, 0.09)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_Canvas_Photo_KimiNiTodoke_1"]')
    out.append('material = SubResource("Mat_Photo_KimiNiTodoke_1")')
    out.append('size = Vector3(2.4, 1.6, 0.09)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_Canvas_Photo_KimiNiTodoke_2"]')
    out.append('material = SubResource("Mat_Photo_KimiNiTodoke_2")')
    out.append('size = Vector3(2.4, 1.6, 0.09)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_Canvas_Photo_Josee_1"]')
    out.append('material = SubResource("Mat_Photo_Josee_1")')
    out.append('size = Vector3(2.4, 1.6, 0.09)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_Canvas_Photo_Josee_2"]')
    out.append('material = SubResource("Mat_Photo_Josee_2")')
    out.append('size = Vector3(2.4, 1.6, 0.09)')
    out.append('')
    
    # Thematic Hallway Portal Panel Meshes
    out.append('[sub_resource type="BoxMesh" id="Mesh_PortalPanel_Walle"]')
    out.append('material = SubResource("Mat_Portal_Walle")')
    out.append('size = Vector3(0.08, 5.0, 7.0)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_PortalPanel_SilentVoice"]')
    out.append('material = SubResource("Mat_Portal_SilentVoice")')
    out.append('size = Vector3(0.08, 5.0, 7.0)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_PortalPanel_KimiNiTodoke"]')
    out.append('material = SubResource("Mat_Portal_KimiNiTodoke")')
    out.append('size = Vector3(0.08, 5.0, 7.0)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_PortalPanel_Josee"]')
    out.append('material = SubResource("Mat_Portal_Josee")')
    out.append('size = Vector3(0.08, 5.0, 7.0)')
    out.append('')
    
    out.append('[sub_resource type="BoxMesh" id="Mesh_LobbyBanner"]')
    out.append('material = SubResource("Mat_LobbyBanner")')
    out.append('size = Vector3(6.4, 3.2, 0.08)')
    out.append('')
    
    # ----------------------------------------------------
    # SCENE NODE HIERARCHY
    # ----------------------------------------------------
    out.append('[node name="Main" type="Node3D"]')
    out.append('')
    
    out.append('[node name="WorldEnvironment" type="WorldEnvironment" parent="."] ')
    out.append('environment = SubResource("Environment_museum")')
    out.append('')
    
    out.append('[node name="GrandHallway" type="Node3D" parent="."] ')
    out.append('')
    
    # Main Floor
    out.append('[node name="HallFloor" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, -0.25, -21)')
    out.append('')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/HallFloor"]')
    out.append('[sub_resource type="BoxMesh" id="Mesh_HallFloor"]')
    out.append('material = SubResource("Mat_HallFloor")')
    out.append('size = Vector3(7.0, 0.5, 66.0)')
    out.append('mesh = SubResource("Mesh_HallFloor")')
    out.append('')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/HallFloor"]')
    out.append('[sub_resource type="BoxShape3D" id="Shape_HallFloor"]')
    out.append('size = Vector3(7.0, 0.5, 66.0)')
    out.append('shape = SubResource("Shape_HallFloor")')
    out.append('')
    
    # Runner Carpet
    out.append('[node name="CarpetRunner" type="MeshInstance3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.015, -21)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Carpet"]')
    out.append('material = SubResource("Mat_RunnerCarpet")')
    out.append('size = Vector3(2.4, 0.02, 64.0)')
    out.append('mesh = SubResource("Mesh_Carpet")')
    out.append('')
    
    # Ceiling
    out.append('[node name="HallCeiling" type="MeshInstance3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 5.25, -21)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_HallCeiling"]')
    out.append('material = SubResource("Mat_HallCeiling")')
    out.append('size = Vector3(7.0, 0.5, 66.0)')
    out.append('mesh = SubResource("Mesh_HallCeiling")')
    out.append('')
    
    # South Wall (Entrance with Lobby Banner)
    out.append('[node name="SouthWall" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2.5, 12)')
    out.append('')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/SouthWall"]')
    out.append('[sub_resource type="BoxMesh" id="Mesh_HallEndWall"]')
    out.append('material = SubResource("Mat_HallWall")')
    out.append('size = Vector3(7.0, 5.2, 0.5)')
    out.append('mesh = SubResource("Mesh_HallEndWall")')
    out.append('')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/SouthWall"]')
    out.append('[sub_resource type="BoxShape3D" id="Shape_HallEndWall"]')
    out.append('size = Vector3(7.0, 5.2, 0.5)')
    out.append('shape = SubResource("Shape_HallEndWall")')
    out.append('')
    
    out.append('[node name="LobbyBannerMesh" type="MeshInstance3D" parent="GrandHallway/SouthWall"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.2, -0.28)')
    out.append('mesh = SubResource("Mesh_LobbyBanner")')
    out.append('')
    
    # North Wall (Sanctuary End Wall)
    out.append('[node name="NorthWall" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2.5, -54)')
    out.append('')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/NorthWall"]')
    out.append('mesh = SubResource("Mesh_HallEndWall")')
    out.append('')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/NorthWall"]')
    out.append('shape = SubResource("Shape_HallEndWall")')
    out.append('')

    # West Wall Segments (with doors at Z=0, Z=-28)
    # W1: Z = 12 to 1.8 (center 6.9, length 10.2)
    out.append('[node name="WestWall_Seg1" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -3.5, 2.5, 6.9)')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/WestWall_Seg1"]')
    out.append('[sub_resource type="BoxMesh" id="Mesh_WestWall_Seg1"]')
    out.append('material = SubResource("Mat_HallWall")')
    out.append('size = Vector3(0.5, 5.2, 10.2)')
    out.append('mesh = SubResource("Mesh_WestWall_Seg1")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/WestWall_Seg1"]')
    out.append('[sub_resource type="BoxShape3D" id="Shape_WestWall_Seg1"]')
    out.append('size = Vector3(0.5, 5.2, 10.2)')
    out.append('shape = SubResource("Shape_WestWall_Seg1")')
    out.append('')
    
    # Lintel over Door 1 (Z=0, length 3.6, height 2.0 at Y=4.25)
    out.append('[node name="WestDoor1_Lintel" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -3.5, 4.25, 0)')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/WestDoor1_Lintel"]')
    out.append('mesh = SubResource("Mesh_DoorLintel")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/WestDoor1_Lintel"]')
    out.append('shape = SubResource("Shape_DoorLintel")')
    out.append('')
    
    # W2: Z = -1.8 to -26.2 (center -14.0, length 24.4)
    out.append('[node name="WestWall_Seg2" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -3.5, 2.5, -14.0)')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/WestWall_Seg2"]')
    out.append('[sub_resource type="BoxMesh" id="Mesh_WestWall_Seg2"]')
    out.append('material = SubResource("Mat_HallWall")')
    out.append('size = Vector3(0.5, 5.2, 24.4)')
    out.append('mesh = SubResource("Mesh_WestWall_Seg2")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/WestWall_Seg2"]')
    out.append('[sub_resource type="BoxShape3D" id="Shape_WestWall_Seg2"]')
    out.append('size = Vector3(0.5, 5.2, 24.4)')
    out.append('shape = SubResource("Shape_WestWall_Seg2")')
    out.append('')
    
    # Lintel over Door 3 (Z=-28, length 3.6, height 2.0 at Y=4.25)
    out.append('[node name="WestDoor3_Lintel" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -3.5, 4.25, -28)')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/WestDoor3_Lintel"]')
    out.append('mesh = SubResource("Mesh_DoorLintel")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/WestDoor3_Lintel"]')
    out.append('shape = SubResource("Shape_DoorLintel")')
    out.append('')
    
    # W3: Z = -29.8 to -54 (center -41.9, length 24.2)
    out.append('[node name="WestWall_Seg3" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -3.5, 2.5, -41.9)')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/WestWall_Seg3"]')
    out.append('[sub_resource type="BoxMesh" id="Mesh_WestWall_Seg3"]')
    out.append('material = SubResource("Mat_HallWall")')
    out.append('size = Vector3(0.5, 5.2, 24.2)')
    out.append('mesh = SubResource("Mesh_WestWall_Seg3")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/WestWall_Seg3"]')
    out.append('[sub_resource type="BoxShape3D" id="Shape_WestWall_Seg3"]')
    out.append('size = Vector3(0.5, 5.2, 24.2)')
    out.append('shape = SubResource("Shape_WestWall_Seg3")')
    out.append('')
    
    # East Wall Segments (with doors at Z=-14, Z=-42)
    # E1: Z = 12 to -12.2 (center -0.1, length 24.2)
    out.append('[node name="EastWall_Seg1" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 3.5, 2.5, -0.1)')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/EastWall_Seg1"]')
    out.append('[sub_resource type="BoxMesh" id="Mesh_EastWall_Seg1"]')
    out.append('material = SubResource("Mat_HallWall")')
    out.append('size = Vector3(0.5, 5.2, 24.2)')
    out.append('mesh = SubResource("Mesh_EastWall_Seg1")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/EastWall_Seg1"]')
    out.append('[sub_resource type="BoxShape3D" id="Shape_EastWall_Seg1"]')
    out.append('size = Vector3(0.5, 5.2, 24.2)')
    out.append('shape = SubResource("Shape_EastWall_Seg1")')
    out.append('')
    
    # Lintel over Door 2 (Z=-14, length 3.6, height 2.0 at Y=4.25)
    out.append('[node name="EastDoor2_Lintel" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 3.5, 4.25, -14)')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/EastDoor2_Lintel"]')
    out.append('mesh = SubResource("Mesh_DoorLintel")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/EastDoor2_Lintel"]')
    out.append('shape = SubResource("Shape_DoorLintel")')
    out.append('')
    
    # E2: Z = -15.8 to -40.2 (center -28.0, length 24.4)
    out.append('[node name="EastWall_Seg2" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 3.5, 2.5, -28.0)')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/EastWall_Seg2"]')
    out.append('[sub_resource type="BoxMesh" id="Mesh_EastWall_Seg2"]')
    out.append('material = SubResource("Mat_HallWall")')
    out.append('size = Vector3(0.5, 5.2, 24.4)')
    out.append('mesh = SubResource("Mesh_EastWall_Seg2")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/EastWall_Seg2"]')
    out.append('[sub_resource type="BoxShape3D" id="Shape_EastWall_Seg2"]')
    out.append('size = Vector3(0.5, 5.2, 24.4)')
    out.append('shape = SubResource("Shape_EastWall_Seg2")')
    out.append('')
    
    # Lintel over Door 4 (Z=-42, length 3.6, height 2.0 at Y=4.25)
    out.append('[node name="EastDoor4_Lintel" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 3.5, 4.25, -42)')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/EastDoor4_Lintel"]')
    out.append('mesh = SubResource("Mesh_DoorLintel")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/EastDoor4_Lintel"]')
    out.append('shape = SubResource("Shape_DoorLintel")')
    out.append('')
    
    # E3: Z = -43.8 to -54 (center -48.9, length 10.2)
    out.append('[node name="EastWall_Seg3" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 3.5, 2.5, -48.9)')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/EastWall_Seg3"]')
    out.append('[sub_resource type="BoxMesh" id="Mesh_EastWall_Seg3"]')
    out.append('material = SubResource("Mat_HallWall")')
    out.append('size = Vector3(0.5, 5.2, 10.2)')
    out.append('mesh = SubResource("Mesh_EastWall_Seg3")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/EastWall_Seg3"]')
    out.append('[sub_resource type="BoxShape3D" id="Shape_EastWall_Seg3"]')
    out.append('size = Vector3(0.5, 5.2, 10.2)')
    out.append('shape = SubResource("Shape_EastWall_Seg3")')
    out.append('')
    
    # ----------------------------------------------------
    # THEMATIC PORTAL WALLS (IN MAIN HALLWAY)
    # ----------------------------------------------------
    # Portal 1 (Wall-E) at West wall X = -3.22, Z = 0
    out.append('[node name="PortalOuter_WallE" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -3.22, 2.5, 0)')
    out.append('script = ExtResource("2_interactable")')
    out.append('prompt_text = "Lihat Info Section 01"')
    out.append('exhibit_title = "Section 01: WALL-E (2008) — Deep Space"')
    out.append('exhibit_description = "Gerbang menuju sayap penghormatan WALL-E. Tembok dihiasi tema kosmik luar angkasa dengan nebula dan taburan bintang abadi, melambangkan perjalanan cinta tulus WALL-E dan EVE yang menyeberangi galaksi."')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/PortalOuter_WallE"]')
    out.append('mesh = SubResource("Mesh_PortalPanel_Walle")')
    out.append('[node name="ArchFrame" type="MeshInstance3D" parent="GrandHallway/PortalOuter_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0.05, 0, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Arch_Walle"]')
    out.append('material = SubResource("Mat_Arch_Walle")')
    out.append('size = Vector3(0.06, 3.3, 3.8)')
    out.append('mesh = SubResource("Mesh_Arch_Walle")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/PortalOuter_WallE"]')
    out.append('[sub_resource type="BoxShape3D" id="Shape_PortalPanel"]')
    out.append('size = Vector3(0.5, 5.0, 7.0)')
    out.append('shape = SubResource("Shape_PortalPanel")')
    out.append('')
    
    # Portal 2 (A Silent Voice) at East wall X = 3.22, Z = -14
    out.append('[node name="PortalOuter_SilentVoice" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 3.22, 2.5, -14)')
    out.append('script = ExtResource("2_interactable")')
    out.append('prompt_text = "Lihat Info Section 02"')
    out.append('exhibit_title = "Section 02: A Silent Voice (2016) — Sakura & River"')
    out.append('exhibit_description = "Gerbang menuju sayap penghormatan A Silent Voice (聲の形). Didekorasi dengan kelopak bunga sakura, riak air jernih Sungai Suimon, dan simbol siluet X yang terlepas saat seseorang menemukan keberanian untuk mendengar suara hati orang lain."')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/PortalOuter_SilentVoice"]')
    out.append('mesh = SubResource("Mesh_PortalPanel_SilentVoice")')
    out.append('[node name="ArchFrame" type="MeshInstance3D" parent="GrandHallway/PortalOuter_SilentVoice"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -0.05, 0, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Arch_SilentVoice"]')
    out.append('material = SubResource("Mat_Arch_SilentVoice")')
    out.append('size = Vector3(0.06, 3.3, 3.8)')
    out.append('mesh = SubResource("Mesh_Arch_SilentVoice")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/PortalOuter_SilentVoice"]')
    out.append('shape = SubResource("Shape_PortalPanel")')
    out.append('')
    
    # Portal 3 (Kimi ni Todoke) at West wall X = -3.22, Z = -28
    out.append('[node name="PortalOuter_KimiNiTodoke" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -3.22, 2.5, -28)')
    out.append('script = ExtResource("2_interactable")')
    out.append('prompt_text = "Lihat Info Section 03"')
    out.append('exhibit_title = "Section 03: Kimi ni Todoke — Springtime Youth"')
    out.append('exhibit_description = "Gerbang menuju sayap penghormatan Kimi ni Todoke (君に届け). Didekorasi dengan kehangatan musim semi sekolah, bunga sakura yang bersemi, dan semilir angin lembut yang mengantarkan ketulusan perasaan Sawako dan Kazehaya."')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/PortalOuter_KimiNiTodoke"]')
    out.append('mesh = SubResource("Mesh_PortalPanel_KimiNiTodoke")')
    out.append('[node name="ArchFrame" type="MeshInstance3D" parent="GrandHallway/PortalOuter_KimiNiTodoke"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0.05, 0, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Arch_KimiNiTodoke"]')
    out.append('material = SubResource("Mat_Arch_KimiNiTodoke")')
    out.append('size = Vector3(0.06, 3.3, 3.8)')
    out.append('mesh = SubResource("Mesh_Arch_KimiNiTodoke")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/PortalOuter_KimiNiTodoke"]')
    out.append('shape = SubResource("Shape_PortalPanel")')
    out.append('')
    
    # Portal 4 (Josee) at East wall X = 3.22, Z = -42
    out.append('[node name="PortalOuter_Josee" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 3.22, 2.5, -42)')
    out.append('script = ExtResource("2_interactable")')
    out.append('prompt_text = "Lihat Info Section 04"')
    out.append('exhibit_title = "Section 04: Josee, the Tiger and the Fish (2020) — Ocean Dreams"')
    out.append('exhibit_description = "Gerbang menuju sayap penghormatan Josee (ジョゼと虎と魚たち). Didekorasi dengan gradasi biru laut dalam, sinar mentari yang menembus air, serta siluet ikan yang berenang bebas melintasi mimpi Josee."')
    out.append('[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/PortalOuter_Josee"]')
    out.append('mesh = SubResource("Mesh_PortalPanel_Josee")')
    out.append('[node name="ArchFrame" type="MeshInstance3D" parent="GrandHallway/PortalOuter_Josee"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -0.05, 0, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Arch_Josee"]')
    out.append('material = SubResource("Mat_Arch_Josee")')
    out.append('size = Vector3(0.06, 3.3, 3.8)')
    out.append('mesh = SubResource("Mesh_Arch_Josee")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/PortalOuter_Josee"]')
    out.append('shape = SubResource("Shape_PortalPanel")')
    out.append('')
    
    # Welcome Lectern at Lobby
    out.append('[node name="WelcomeLectern" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 9.5)')
    out.append('script = ExtResource("2_interactable")')
    out.append('prompt_text = "Baca Panduan Museum"')
    out.append('exhibit_title = "Museum Karakter Fiksi Hidupku"')
    out.append('exhibit_description = "Selamat datang di lorong memorial karakter fiksi yang telah menemani dan mengubah jalan hidupku.\n\nDi museum ini, setiap sayap ruangan didedikasikan untuk satu karya dan karakter yang memiliki tempat istimewa di hatiku:\n• Section 01 (Kiri): WALL-E (2008)\n• Section 02 (Kanan): A Silent Voice (2016)\n• Section 03 (Kiri): Kimi ni Todoke\n• Section 04 (Kanan): Josee, the Tiger and the Fish (2020)\n\nSilakan menyusuri lorong panjang ini dan nikmati setiap memori yang tersimpan di balik pintu-pintu bertema khusus."')
    out.append('[node name="StandMesh" type="MeshInstance3D" parent="GrandHallway/WelcomeLectern"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.5, 0)')
    out.append('mesh = SubResource("Mesh_LecternStand")')
    out.append('[node name="TopMesh" type="MeshInstance3D" parent="GrandHallway/WelcomeLectern"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 0.965926, 0.258819, 0, -0.258819, 0.965926, 0, 1.05, 0)')
    out.append('mesh = SubResource("Mesh_LecternTop")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/WelcomeLectern"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.7, 0)')
    out.append('shape = SubResource("Shape_Lectern")')
    out.append('')
    
    # Sanctuary Plaque at End of Hallway (Z = -52)
    out.append('[node name="SanctuaryLectern" type="StaticBody3D" parent="GrandHallway"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, -52.0)')
    out.append('script = ExtResource("2_interactable")')
    out.append('prompt_text = "Baca Renungan Akhir"')
    out.append('exhibit_title = "Sanctuary of Stories: Renungan Akhir"')
    out.append('exhibit_description = "Karakter fiksi bukan sekadar bayangan semu di layar kaca. Mereka adalah teman setia yang menemani kita melewati malam-malam paling sepi, memberi kita tawa saat kita lupa cara tersenyum, dan memberi kita keberanian untuk menghadapi hari esok.\n\n• WALL-E mengajarkan cinta tanpa syarat & harapan abadi.\n• Shoko & Shoya mengajarkan pengampunan dan penerimaan diri.\n• Sawako mengajarkan ketulusan yang tak tergoyahkan.\n• Josee mengajarkan keberanian untuk berenang di samudra impian.\n\nTerima kasih telah hadir dan hidup di dalam hatiku selamanya."')
    out.append('[node name="StandMesh" type="MeshInstance3D" parent="GrandHallway/SanctuaryLectern"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.5, 0)')
    out.append('mesh = SubResource("Mesh_LecternStand")')
    out.append('[node name="TopMesh" type="MeshInstance3D" parent="GrandHallway/SanctuaryLectern"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 0.965926, -0.258819, 0, 0.258819, 0.965926, 0, 1.05, 0)')
    out.append('mesh = SubResource("Mesh_LecternTop")')
    out.append('[node name="Collision" type="CollisionShape3D" parent="GrandHallway/SanctuaryLectern"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.7, 0)')
    out.append('shape = SubResource("Shape_Lectern")')
    out.append('')
    
    # Hallway Benches
    for bz in [5.0, -7.0, -21.0, -35.0, -49.0]:
        out.append(f'[node name="Bench_{bz}" type="StaticBody3D" parent="GrandHallway"]')
        out.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.22, {bz})')
        out.append(f'[node name="Mesh" type="MeshInstance3D" parent="GrandHallway/Bench_{bz}"]')
        out.append('mesh = SubResource("Mesh_WoodBench")')
        out.append(f'[node name="Collision" type="CollisionShape3D" parent="GrandHallway/Bench_{bz}"]')
        out.append('shape = SubResource("Shape_Bench")')
        out.append('')

    # Hallway Spotlights & Lighting
    out.append('[node name="HallwayLighting" type="Node3D" parent="GrandHallway"]')
    for lz in [9.0, 0.0, -14.0, -28.0, -42.0, -52.0]:
        out.append(f'[node name="Light_Hall_{lz}" type="OmniLight3D" parent="GrandHallway/HallwayLighting"]')
        out.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 4.6, {lz})')
        out.append('light_color = Color(1.0, 0.95, 0.9, 1)')
        out.append('light_energy = 1.9')
        out.append('omni_range = 14.0')
        out.append('')
        
    # Spotlights on the 4 Thematic Portals
    out.append('[node name="Spot_Portal_Walle" type="SpotLight3D" parent="GrandHallway/HallwayLighting"]')
    out.append('transform = Transform3D(0, 0, 1, 0.5, 0.866025, 0, -0.866025, 0.5, 0, 0, 4.4, 0)')
    out.append('light_color = Color(0.3, 0.85, 1.0, 1)')
    out.append('light_energy = 3.5')
    out.append('spot_range = 8.0')
    out.append('spot_angle = 45.0')
    out.append('')
    
    out.append('[node name="Spot_Portal_SilentVoice" type="SpotLight3D" parent="GrandHallway/HallwayLighting"]')
    out.append('transform = Transform3D(0, 0, -1, -0.5, 0.866025, 0, 0.866025, 0.5, 0, 0, 4.4, -14)')
    out.append('light_color = Color(1.0, 0.8, 0.88, 1)')
    out.append('light_energy = 3.5')
    out.append('spot_range = 8.0')
    out.append('spot_angle = 45.0')
    out.append('')
    
    out.append('[node name="Spot_Portal_KimiNiTodoke" type="SpotLight3D" parent="GrandHallway/HallwayLighting"]')
    out.append('transform = Transform3D(0, 0, 1, 0.5, 0.866025, 0, -0.866025, 0.5, 0, 0, 4.4, -28)')
    out.append('light_color = Color(1.0, 0.9, 0.7, 1)')
    out.append('light_energy = 3.5')
    out.append('spot_range = 8.0')
    out.append('spot_angle = 45.0')
    out.append('')
    
    out.append('[node name="Spot_Portal_Josee" type="SpotLight3D" parent="GrandHallway/HallwayLighting"]')
    out.append('transform = Transform3D(0, 0, -1, -0.5, 0.866025, 0, 0.866025, 0.5, 0, 0, 4.4, -42)')
    out.append('light_color = Color(0.2, 0.8, 1.0, 1)')
    out.append('light_energy = 3.5')
    out.append('spot_range = 8.0')
    out.append('spot_angle = 45.0')
    out.append('')
    
    # ----------------------------------------------------
    # HELPER TO BUILD EACH ROOM
    # ----------------------------------------------------
    def build_room(room_id, room_name, cx, cz, is_west, floor_mesh_id, 
                   light_color_str,
                   poster_mesh_id, poster_title, poster_desc,
                   photo1_mesh_id, photo1_title, photo1_desc,
                   photo2_mesh_id, photo2_title, photo2_desc,
                   tribute_title, tribute_desc,
                   bio_title, bio_desc):
        
        r_lines = []
        r_lines.append(f'[node name="{room_id}" type="Node3D" parent="."] ')
        r_lines.append('')
        
        # Floor
        r_lines.append(f'[node name="Floor" type="StaticBody3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {cx}, -0.25, {cz})')
        r_lines.append(f'[node name="Mesh" type="MeshInstance3D" parent="{room_id}/Floor"]')
        r_lines.append(f'mesh = SubResource("{floor_mesh_id}")')
        r_lines.append(f'[node name="Collision" type="CollisionShape3D" parent="{room_id}/Floor"]')
        r_lines.append('shape = SubResource("Shape_RoomFloor")')
        r_lines.append('')
        
        # Ceiling
        r_lines.append(f'[node name="Ceiling" type="MeshInstance3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {cx}, 5.2, {cz})')
        r_lines.append('mesh = SubResource("Mesh_RoomCeiling")')
        r_lines.append('')
        
        # North Wall (Z = cz - 7.0) -> Holds Movie Poster
        nw_z = cz - 6.8
        r_lines.append(f'[node name="NorthWall" type="StaticBody3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {cx}, 2.5, {nw_z})')
        r_lines.append(f'[node name="Mesh" type="MeshInstance3D" parent="{room_id}/NorthWall"]')
        r_lines.append('mesh = SubResource("Mesh_RoomWallNS")')
        r_lines.append(f'[node name="Collision" type="CollisionShape3D" parent="{room_id}/NorthWall"]')
        r_lines.append('shape = SubResource("Shape_RoomWallNS")')
        r_lines.append('')
        
        # South Wall (Z = cz + 7.0) -> Holds Photos
        sw_z = cz + 6.8
        r_lines.append(f'[node name="SouthWall" type="StaticBody3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {cx}, 2.5, {sw_z})')
        r_lines.append(f'[node name="Mesh" type="MeshInstance3D" parent="{room_id}/SouthWall"]')
        r_lines.append('mesh = SubResource("Mesh_RoomWallNS")')
        r_lines.append(f'[node name="Collision" type="CollisionShape3D" parent="{room_id}/SouthWall"]')
        r_lines.append('shape = SubResource("Shape_RoomWallNS")')
        r_lines.append('')
        
        # Outer Outer Wall (Far wall away from hallway)
        far_x = (cx - 6.8) if is_west else (cx + 6.8)
        r_lines.append(f'[node name="FarWall" type="StaticBody3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {far_x}, 2.5, {cz})')
        r_lines.append(f'[node name="Mesh" type="MeshInstance3D" parent="{room_id}/FarWall"]')
        r_lines.append('mesh = SubResource("Mesh_RoomWallEW")')
        r_lines.append(f'[node name="Collision" type="CollisionShape3D" parent="{room_id}/FarWall"]')
        r_lines.append('shape = SubResource("Shape_RoomWallEW")')
        r_lines.append('')
        
        # Inner Wall Segments (Facing hallway, with central 3.6m door)
        near_x = (cx + 6.8) if is_west else (cx - 6.8)
        # Seg N: Z from cz-1.8 to cz-7.0 (center cz - 4.4, length 5.2)
        r_lines.append(f'[node name="NearWallN" type="StaticBody3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {near_x}, 2.5, {cz - 4.4})')
        r_lines.append(f'[node name="Mesh" type="MeshInstance3D" parent="{room_id}/NearWallN"]')
        r_lines.append('mesh = SubResource("Mesh_RoomDoorWall")')
        r_lines.append(f'[node name="Collision" type="CollisionShape3D" parent="{room_id}/NearWallN"]')
        r_lines.append('shape = SubResource("Shape_RoomDoorWall")')
        r_lines.append('')
        
        # Seg S: Z from cz+1.8 to cz+7.0 (center cz + 4.4, length 5.2)
        r_lines.append(f'[node name="NearWallS" type="StaticBody3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {near_x}, 2.5, {cz + 4.4})')
        r_lines.append(f'[node name="Mesh" type="MeshInstance3D" parent="{room_id}/NearWallS"]')
        r_lines.append('mesh = SubResource("Mesh_RoomDoorWall")')
        r_lines.append(f'[node name="Collision" type="CollisionShape3D" parent="{room_id}/NearWallS"]')
        r_lines.append('shape = SubResource("Shape_RoomDoorWall")')
        r_lines.append('')
        
        # Doorway Lintel
        r_lines.append(f'[node name="DoorwayLintel" type="StaticBody3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {near_x}, 4.25, {cz})')
        r_lines.append(f'[node name="Mesh" type="MeshInstance3D" parent="{room_id}/DoorwayLintel"]')
        r_lines.append('mesh = SubResource("Mesh_DoorLintel")')
        r_lines.append(f'[node name="Collision" type="CollisionShape3D" parent="{room_id}/DoorwayLintel"]')
        r_lines.append('shape = SubResource("Shape_DoorLintel")')
        r_lines.append('')
        
        # Room Ambient & Spot Lights
        r_lines.append(f'[node name="RoomLight" type="OmniLight3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {cx}, 4.6, {cz})')
        r_lines.append(f'light_color = {light_color_str}')
        r_lines.append('light_energy = 2.4')
        r_lines.append('omni_range = 16.0')
        r_lines.append('')
        
        # 1. MOVIE POSTER (North Wall)
        p_z = cz - 6.6
        r_lines.append(f'[node name="MoviePoster" type="StaticBody3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {cx}, 2.5, {p_z})')
        r_lines.append('script = ExtResource("2_interactable")')
        r_lines.append('prompt_text = "Lihat Poster Film"')
        r_lines.append(f'exhibit_title = "{poster_title}"')
        r_lines.append(f'exhibit_description = "{poster_desc}"')
        r_lines.append(f'[node name="FrameMesh" type="MeshInstance3D" parent="{room_id}/MoviePoster"]')
        r_lines.append('mesh = SubResource("Mesh_PosterFrame")')
        r_lines.append(f'[node name="CanvasMesh" type="MeshInstance3D" parent="{room_id}/MoviePoster"]')
        r_lines.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0.05)')
        r_lines.append(f'mesh = SubResource("{poster_mesh_id}")')
        r_lines.append(f'[node name="Collision" type="CollisionShape3D" parent="{room_id}/MoviePoster"]')
        r_lines.append('shape = SubResource("Shape_Poster")')
        r_lines.append('')
        
        r_lines.append(f'[node name="SpotPoster" type="SpotLight3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 0.707107, 0.707107, 0, -0.707107, 0.707107, {cx}, 4.6, {cz - 4.5})')
        r_lines.append('light_color = Color(1.0, 0.96, 0.92, 1)')
        r_lines.append('light_energy = 3.6')
        r_lines.append('spot_range = 6.5')
        r_lines.append('spot_angle = 42.0')
        r_lines.append('')
        
        # 2. GALLERY PHOTO 1 (South Wall Left: cx - 3.2)
        ph1_z = cz + 6.6
        r_lines.append(f'[node name="GalleryPhoto1" type="StaticBody3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {cx - 3.2}, 2.5, {ph1_z})')
        r_lines.append('script = ExtResource("2_interactable")')
        r_lines.append('prompt_text = "Lihat Foto Kenangan"')
        r_lines.append(f'exhibit_title = "{photo1_title}"')
        r_lines.append(f'exhibit_description = "{photo1_desc}"')
        r_lines.append(f'[node name="FrameMesh" type="MeshInstance3D" parent="{room_id}/GalleryPhoto1"]')
        r_lines.append('mesh = SubResource("Mesh_PhotoFrame")')
        r_lines.append(f'[node name="CanvasMesh" type="MeshInstance3D" parent="{room_id}/GalleryPhoto1"]')
        r_lines.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, -0.05)')
        r_lines.append(f'mesh = SubResource("{photo1_mesh_id}")')
        r_lines.append(f'[node name="Collision" type="CollisionShape3D" parent="{room_id}/GalleryPhoto1"]')
        r_lines.append('shape = SubResource("Shape_Photo")')
        r_lines.append('')
        
        # 3. GALLERY PHOTO 2 (South Wall Right: cx + 3.2)
        r_lines.append(f'[node name="GalleryPhoto2" type="StaticBody3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {cx + 3.2}, 2.5, {ph1_z})')
        r_lines.append('script = ExtResource("2_interactable")')
        r_lines.append('prompt_text = "Lihat Foto Kenangan"')
        r_lines.append(f'exhibit_title = "{photo2_title}"')
        r_lines.append(f'exhibit_description = "{photo2_desc}"')
        r_lines.append(f'[node name="FrameMesh" type="MeshInstance3D" parent="{room_id}/GalleryPhoto2"]')
        r_lines.append('mesh = SubResource("Mesh_PhotoFrame")')
        r_lines.append(f'[node name="CanvasMesh" type="MeshInstance3D" parent="{room_id}/GalleryPhoto2"]')
        r_lines.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, -0.05)')
        r_lines.append(f'mesh = SubResource("{photo2_mesh_id}")')
        r_lines.append(f'[node name="Collision" type="CollisionShape3D" parent="{room_id}/GalleryPhoto2"]')
        r_lines.append('shape = SubResource("Shape_Photo")')
        r_lines.append('')
        
        # Spotlights for South Wall Photos
        r_lines.append(f'[node name="SpotPhotos" type="SpotLight3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 0.707107, -0.707107, 0, 0.707107, 0.707107, {cx}, 4.6, {cz + 4.5})')
        r_lines.append('light_color = Color(1.0, 0.96, 0.92, 1)')
        r_lines.append('light_energy = 3.6')
        r_lines.append('spot_range = 6.5')
        r_lines.append('spot_angle = 50.0')
        r_lines.append('')
        
        # 4. BIOGRAPHY & PERSONAL REFLECTION LECTERN (Near entrance inside room)
        lectern_x = (cx + 4.5) if is_west else (cx - 4.5)
        lectern_z = cz + 2.8
        r_lines.append(f'[node name="BioLectern" type="StaticBody3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {lectern_x}, 0, {lectern_z})')
        r_lines.append('script = ExtResource("2_interactable")')
        r_lines.append('prompt_text = "Baca Kisah Karakter"')
        r_lines.append(f'exhibit_title = "{bio_title}"')
        r_lines.append(f'exhibit_description = "{bio_desc}"')
        r_lines.append(f'[node name="StandMesh" type="MeshInstance3D" parent="{room_id}/BioLectern"]')
        r_lines.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.5, 0)')
        r_lines.append('mesh = SubResource("Mesh_LecternStand")')
        r_lines.append(f'[node name="TopMesh" type="MeshInstance3D" parent="{room_id}/BioLectern"]')
        r_lines.append('transform = Transform3D(1, 0, 0, 0, 0.965926, 0.258819, 0, -0.258819, 0.965926, 0, 1.05, 0)')
        r_lines.append('mesh = SubResource("Mesh_LecternTop")')
        r_lines.append(f'[node name="Collision" type="CollisionShape3D" parent="{room_id}/BioLectern"]')
        r_lines.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.7, 0)')
        r_lines.append('shape = SubResource("Shape_Lectern")')
        r_lines.append('')
        
        # Centerpiece Spotlight
        r_lines.append(f'[node name="SpotCenter" type="SpotLight3D" parent="{room_id}"]')
        r_lines.append(f'transform = Transform3D(1, 0, 0, 0, 0.173648, 0.984808, 0, -0.984808, 0.173648, {cx}, 4.8, {cz})')
        r_lines.append(f'light_color = {light_color_str}')
        r_lines.append('light_energy = 4.0')
        r_lines.append('spot_range = 7.5')
        r_lines.append('spot_angle = 45.0')
        r_lines.append('')
        
        return r_lines

    # ----------------------------------------------------
    # BUILD ROOM 1: WALL-E (West side, cx = -13.5, cz = 0)
    # ----------------------------------------------------
    walle_poster_desc = "WALL·E (2008) - Sutradara Andrew Stanton (Pixar Animation Studios).\\n\\nDi masa depan ketika bumi ditinggalkan manusia karena gunungan sampah yang tak tertangani, hanya tersisa satu robot unit kecil yang masih setia menjalankan tugasnya selama lebih dari 700 tahun: Waste Allocation Load Lifter: Earth-Class (WALL-E)."
    walle_photo1_desc = "Meskipun hanya sebuah mesin pemadat rongsokan, WALL-E mengembangkan jiwa penjelajah yang menakjubkan. Dia mengoleksi pemantik api kuno, kubus rubik warna-warni, bola lampu, dan rekaman kaset film musikal 'Hello, Dolly!'. Dia merawat hal-hal kecil yang terlupakan dengan penuh kelembutan rasa ingin tahu."
    walle_photo2_desc = "Saat EVE tiba di bumi dalam misi rahasia, WALL-E rela menyeberangi luasnya galaksi tanpa ragu hanya untuk berada di sampingnya. Momen ketika kedua tangan mekanik mereka saling bertaut adalah simbol cinta paling murni tanpa sepatah kata pun terucap."
    walle_bio_desc = "WALL-E bukan sekadar film animasi fiksi ilmiah biasa bagi hidupku.\\n\\nKarakter WALL-E mengajarkan arti kesendirian yang indah: bagaimana di tengah dunia yang hancur dan sepi, dia tetap menyimpan jiwa yang hangat, mendengarkan lagu cinta lama, merawat kecoak kecil temannya, dan menjaga rasa ingin tahu yang murni.\\n\\nKetika dia bertemu EVE, dia memberikan segalanya tanpa pamrih. Dia mengajarkanku bahwa cinta sejati bukanlah kata-kata mutiara rumit, melainkan tindakan nyata: memegang tangan seseorang, melindunginya dari hujan petir, dan menolak untuk menyerah pada harapan sekecil apa pun."
    walle_tribute_desc = "Patung memorial WALL-E yang menggenggam sebuah sepatu boot bekas berisi tunas tanaman hijau kecil yang masih hidup.\\n\\nTunas ini adalah bukti bahwa kehidupan selalu menemukan jalannya kembali. WALL-E mengajarkan kita untuk tidak hanya 'bertahan hidup' (survive), melainkan benar-benar 'hidup' (live)."
    
    out.extend(build_room(
        "Room_WallE", "WALL-E", -13.5, 0.0, True, "Mesh_RoomFloor_Walle",
        "Color(0.85, 0.95, 1.0, 1)",
        "Mesh_Canvas_Poster_Walle", "Poster Resmi: WALL·E (2008)", walle_poster_desc,
        "Mesh_Canvas_Photo_Walle_1", "WALL-E & Jiwa Penjelajah", walle_photo1_desc,
        "Mesh_Canvas_Photo_Walle_2", "WALL-E & EVE: Direktif Cinta", walle_photo2_desc,
        "Monumen WALL-E & Tunas Hijau", walle_tribute_desc,
        "Kenangan WALL-E: Makna Kesetiaan & Cinta Tulus", walle_bio_desc
    ))
    
    # Room 1 Centerpiece 3D Model: WALL-E with Plant in Boot
    out.append('[node name="Tribute_WallE" type="StaticBody3D" parent="Room_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -13.5, 0, 0)')
    out.append('script = ExtResource("2_interactable")')
    out.append('prompt_text = "Amati WALL-E & Tunas Hijau"')
    out.append('exhibit_title = "Monumen WALL-E & Tunas Hijau Dalam Sepatu"')
    out.append(f'exhibit_description = "{walle_tribute_desc}"')
    # Pedestal
    out.append('[node name="PedestalMesh" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.35, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Pedestal_Walle"]')
    out.append('material = SubResource("Mat_Pedestal")')
    out.append('size = Vector3(2.4, 0.7, 2.4)')
    out.append('mesh = SubResource("Mesh_Pedestal_Walle")')
    # Body Chassis
    out.append('[node name="BodyMesh" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1.25, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Walle_Chassis"]')
    out.append('material = SubResource("Mat_WalleYellow")')
    out.append('size = Vector3(0.9, 0.8, 0.8)')
    out.append('mesh = SubResource("Mesh_Walle_Chassis")')
    # Solar Gauge Bar on front
    out.append('[node name="SolarGauge" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1.45, 0.41)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Walle_Gauge"]')
    out.append('material = SubResource("Mat_PlantGreen")')
    out.append('size = Vector3(0.5, 0.08, 0.04)')
    out.append('mesh = SubResource("Mesh_Walle_Gauge")')
    # Left Tread
    out.append('[node name="LeftTread" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -0.6, 1.1, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Walle_Tread"]')
    out.append('material = SubResource("Mat_Beam")')
    out.append('size = Vector3(0.25, 0.65, 1.05)')
    out.append('mesh = SubResource("Mesh_Walle_Tread")')
    # Right Tread
    out.append('[node name="RightTread" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0.6, 1.1, 0)')
    out.append('mesh = SubResource("Mesh_Walle_Tread")')
    # Neck
    out.append('[node name="Neck" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1.8, -0.1)')
    out.append('[sub_resource type="CylinderMesh" id="Mesh_Walle_Neck"]')
    out.append('material = SubResource("Mat_Beam")')
    out.append('top_radius = 0.08')
    out.append('bottom_radius = 0.08')
    out.append('height = 0.4')
    out.append('mesh = SubResource("Mesh_Walle_Neck")')
    # Eyes (Left & Right Binoculars)
    out.append('[node name="EyeLeft" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(0.965926, 0, 0.258819, 0, 1, 0, -0.258819, 0, 0.965926, -0.2, 2.05, 0)')
    out.append('[sub_resource type="CylinderMesh" id="Mesh_Walle_Eye"]')
    out.append('material = SubResource("Mat_WalleYellow")')
    out.append('top_radius = 0.16')
    out.append('bottom_radius = 0.18')
    out.append('height = 0.35')
    out.append('mesh = SubResource("Mesh_Walle_Eye")')
    out.append('[node name="EyeLensLeft" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -0.2, 2.05, 0.18)')
    out.append('[sub_resource type="SphereMesh" id="Mesh_Walle_Lens"]')
    out.append('material = SubResource("Mat_WalleEyes")')
    out.append('radius = 0.12')
    out.append('height = 0.24')
    out.append('mesh = SubResource("Mesh_Walle_Lens")')
    out.append('[node name="EyeRight" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(0.965926, 0, -0.258819, 0, 1, 0, 0.258819, 0, 0.965926, 0.2, 2.05, 0)')
    out.append('mesh = SubResource("Mesh_Walle_Eye")')
    out.append('[node name="EyeLensRight" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0.2, 2.05, 0.18)')
    out.append('mesh = SubResource("Mesh_Walle_Lens")')
    # Little Boot with Plant in front of WALL-E
    out.append('[node name="BootMesh" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.85, 0.65)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Boot"]')
    out.append('material = SubResource("Mat_Beam")')
    out.append('size = Vector3(0.24, 0.26, 0.36)')
    out.append('mesh = SubResource("Mesh_Boot")')
    out.append('[node name="PlantStem" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1.08, 0.65)')
    out.append('[sub_resource type="CylinderMesh" id="Mesh_PlantStem"]')
    out.append('material = SubResource("Mat_PlantGreen")')
    out.append('top_radius = 0.02')
    out.append('bottom_radius = 0.03')
    out.append('height = 0.22')
    out.append('mesh = SubResource("Mesh_PlantStem")')
    out.append('[node name="PlantLeaf" type="MeshInstance3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(0.707107, -0.707107, 0, 0.707107, 0.707107, 0, 0, 0, 1, 0.08, 1.18, 0.65)')
    out.append('[sub_resource type="PrismMesh" id="Mesh_PlantLeaf"]')
    out.append('material = SubResource("Mat_PlantGreen")')
    out.append('size = Vector3(0.12, 0.16, 0.04)')
    out.append('mesh = SubResource("Mesh_PlantLeaf")')
    # Collision
    out.append('[node name="Collision" type="CollisionShape3D" parent="Room_WallE/Tribute_WallE"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1.15, 0)')
    out.append('[sub_resource type="BoxShape3D" id="Shape_Tribute_WallE"]')
    out.append('size = Vector3(2.4, 2.3, 2.4)')
    out.append('shape = SubResource("Shape_Tribute_WallE")')
    out.append('')

    # ----------------------------------------------------
    # BUILD ROOM 2: A SILENT VOICE (East side, cx = 13.5, cz = -14)
    # ----------------------------------------------------
    silent_poster_desc = "A Silent Voice / Koe no Katachi (2016) - Sutradara Naoko Yamada (Kyoto Animation).\\n\\nSebuah karya film animasi mengguncang jiwa yang diadaptasi dari manga karya Yoshitoki Oima. Mengangkat tema penerimaan diri, trauma perundungan, rasa bersalah yang melumpuhkan, dan perjuangan tulus untuk saling mendengar isi hati."
    silent_photo1_desc = "Buku catatan komunikasi bergaris tempat Shoko Nishimiya menuliskan kalimat perkenalan pertamanya: 'Nama saya Nishimiya Shoko. Saya tidak bisa mendengar.' Buku yang sempat dibuang ke kolam ikan ini menjadi saksi bisu kesabaran dan keikhlasan hati Shoko."
    silent_photo2_desc = "Di atas jembatan memberi makan ikan koi bersama roti tawar, Shoko dan Shoya perlahan membangun kembali jembatan komunikasi yang pernah hancur. Bahasa isyarat yang mereka pelajari bukan sekadar gerak tangan, melainkan jembatan jiwa."
    silent_bio_desc = "Film ini menyelamatkan cara pandangku terhadap orang-orang di sekitarku.\\n\\nTanda silang 'X' di wajah orang-orang yang dilihat oleh Shoya adalah gambaran paling akurat tentang bagaimana kecemasan dan rasa benci pada diri sendiri bisa membuat kita menutup telinga dari dunia.\\n\\nSaat tanda silang itu akhirnya jatuh di festival sekolah dan air mata Shoya mengalir, aku menyadari bahwa dunia ini layak untuk didengar. Setiap orang sedang bertarung melawan rasa bersalahnya masing-masing, dan hadiah terbesar yang bisa kita berikan adalah pengampunan."
    silent_tribute_desc = "Memorial kolam zen dengan jembatan kayu kecil, guguran kelopak sakura, dan buku catatan komunikasi Shoko yang bercahaya lembut.\\n\\nMenyimbolkan keberanian untuk memaafkan mereka yang pernah menyakiti kita, dan yang terpenting: keberanian untuk memaafkan diri sendiri."
    
    out.extend(build_room(
        "Room_SilentVoice", "A Silent Voice", 13.5, -14.0, False, "Mesh_RoomFloor_SilentVoice",
        "Color(1.0, 0.94, 0.96, 1)",
        "Mesh_Canvas_Poster_SilentVoice", "Poster Resmi: A Silent Voice (聲の形)", silent_poster_desc,
        "Mesh_Canvas_Photo_SilentVoice_1", "Buku Catatan Komunikasi Shoko", silent_photo1_desc,
        "Mesh_Canvas_Photo_SilentVoice_2", "Senyuman Shoko di Jembatan Suimon", silent_photo2_desc,
        "Memorial Jembatan Suimon & Buku Catatan Hati", silent_tribute_desc,
        "Kenangan A Silent Voice: Pengampunan & Membuka Hati", silent_bio_desc
    ))
    
    # Room 2 Centerpiece 3D Model: Zen Pond, Bridge & Glowing Notebook
    out.append('[node name="Tribute_SilentVoice" type="StaticBody3D" parent="Room_SilentVoice"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 13.5, 0, -14)')
    out.append('script = ExtResource("2_interactable")')
    out.append('prompt_text = "Baca Catatan Shoko"')
    out.append('exhibit_title = "Memorial Kolam Koi & Buku Catatan Hati"')
    out.append(f'exhibit_description = "{silent_tribute_desc}"')
    # Circular Stone Pedestal
    out.append('[node name="PedestalStone" type="MeshInstance3D" parent="Room_SilentVoice/Tribute_SilentVoice"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.25, 0)')
    out.append('[sub_resource type="CylinderMesh" id="Mesh_Stone_Pond"]')
    out.append('material = SubResource("Mat_Pedestal")')
    out.append('top_radius = 1.6')
    out.append('bottom_radius = 1.7')
    out.append('height = 0.5')
    out.append('mesh = SubResource("Mesh_Stone_Pond")')
    # Water Disc Inset
    out.append('[node name="WaterDisc" type="MeshInstance3D" parent="Room_SilentVoice/Tribute_SilentVoice"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.52, 0)')
    out.append('[sub_resource type="CylinderMesh" id="Mesh_Water_Disc"]')
    out.append('material = SubResource("Mat_ZenWater")')
    out.append('top_radius = 1.45')
    out.append('bottom_radius = 1.45')
    out.append('height = 0.04')
    out.append('mesh = SubResource("Mesh_Water_Disc")')
    # Japanese Red Wood Bridge Arch
    out.append('[node name="BridgePlank" type="MeshInstance3D" parent="Room_SilentVoice/Tribute_SilentVoice"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.65, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_BridgePlank"]')
    out.append('material = SubResource("Mat_RunnerCarpet")')
    out.append('size = Vector3(1.8, 0.12, 0.6)')
    out.append('mesh = SubResource("Mesh_BridgePlank")')
    # Center Acrylic Stand for Notebook
    out.append('[node name="StandMesh" type="MeshInstance3D" parent="Room_SilentVoice/Tribute_SilentVoice"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.95, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_NotebookStand"]')
    out.append('material = SubResource("Mat_Pedestal")')
    out.append('size = Vector3(0.5, 0.5, 0.4)')
    out.append('mesh = SubResource("Mesh_NotebookStand")')
    # The Communication Notebook
    out.append('[node name="NotebookMesh" type="MeshInstance3D" parent="Room_SilentVoice/Tribute_SilentVoice"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 0.965926, 0.258819, 0, -0.258819, 0.965926, 0, 1.25, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Notebook"]')
    out.append('material = SubResource("Mat_Pedestal")')
    out.append('size = Vector3(0.44, 0.05, 0.32)')
    out.append('mesh = SubResource("Mesh_Notebook")')
    # Blue Ribbon Bookmark
    out.append('[node name="RibbonMesh" type="MeshInstance3D" parent="Room_SilentVoice/Tribute_SilentVoice"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0.08, 1.28, 0.05)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Ribbon"]')
    out.append('material = SubResource("Mat_OceanBlue")')
    out.append('size = Vector3(0.04, 0.06, 0.25)')
    out.append('mesh = SubResource("Mesh_Ribbon")')
    # Falling Sakura Petals around base
    for s_idx, (sx, sz) in enumerate([(-0.6, 0.5), (0.7, -0.4), (-0.3, -0.7), (0.5, 0.6)]):
        out.append(f'[node name="Petal_{s_idx}" type="MeshInstance3D" parent="Room_SilentVoice/Tribute_SilentVoice"]')
        out.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {sx}, 0.56, {sz})')
        out.append('[sub_resource type="SphereMesh" id="Mesh_Petal"]')
        out.append('material = SubResource("Mat_SakuraPetals")')
        out.append('radius = 0.06')
        out.append('height = 0.03')
        out.append('mesh = SubResource("Mesh_Petal")')
    # Collision
    out.append('[node name="Collision" type="CollisionShape3D" parent="Room_SilentVoice/Tribute_SilentVoice"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.75, 0)')
    out.append('[sub_resource type="CylinderShape3D" id="Shape_Tribute_SilentVoice"]')
    out.append('radius = 1.7')
    out.append('height = 1.5')
    out.append('shape = SubResource("Shape_Tribute_SilentVoice")')
    out.append('')

    # ----------------------------------------------------
    # BUILD ROOM 3: KIMI NI TODOKE (West side, cx = -13.5, cz = -28)
    # ----------------------------------------------------
    kimi_poster_desc = "Kimi ni Todoke (君に届け / From Me to You) - Production I.G (Karuho Shiina).\\n\\nMenceritakan kisah Sawako Kuronuma yang dijuluki 'Sadako' oleh teman-temannya karena sifatnya yang pemalu dan pendiam, serta bagaimana pertemuannya dengan Shota Kazehaya mengubah dunianya selamanya dengan kehangatan dan ketulusan."
    kimi_photo1_desc = "Sawako adalah definisi jiwa paling murni. Walaupun sering ditakuti dan dijauhi teman sekelas karena penampilannya yang mirip tokoh horor, dia tidak pernah menaruh dendam. Dia selalu bangun paling pagi untuk membersihkan kelas dan menyiram tanaman sekolah."
    kimi_photo2_desc = "Momen legendaris di hari pertama masuk sekolah menengah atas, saat Kazehaya tersesat di persimpangan jalan dan bertanya arah pada Sawako di bawah pohon sakura. Senyuman tulus Kazehaya adalah sinar mentari pertama yang menyinari hari-hari Sawako."
    kimi_bio_desc = "Kimi ni Todoke mengajarkanku kekuatan luar biasa dari ketulusan tanpa pamrih.\\n\\nDi dunia yang penuh dengan kepura-puraan dan penilaian dangkal dari penampilan luar, Sawako membuktikan bahwa kebaikan yang tulus pada akhirnya akan 'sampai' ke hati orang lain.\\n\\nKisah ini selalu menghangatkan hatiku saat aku merasa disalahpahami, mengingatkanku bahwa tidak ada kebaikan yang sia-sia jika dilakukan dengan hati yang bersih."
    kimi_tribute_desc = "Bangku dan meja kelas sekolah tempat Sawako belajar dengan tekun, ditemani buku catatan tulisan tangannya dan burung bangau kertas origami.\\n\\nSimbol awal mula persahabatan sejati bersama Chizuru dan Ayane, serta keberanian menyampaikan isi hati."
    
    out.extend(build_room(
        "Room_KimiNiTodoke", "Kimi ni Todoke", -13.5, -28.0, True, "Mesh_RoomFloor_KimiNiTodoke",
        "Color(1.0, 0.95, 0.9, 1)",
        "Mesh_Canvas_Poster_KimiNiTodoke", "Poster Resmi: Kimi ni Todoke (君に届け)", kimi_poster_desc,
        "Mesh_Canvas_Photo_KimiNiTodoke_1", "Ketulusan Senyuman Sawako", kimi_photo1_desc,
        "Mesh_Canvas_Photo_KimiNiTodoke_2", "Di Bawah Ranting Sakura Bersama Kazehaya", kimi_photo2_desc,
        "Memorial Bangku Kelas & Bangau Kertas", kimi_tribute_desc,
        "Kenangan Kimi ni Todoke: Ketulusan & Cinta Pertama", kimi_bio_desc
    ))
    
    # Room 3 Centerpiece 3D Model: Classroom Desk, Chair, Origami Crane
    out.append('[node name="Tribute_KimiNiTodoke" type="StaticBody3D" parent="Room_KimiNiTodoke"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -13.5, 0, -28)')
    out.append('script = ExtResource("2_interactable")')
    out.append('prompt_text = "Amati Meja Kelas Sawako"')
    out.append('exhibit_title = "Memorial Bangku Sekolah & Bangau Kertas Harapan"')
    out.append(f'exhibit_description = "{kimi_tribute_desc}"')
    # Wooden Platform Base
    out.append('[node name="BasePlatform" type="MeshInstance3D" parent="Room_KimiNiTodoke/Tribute_KimiNiTodoke"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.15, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Kimi_Base"]')
    out.append('material = SubResource("Mat_Pedestal")')
    out.append('size = Vector3(2.4, 0.3, 2.4)')
    out.append('mesh = SubResource("Mesh_Kimi_Base")')
    # School Desk Top
    out.append('[node name="DeskTop" type="MeshInstance3D" parent="Room_KimiNiTodoke/Tribute_KimiNiTodoke"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.85, -0.2)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_School_DeskTop"]')
    out.append('material = SubResource("Mat_WoodBench")')
    out.append('size = Vector3(1.0, 0.06, 0.65)')
    out.append('mesh = SubResource("Mesh_School_DeskTop")')
    # School Desk Steel Legs
    out.append('[node name="DeskLegs" type="MeshInstance3D" parent="Room_KimiNiTodoke/Tribute_KimiNiTodoke"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.5, -0.2)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_School_DeskLegs"]')
    out.append('material = SubResource("Mat_Beam")')
    out.append('size = Vector3(0.9, 0.65, 0.55)')
    out.append('mesh = SubResource("Mesh_School_DeskLegs")')
    # School Chair Seat
    out.append('[node name="ChairSeat" type="MeshInstance3D" parent="Room_KimiNiTodoke/Tribute_KimiNiTodoke"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.55, 0.45)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_School_ChairSeat"]')
    out.append('material = SubResource("Mat_WoodBench")')
    out.append('size = Vector3(0.5, 0.05, 0.5)')
    out.append('mesh = SubResource("Mesh_School_ChairSeat")')
    # Chair Backrest
    out.append('[node name="ChairBack" type="MeshInstance3D" parent="Room_KimiNiTodoke/Tribute_KimiNiTodoke"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.9, 0.68)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_School_ChairBack"]')
    out.append('material = SubResource("Mat_WoodBench")')
    out.append('size = Vector3(0.48, 0.35, 0.04)')
    out.append('mesh = SubResource("Mesh_School_ChairBack")')
    # Chair Legs
    out.append('[node name="ChairLegs" type="MeshInstance3D" parent="Room_KimiNiTodoke/Tribute_KimiNiTodoke"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.42, 0.45)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_School_ChairLegs"]')
    out.append('material = SubResource("Mat_Beam")')
    out.append('size = Vector3(0.46, 0.48, 0.46)')
    out.append('mesh = SubResource("Mesh_School_ChairLegs")')
    # Origami Paper Crane on Desk
    out.append('[node name="OrigamiCrane" type="MeshInstance3D" parent="Room_KimiNiTodoke/Tribute_KimiNiTodoke"]')
    out.append('transform = Transform3D(0.866025, 0, 0.5, 0, 1, 0, -0.5, 0, 0.866025, 0.25, 0.92, -0.2)')
    out.append('[sub_resource type="PrismMesh" id="Mesh_Crane"]')
    out.append('material = SubResource("Mat_Pedestal")')
    out.append('size = Vector3(0.12, 0.1, 0.12)')
    out.append('mesh = SubResource("Mesh_Crane")')
    # Cherry Blossom Miniature Tree / Branch on corner of base
    out.append('[node name="SakuraTrunk" type="MeshInstance3D" parent="Room_KimiNiTodoke/Tribute_KimiNiTodoke"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -0.85, 0.75, 0.85)')
    out.append('[sub_resource type="CylinderMesh" id="Mesh_SakuraTrunk"]')
    out.append('material = SubResource("Mat_WoodBench")')
    out.append('top_radius = 0.05')
    out.append('bottom_radius = 0.08')
    out.append('height = 0.9')
    out.append('mesh = SubResource("Mesh_SakuraTrunk")')
    out.append('[node name="SakuraCanopy" type="MeshInstance3D" parent="Room_KimiNiTodoke/Tribute_KimiNiTodoke"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -0.85, 1.35, 0.85)')
    out.append('[sub_resource type="SphereMesh" id="Mesh_SakuraCanopy"]')
    out.append('material = SubResource("Mat_SakuraPetals")')
    out.append('radius = 0.38')
    out.append('height = 0.65')
    out.append('mesh = SubResource("Mesh_SakuraCanopy")')
    # Collision
    out.append('[node name="Collision" type="CollisionShape3D" parent="Room_KimiNiTodoke/Tribute_KimiNiTodoke"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.8, 0)')
    out.append('[sub_resource type="BoxShape3D" id="Shape_Tribute_KimiNiTodoke"]')
    out.append('size = Vector3(2.4, 1.6, 2.4)')
    out.append('shape = SubResource("Shape_Tribute_KimiNiTodoke")')
    out.append('')

    # ----------------------------------------------------
    # BUILD ROOM 4: JOSEE, THE TIGER AND THE FISH (East side, cx = 13.5, cz = -42)
    # ----------------------------------------------------
    josee_poster_desc = "Josee, the Tiger and the Fish (ジョゼと虎と魚たち) - Studio Bones (2020), Sutradara Kotaro Tamura.\\n\\nKisah luar biasa tentang Josee (Kumiko Yamamura), gadis difabel yang melarikan diri ke dalam dunia imajinasi dan lukisan, serta Tsuneo Suzukawa, pemuda pecinta laut yang mengajarkannya bahwa samudra mimpi bisa diarungi bersama."
    josee_photo1_desc = "Saat pertama kali Tsuneo membawanya melihat laut secara langsung, Josee menyentuh deburan ombak dengan tangan gemetar. Laut yang selama ini hanya ada di dalam buku bacaan dan kanvas lukisannya akhirnya menjadi kenyataan yang bisa dirasakan."
    josee_photo2_desc = "Di balik sikapnya yang galak dan sering menyebut Tsuneo sebagai pelayannya, Josee memiliki ketakutan besar terhadap 'Harimau' dunia luar. Namun kursi rodanya akhirnya menjadi kendaraan yang membawanya terbang melompat melampaui segala ketakutannya."
    josee_bio_desc = "Josee mengajariku arti saling menyembuhkan dan bangkit dari keterpurukan paling gelap.\\n\\nKetika Tsuneo terluka parah dan kehilangan harapan untuk bisa menyelam lagi, Josee-lah yang menulis buku dongeng 'Putri Duyung dan Sayap Laut' untuk memberi Tsuneo alasan baru untuk berdiri.\\n\\nMereka saling melengkapi: bukan sebagai beban, melainkan sebagai sayap yang memungkinkan satu sama lain terbang tinggi melompati ketakutan terbesarnya."
    josee_tribute_desc = "Memorial kursi roda vintage Josee berdampingan dengan standing easel kanvas cat air tempat Josee melukiskan mimpinya tentang laut dan ikan terbang.\\n\\nSimbol bahwa keterbatasan fisik tidak akan pernah bisa memenjarakan jiwa manusia yang berani bermimpi dan terbang bebas."
    
    out.extend(build_room(
        "Room_Josee", "Josee", 13.5, -42.0, False, "Mesh_RoomFloor_Josee",
        "Color(0.8, 0.95, 1.0, 1)",
        "Mesh_Canvas_Poster_Josee", "Poster Resmi: Josee, the Tiger and the Fish", josee_poster_desc,
        "Mesh_Canvas_Photo_Josee_1", "Josee & Hamparan Samudra Luas", josee_photo1_desc,
        "Mesh_Canvas_Photo_Josee_2", "Josee di Kursi Rodanya", josee_photo2_desc,
        "Memorial Kursi Roda & Kanvas Laut Josee", josee_tribute_desc,
        "Kenangan Josee: Keberanian Menggapai Samudra", josee_bio_desc
    ))
    
    # Room 4 Centerpiece 3D Model: Josee's Wheelchair & Art Easel
    out.append('[node name="Tribute_Josee" type="StaticBody3D" parent="Room_Josee"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 13.5, 0, -42)')
    out.append('script = ExtResource("2_interactable")')
    out.append('prompt_text = "Amati Kursi Roda & Lukisan Josee"')
    out.append('exhibit_title = "Memorial Kursi Roda Kebebasan & Kanvas Laut Josee"')
    out.append(f'exhibit_description = "{josee_tribute_desc}"')
    # Deep Blue Pedestal Base
    out.append('[node name="BasePedestal" type="MeshInstance3D" parent="Room_Josee/Tribute_Josee"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.2, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Josee_Base"]')
    out.append('material = SubResource("Mat_Pedestal")')
    out.append('size = Vector3(2.4, 0.4, 2.4)')
    out.append('mesh = SubResource("Mesh_Josee_Base")')
    # Wheelchair Seat Cushion
    out.append('[node name="WheelchairSeat" type="MeshInstance3D" parent="Room_Josee/Tribute_Josee"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -0.4, 0.85, 0)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Wheelchair_Seat"]')
    out.append('material = SubResource("Mat_JoseeRed")')
    out.append('size = Vector3(0.65, 0.1, 0.65)')
    out.append('mesh = SubResource("Mesh_Wheelchair_Seat")')
    # Wheelchair Backrest
    out.append('[node name="WheelchairBack" type="MeshInstance3D" parent="Room_Josee/Tribute_Josee"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, -0.4, 1.25, 0.3)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Wheelchair_Back"]')
    out.append('material = SubResource("Mat_JoseeRed")')
    out.append('size = Vector3(0.65, 0.7, 0.08)')
    out.append('mesh = SubResource("Mesh_Wheelchair_Back")')
    # Left Wheel (Torus)
    out.append('[node name="WheelLeft" type="MeshInstance3D" parent="Room_Josee/Tribute_Josee"]')
    out.append('transform = Transform3D(0, 0, 1, 1, 0, 0, 0, 1, 0, -0.76, 0.82, 0)')
    out.append('[sub_resource type="TorusMesh" id="Mesh_Wheel"]')
    out.append('material = SubResource("Mat_ChromeMetal")')
    out.append('inner_radius = 0.35')
    out.append('outer_radius = 0.45')
    out.append('mesh = SubResource("Mesh_Wheel")')
    # Right Wheel (Torus)
    out.append('[node name="WheelRight" type="MeshInstance3D" parent="Room_Josee/Tribute_Josee"]')
    out.append('transform = Transform3D(0, 0, 1, 1, 0, 0, 0, 1, 0, -0.04, 0.82, 0)')
    out.append('mesh = SubResource("Mesh_Wheel")')
    # Painting Easel next to wheelchair
    out.append('[node name="EaselLegs" type="MeshInstance3D" parent="Room_Josee/Tribute_Josee"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0.6, 1.15, 0)')
    out.append('[sub_resource type="PrismMesh" id="Mesh_Easel_Legs"]')
    out.append('material = SubResource("Mat_WoodBench")')
    out.append('size = Vector3(0.7, 1.5, 0.4)')
    out.append('mesh = SubResource("Mesh_Easel_Legs")')
    # Ocean Art Canvas on Easel
    out.append('[node name="EaselCanvas" type="MeshInstance3D" parent="Room_Josee/Tribute_Josee"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 0.965926, 0.258819, 0, -0.258819, 0.965926, 0.6, 1.25, 0.15)')
    out.append('[sub_resource type="BoxMesh" id="Mesh_Easel_Canvas"]')
    out.append('material = SubResource("Mat_OceanBlue")')
    out.append('size = Vector3(0.65, 0.5, 0.05)')
    out.append('mesh = SubResource("Mesh_Easel_Canvas")')
    # Collision
    out.append('[node name="Collision" type="CollisionShape3D" parent="Room_Josee/Tribute_Josee"]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.95, 0)')
    out.append('[sub_resource type="BoxShape3D" id="Shape_Tribute_Josee"]')
    out.append('size = Vector3(2.4, 1.8, 2.4)')
    out.append('shape = SubResource("Shape_Tribute_Josee")')
    out.append('')

    # ----------------------------------------------------
    # PLAYER SPAWN (Lobby entrance at Z = 10 facing north)
    # ----------------------------------------------------
    out.append('[node name="Player" parent="." instance=ExtResource("1_player")]')
    out.append('transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.1, 9.0)')
    out.append('')

    import re
    blocks = re.split(r'\n(?=\[)', '\n'.join(out))
    header = blocks[0]
    ext_res = [b.strip() for b in blocks[1:] if b.startswith('[ext_resource')]
    sub_res = [b.strip() for b in blocks[1:] if b.startswith('[sub_resource')]
    nodes = [b.strip() for b in blocks[1:] if b.startswith('[node')]

    total_steps = len(ext_res) + len(sub_res) + 1
    header = re.sub(r'load_steps=\d+', f'load_steps={total_steps}', header)

    new_text = header.strip() + '\n\n'
    new_text += '\n\n'.join(ext_res) + '\n\n'
    new_text += '\n\n'.join(sub_res) + '\n\n'
    new_text += '\n\n'.join(nodes) + '\n'

    target_path = 'scenes/main.tscn'
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print(f"Successfully generated {target_path} ({len(new_text)} bytes, {len(nodes)} nodes, load_steps={total_steps})")

if __name__ == '__main__':
    generate_main_scene()
