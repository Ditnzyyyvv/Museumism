# 🏛️ Museum Art & Artifact - Godot Engine 4 (3D First-Person Exploration)

Template game 3D First-Person dengan tema **Museum Seni & Artifak** menggunakan **Godot Engine 4**. Didesain khusus untuk genre eksplorasi santai (*walking simulator / interactive exhibition*) dengan tampilan layar yang bersih dan imersif.

---

## 🕹️ Kontrol Permainan

| Tombol / Input | Aksi | Keterangan |
| :--- | :--- | :--- |
| **W, A, S, D** | **Bergerak** | Berjalan santai menelusuri lorong museum |
| **Shift** (Tahan) | **Berlari (Sprint)** | Melangkah lebih cepat dengan efek dinamis |
| **E** | **Interaksi** | Membaca plakat & kartu deskripsi karya seni |
| **Spasi (Space)** | **Melompat** | Lompat saat menjelajahi ruangan |
| **Gerakan Mouse** | **Melihat Sekeliling** | Rotasi kamera First-Person (Pitch & Yaw) |
| **Escape (Esc)** | **Tutup Info / Kursor** | Menutup kartu karya seni atau membuka kunci kursor mouse |
| **Klik Kiri Mouse** | **Kunci Kursor** | Mengunci mouse kembali saat jendela game aktif |

---

## ✨ Fitur & Perubahan Terbaru

1. **Dot Crosshair Minimalis**:
   - Crosshair garis bidik dihapus sepenuhnya dan digantikan oleh **titik kecil (dot reticle)** lembut di tengah layar.
   - Saat Anda mengarahkan pandangan ke karya seni atau plakat, dot akan otomatis membesar lembut dan memunculkan petunjuk interaksi `[E] Amati`.

2. **Tampilan Layar Bersih (Unobstructed View)**:
   - Panel dashboard di pojok kiri atas telah dihilangkan sehingga Anda dapat menikmati visual museum dan mengamati karya seni tanpa gangguan elemen UI.
   - Kartu informasi karya seni hanya muncul saat Anda menekan tombol **E** di depan objek pameran, dan dapat ditutup kembali dengan **E** atau **Esc**.

3. **Lingkungan Museum 3D yang Lengkap**:
   - **Lobby Masuk**: Dilengkapi meja penerima tamu dan plakat panduan museum.
   - **Atrium Utama**: Ruang megah dengan karya pameran utama: **Monolit Kristal Abadi** yang berpendar cahaya biru toska.
   - **Wing Barat (Galeri Lukisan)**: Dinding galeri yang memajang lukisan cat minyak berbingkai emas (*Senja Abadi, Samudra Biru, Hutan Zamrud, Geometri Kosmik*) lengkap dengan lampu sorot (*spotlight*).
   - **Wing Timur (Galeri Patung)**: Menampilkan patung logam reflektif di atas pedestal marmer (*Torus Emas Murni, Keseimbangan Kromatik, Piramida Obsidian*).
   - **Sanctuary Utara**: Tempat kehormatan untuk **Fragmen Bintang (Starlight Relic)** yang bersinar keemasan.
   - **Fasilitas Pengunjung**: Bangku kayu santai di berbagai sudut ruangan dan balok arsitektur langit-langit yang elegan.

4. **Sistem Pergerakan Terintegrasi**:
   - Kontrol WASD halus dengan akselerasi alami.
   - Sprinting dengan tombol Shift disertai *Dynamic FOV* lembut.
   - Goyangan kamera langkah kaki (*Head Bobbing*) realistis.

---

## 📁 Struktur File Proyek

```text
Kimi ni Todoke/
├── project.godot           # Konfigurasi proyek & Input Map (WASD, Shift, E, Space, Esc)
├── icon.svg                # Ikon proyek
├── .gitignore              # Mengabaikan file cache .godot/
├── README.md               # Dokumentasi panduan
├── scenes/
│   ├── player.tscn         # Karakter pemain (Kamera, RayCast interaksi, Dot Reticle, Info Card)
│   └── main.tscn           # Arsitektur interior museum, pencahayaan, & karya seni
└── scripts/
    ├── player.gd           # Skrip pengontrol karakter & logika interaksi E
    ├── dot_reticle.gd      # Skrip titik reticle dinamis di tengah layar
    └── interactable.gd     # Komponen objek pameran museum yang bisa diamati
```

---

## 🚀 Cara Membuka & Menjalankan di Godot

1. Buka aplikasi **Godot Engine 4** (4.0 s/d 4.3+).
2. Di jendela **Project Manager**, klik tombol **Import** (Impor).
3. Klik **Browse**, lalu arahkan ke folder:
   `c:\Users\Lenovo\Documents\.Project\Ditnzy - Game\Kimi ni Todoke`
4. Pilih file [`project.godot`](file:///c:/Users/Lenovo/Documents/.Project/Ditnzy%20-%20Game/Kimi%20ni%20Todoke/project.godot) dan klik **Import & Edit**.
5. Tekan tombol **F5** (atau klik ikon **Play** di pojok kanan atas) untuk langsung menjelajahi museum!
