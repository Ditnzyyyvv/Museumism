# 🏛️ Museumism: Museum Karakter Fiksi Hidupku
### 3D First-Person Exploration & Memorial Gallery (Godot Engine 4)

Game eksplorasi first-person bertemakan **Museum Memorial Karakter Fiksi** yang dibuat untuk mengenang karakter-karakter fiksi berharga yang telah hadir, menemani, dan memberikan inspirasi mendalam dalam perjalanan hidup.

---

## 🌟 Konsep & Struktur Museum

Museum ini dirancang dengan tata letak **Lorong Panjang (Grand Hallway)** yang megah dengan karpet merah beraksen emas. Di sepanjang lorong, terdapat 4 sayap ruangan (*1 Topik 1 Ruang*) dengan pintu portal tematik khusus:

### 🚀 Pintu 1 (Section 01): WALL-E (2008) — Deep Space & Cosmic Love
* **Tema Tembok Luar Pintu**: Dinding kosmik luar angkasa bernuansa nebula ungu-sian, taburan bintang berkilau, dan portal bercahaya neon biru futuristik.
* **Isi Ruangan**:
  * **Centerpiece 3D**: Patung penghormatan robot WALL-E berbadan kuning dengan mata binokular, roda tank tread, dan sepatu boot bekas berisi tunas hijau yang hidup.
  * **Poster Resmi**: Poster film *WALL·E (2008)* karya Pixar Animation Studios & Andrew Stanton.
  * **Galeri Foto**: Foto WALL-E merawat koleksi nostalgianya dan momen berpegangan tangan bersama EVE.
  * **Plakat Refleksi**: Pelajaran tentang kesetiaan, kehangatan di tengah kesendirian, dan cinta tanpa kata.

### 🌸 Pintu 2 (Section 02): A Silent Voice (2016) — Jembatan Sakura & Suara Hati
* **Tema Tembok Luar Pintu**: Dinding bernuansa lukisan cat air kelopak sakura berguguran di atas riak air jernih Sungai Suimon, dengan motif tanda silang 'X' yang perlahan lepas.
* **Isi Ruangan**:
  * **Centerpiece 3D**: Kolam zen berbatu dengan jembatan lengkung kayu merah, taburan kelopak sakura, dan Buku Catatan Komunikasi Shoko Nishimiya yang berpendar lembut.
  * **Poster Resmi**: Poster film anime *A Silent Voice (聲の形)* karya Kyoto Animation & Naoko Yamada.
  * **Galeri Foto**: Buku catatan pertama Shoko dan senyuman tulus Shoko di jembatan taman.
  * **Plakat Refleksi**: Pelajaran tentang keberanian membuka telinga untuk mendengar suara hati orang lain, melepaskan rasa bersalah, dan saling memaafkan.

### 🍃 Pintu 3 (Section 03): Kimi ni Todoke — Semilir Angin Musim Semi & Ketulusan
* **Tema Tembok Luar Pintu**: Dinding cerah bernuansa musim semi sekolah, bunga sakura mekar di bawah sinar mentari pagi, dan semilir angin lembut.
* **Isi Ruangan**:
  * **Centerpiece 3D**: Bangku dan meja kelas sekolah Sawako Kuronuma dan Shota Kazehaya, buku catatan, burung bangau kertas (origami), dan ranting sakura.
  * **Poster Resmi**: Poster anime *Kimi ni Todoke (君に届け)* karya Production I.G & Karuho Shiina.
  * **Galeri Foto**: Senyuman tulus Sawako yang menyinari rumor kelam dan momen pertama di bawah pohon sakura bersama Kazehaya.
  * **Plakat Refleksi**: Pelajaran tentang kekuatan kebaikan tanpa pamrih, bahwa ketulusan hati pada akhirnya akan selalu sampai ke hati orang lain.

### 🌊 Pintu 4 (Section 04): Josee, the Tiger and the Fish (2020) — Samudra Kebebasan & Sayap Impian
* **Tema Tembok Luar Pintu**: Dinding gradasi biru laut dalam, sinar matahari yang membelah permukaan air, dan siluet ikan-ikan tropis yang berenang bebas.
* **Isi Ruangan**:
  * **Centerpiece 3D**: Kursi roda klasik Josee (Kumiko) bersanding dengan standing easel kanvas cat air lukisan laut dan ikan terbang.
  * **Poster Resmi**: Poster film anime *Josee, the Tiger and the Fish (ジョゼと虎と魚たち)* karya Studio Bones & Kotaro Tamura.
  * **Galeri Foto**: Josee saat pertama kali menyentuh deburan ombak laut dan keteguhan hatinya di kursi roda.
  * **Plakat Refleksi**: Pelajaran tentang saling menyembuhkan, bahwa keterbatasan fisik tidak akan pernah bisa memenjarakan jiwa yang berani bermimpi dan terbang bebas.

### 🕊️ Sanctuary of Stories (Ujung Lorong)
Di ujung lorong panjang terdapat ruang renungan akhir dengan plakat epilog: refleksi mendalam mengenai bagaimana karakter-karakter fiksi ini tetap hidup dan memberi kekuatan di dunia nyata.

---

## 🕹️ Kontrol Permainan

| Tombol / Input | Aksi | Keterangan |
| :--- | :--- | :--- |
| **W, A, S, D** | **Bergerak** | Berjalan santai menelusuri lorong dan sayap ruangan museum |
| **Shift** (Tahan) | **Berlari (Sprint)** | Melangkah lebih cepat disertai efek *Dynamic FOV* |
| **E** | **Interaksi** | Membaca plakat, poster, foto kenangan, atau monumen 3D |
| **Spasi (Space)** | **Melompat** | Lompat saat menjelajahi ruangan |
| **Gerakan Mouse** | **Melihat Sekeliling** | Rotasi kamera First-Person (Pitch & Yaw) |
| **Escape (Esc)** | **Tutup Info / Kursor** | Menutup kartu penjelasan karya atau membuka kunci kursor mouse |
| **Klik Kiri Mouse** | **Kunci Kursor** | Mengunci kursor mouse kembali saat jendela game aktif |

---

## 📁 Struktur File Proyek

```text
Museumism/
├── project.godot           # Konfigurasi proyek Godot 4 & Input Map
├── icon.svg                # Ikon aplikasi
├── .gitignore              # Git ignore standar Godot (.godot/, dll.)
├── README.md               # Dokumentasi proyek
├── assets/
│   ├── posters/            # Poster resmi film (Wall-E, Silent Voice, Kimi ni Todoke, Josee)
│   ├── photos/             # Foto & cuplikan kenangan karakter
│   └── themes/             # Tekstur artistik dinding gerbang portal (Space, Sakura, Spring, Ocean)
├── scenes/
│   ├── player.tscn         # Pemain FPS (Kamera, Raycast, Dot Reticle, InfoCard Glassmorphism)
│   └── main.tscn           # Lorong panjang, 4 sayap ruangan tematik, pencahayaan & pameran 3D
└── scripts/
    ├── player.gd           # Logika gerak pemain, headbob, fov, dan kartu info
    ├── dot_reticle.gd      # Titik bidik minimalis dinamis di tengah layar
    ├── interactable.gd     # Komponen objek pameran yang dapat diinteraksi dengan [E]
    ├── setup_assets.py     # Script penyiapan & pengunduhan aset grafis
    └── build_museum_scene.py # Script generator arsitektur museum 3D
```

---

## 🚀 Cara Menjalankan

1. Buka aplikasi **Godot Engine 4** (4.0 s/d 4.6+).
2. Di jendela **Project Manager**, klik tombol **Import**.
3. Pilih file [`project.godot`](file:///c:/Users/Lenovo/Documents/.Project/Ditnzy-Game/Museumism/project.godot).
4. Klik **Import & Edit**.
5. Tekan tombol **F5** (atau klik ikon **Play** di kanan atas) untuk langsung menjelajahi museum!
