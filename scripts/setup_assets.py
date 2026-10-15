import os
import urllib.request
import urllib.parse
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import random

POSTERS = {
    "poster_walle.png": "https://upload.wikimedia.org/wikipedia/en/4/4c/WALL-E_poster.jpg",
    "poster_silent_voice.png": "https://upload.wikimedia.org/wikipedia/en/3/32/A_Silent_Voice_Film_Poster.jpg",
    "poster_kimi_ni_todoke.png": "https://upload.wikimedia.org/wikipedia/en/9/9a/Kimi_ni_Todoke_vol_1.jpg",
    "poster_josee.png": "https://upload.wikimedia.org/wikipedia/en/f/f0/Josee%2C_the_Tiger_and_the_Fish_2020_film_poster.jpg"
}

PHOTOS = {
    "photo_walle_1.png": "https://static.wikia.nocookie.net/pixar/images/0/0f/WALL.E.PNG/revision/latest",
    "photo_walle_2.png": "https://static.wikia.nocookie.net/pixar/images/8/8e/WALL%E2%80%A2E_and_EVE_-_WALL%E2%80%A2E_-_Disney%E2%80%A2Pixar/revision/latest",
    "photo_silent_voice_1.png": "https://static.wikia.nocookie.net/koenokatachi/images/6/66/Ch7_Notebook.png/revision/latest",
    "photo_silent_voice_2.png": "https://static.wikia.nocookie.net/koenokatachi/images/d/d9/Shoko_s-img.png/revision/latest",
    "photo_kimi_ni_todoke_1.png": "https://static.wikia.nocookie.net/kiminitodoke/images/a/a5/Sawako_Kuronuma_profile.png/revision/latest",
    "photo_kimi_ni_todoke_2.png": "https://static.wikia.nocookie.net/kiminitodoke/images/e/ee/Kuronuma_sawako_anime.jpg/revision/latest",
    "photo_josee_1.png": "https://static.wikia.nocookie.net/josee-the-tiger-and-the-fish/images/d/d5/Joseemovie.jpg/revision/latest",
    "photo_josee_2.png": "https://static.wikia.nocookie.net/josee-the-tiger-and-the-fish/images/7/7f/Joseeprofile.jpg/revision/latest"
}

def download_or_fallback(url, target_path, fallback_generator):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    req = urllib.request.Request(url, headers=headers)
    success = False
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(target_path + ".tmp", 'wb') as f:
                f.write(response.read())
        # Validate with PIL
        with Image.open(target_path + ".tmp") as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(target_path, 'PNG')
        if os.path.exists(target_path + ".tmp"):
            os.remove(target_path + ".tmp")
        print(f"Downloaded & verified: {target_path}")
        success = True
    except Exception as e:
        print(f"Failed to download {url}: {e}. Generating fallback artwork.")
        if os.path.exists(target_path + ".tmp"):
            os.remove(target_path + ".tmp")
    
    if not success:
        fallback_img = fallback_generator()
        fallback_img.save(target_path, 'PNG')
        print(f"Generated fallback: {target_path}")

def make_fallback(title, subtitle, base_color, accent_color, width=800, height=1200):
    img = Image.new('RGB', (width, height), base_color)
    draw = ImageDraw.Draw(img)
    # Simple aesthetic border and framing
    margin = 40
    draw.rectangle([margin, margin, width - margin, height - margin], outline=accent_color, width=6)
    draw.rectangle([margin + 15, margin + 15, width - margin - 15, height - margin - 15], outline=accent_color, width=2)
    
    # Gradient / geometric circles
    for r in range(200, 50, -30):
        alpha = int(255 * (1.0 - r / 200.0))
        draw.ellipse([width//2 - r, height//2 - r - 50, width//2 + r, height//2 + r - 50], outline=accent_color, width=2)
        
    draw.text((width//2, height//2 + 180), title, fill=(255, 255, 255), anchor="mm")
    draw.text((width//2, height//2 + 240), subtitle, fill=accent_color, anchor="mm")
    return img

def create_portal_walle(width=1024, height=1024):
    img = Image.new('RGB', (width, height), (7, 9, 22))
    draw = ImageDraw.Draw(img)
    
    # Cosmic Nebula glow
    nebula = Image.new('RGB', (width, height), (0, 0, 0))
    n_draw = ImageDraw.Draw(nebula)
    for _ in range(8):
        cx = random.randint(200, 800)
        cy = random.randint(200, 800)
        cr = random.randint(180, 320)
        color = random.choice([(0, 180, 240), (140, 50, 220), (20, 80, 160)])
        n_draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=color)
    nebula = nebula.filter(ImageFilter.GaussianBlur(100))
    img = Image.blend(img, nebula, 0.45)
    draw = ImageDraw.Draw(img)
    
    # Twinkling Stars
    random.seed(42)
    for _ in range(350):
        sx = random.randint(10, width - 10)
        sy = random.randint(10, height - 10)
        size = random.choice([1, 1, 2, 2, 3, 4])
        b = random.randint(180, 255)
        color = (b, b, min(255, b + random.randint(0, 30)))
        draw.ellipse([sx, sy, sx + size, sy + size], fill=color)
        if size >= 3:
            draw.line([sx - 4, sy + size//2, sx + size + 4, sy + size//2], fill=(255, 255, 255, 120), width=1)
            draw.line([sx + size//2, sy - 4, sx + size//2, sy + size + 4], fill=(255, 255, 255, 120), width=1)
            
    # Futuristic Sci-Fi Frame & Circuitry
    frame_color = (0, 225, 255)
    draw.rectangle([40, 40, width - 40, height - 40], outline=frame_color, width=5)
    draw.rectangle([60, 60, width - 60, height - 60], outline=(0, 140, 180), width=2)
    
    # Circuit lines
    for y in [120, height - 120]:
        draw.line([60, y, 200, y], fill=frame_color, width=3)
        draw.line([200, y, 240, y + 40 if y < 500 else y - 40], fill=frame_color, width=3)
        draw.line([width - 60, y, width - 200, y], fill=frame_color, width=3)
        draw.line([width - 200, y, width - 240, y + 40 if y < 500 else y - 40], fill=frame_color, width=3)

    # Title Banner
    draw.rectangle([180, 90, width - 180, 190], fill=(12, 16, 38), outline=frame_color, width=3)
    draw.text((width//2, 125), "SECTION 01: WALL-E (2008)", fill=(255, 255, 255), anchor="mm")
    draw.text((width//2, 160), "PIXAR • THE SOLITUDE OF EARTH & COSMIC LOVE", fill=frame_color, anchor="mm")
    
    # Bottom Quote
    draw.rectangle([160, height - 170, width - 160, height - 90], fill=(12, 16, 38), outline=(255, 200, 80), width=2)
    draw.text((width//2, height - 142), "\"I don't want to survive, I want to live.\"", fill=(255, 220, 120), anchor="mm")
    draw.text((width//2, height - 114), "WALL-E & EVE • A Plant of Hope in Space", fill=(180, 200, 220), anchor="mm")
    
    return img

def create_portal_silent_voice(width=1024, height=1024):
    img = Image.new('RGB', (width, height), (242, 246, 252))
    draw = ImageDraw.Draw(img)
    
    # Pastel sky to water gradient
    for y in range(height):
        r = int(245 - 35 * (y / height))
        g = int(235 + 15 * (y / height))
        b = int(245 + 10 * (y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b))
        
    # Cherry Blossom petals & Koi ripples
    random.seed(101)
    # Ripple circles
    for _ in range(6):
        cx = random.randint(150, width - 150)
        cy = random.randint(300, height - 200)
        for rad in [40, 80, 120]:
            draw.ellipse([cx - rad, cy - rad//2, cx + rad, cy + rad//2], outline=(160, 205, 230), width=2)
            
    # Sakura Petals
    for _ in range(120):
        px = random.randint(30, width - 30)
        py = random.randint(30, height - 30)
        pw = random.randint(12, 24)
        ph = random.randint(18, 36)
        petal_color = random.choice([(255, 182, 193), (255, 192, 203), (255, 218, 225), (255, 160, 180)])
        draw.ellipse([px, py, px + pw, py + ph], fill=petal_color)
        
    # Symbolic 'X' marks fading away (iconic motif from Shoya's perspective)
    for _ in range(14):
        xx = random.randint(100, width - 100)
        xy = random.randint(220, height - 220)
        x_size = random.randint(15, 25)
        draw.line([xx - x_size, xy - x_size, xx + x_size, xy + x_size], fill=(130, 180, 240, 180), width=4)
        draw.line([xx - x_size, xy + x_size, xx + x_size, xy - x_size], fill=(130, 180, 240, 180), width=4)
        
    # Elegant Wood & Pastel Border
    draw.rectangle([40, 40, width - 40, height - 40], outline=(180, 130, 110), width=6)
    draw.rectangle([60, 60, width - 60, height - 60], outline=(255, 160, 180), width=2)
    
    # Title Banner
    draw.rectangle([140, 90, width - 140, 190], fill=(255, 255, 255), outline=(180, 130, 110), width=3)
    draw.text((width//2, 125), "SECTION 02: A SILENT VOICE (2016)", fill=(60, 60, 75), anchor="mm")
    draw.text((width//2, 160), "KOE NO KATACHI • THE SOUND OF HEART & FORGIVENESS", fill=(220, 100, 135), anchor="mm")
    
    # Bottom Note
    draw.rectangle([140, height - 170, width - 140, height - 90], fill=(255, 255, 255), outline=(140, 185, 220), width=2)
    draw.text((width//2, height - 142), "\"I want to hear your voice... and convey my true feelings.\"", fill=(70, 80, 100), anchor="mm")
    draw.text((width//2, height - 114), "Shoko Nishimiya & Shoya Ishida • Crossing the Bridge", fill=(210, 110, 140), anchor="mm")
    
    return img

def create_portal_kimi_ni_todoke(width=1024, height=1024):
    img = Image.new('RGB', (width, height), (255, 247, 250))
    draw = ImageDraw.Draw(img)
    
    # Warm Spring Morning Gradient
    for y in range(height):
        t = y / height
        r = int(255)
        g = int(240 - 25 * t)
        b = int(245 - 20 * t)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
        
    # Floating Bokeh bubbles
    random.seed(777)
    for _ in range(35):
        bx = random.randint(60, width - 60)
        by = random.randint(60, height - 60)
        br = random.randint(25, 75)
        draw.ellipse([bx - br, by - br, bx + br, by + br], outline=(255, 205, 220), width=3)
        draw.ellipse([bx - br + 5, by - br + 5, bx + br - 5, by + br - 5], fill=(255, 230, 240))
        
    # Cherry Blossom Petals
    for _ in range(160):
        px = random.randint(30, width - 30)
        py = random.randint(30, height - 30)
        pw = random.randint(14, 28)
        ph = random.randint(16, 32)
        color = random.choice([(255, 175, 195), (255, 195, 215), (255, 140, 175), (255, 215, 230)])
        draw.ellipse([px, py, px + pw, py + ph], fill=color)
        
    # Spring Green accents
    draw.rectangle([40, 40, width - 40, height - 40], outline=(230, 120, 150), width=6)
    draw.rectangle([60, 60, width - 60, height - 60], outline=(150, 200, 160), width=2)
    
    # Title Banner
    draw.rectangle([140, 90, width - 140, 190], fill=(255, 255, 255), outline=(230, 120, 150), width=3)
    draw.text((width//2, 125), "SECTION 03: KIMI NI TODOKE", fill=(75, 50, 60), anchor="mm")
    draw.text((width//2, 160), "REACHING YOU • THE PURITY OF YOUTH & FIRST LOVE", fill=(225, 95, 135), anchor="mm")
    
    # Bottom Note
    draw.rectangle([140, height - 170, width - 140, height - 90], fill=(255, 255, 255), outline=(150, 200, 160), width=2)
    draw.text((width//2, height - 142), "\"It was you who taught me what warmth and kindness feel like.\"", fill=(75, 50, 60), anchor="mm")
    draw.text((width//2, height - 114), "Sawako Kuronuma & Shota Kazehaya • Under The Cherry Trees", fill=(225, 95, 135), anchor="mm")
    
    return img

def create_portal_josee(width=1024, height=1024):
    img = Image.new('RGB', (width, height), (8, 28, 54))
    draw = ImageDraw.Draw(img)
    
    # Deep Ocean Gradient
    for y in range(height):
        t = y / height
        r = int(6 + 10 * t)
        g = int(24 + 60 * t)
        b = int(58 + 90 * t)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
        
    # Sun rays cutting through ocean
    random.seed(333)
    for _ in range(7):
        rx = random.randint(100, width - 100)
        draw.polygon([(rx, 0), (rx + 40, 0), (rx + 180, height), (rx + 90, height)], fill=(18, 90, 140))
        
    # Tropical Fish & Bubbles
    for _ in range(80):
        bx = random.randint(40, width - 40)
        by = random.randint(80, height - 80)
        br = random.randint(4, 18)
        draw.ellipse([bx - br, by - br, bx + br, by + br], outline=(100, 210, 240), width=2)
        
    # Fish Silhouettes
    for _ in range(16):
        fx = random.randint(120, width - 120)
        fy = random.randint(220, height - 220)
        fs = random.randint(20, 45)
        # fish body
        draw.ellipse([fx - fs, fy - fs//2, fx + fs, fy + fs//2], fill=(240, 200, 80))
        # tail
        draw.polygon([(fx - fs, fy), (fx - fs - fs//2, fy - fs//3), (fx - fs - fs//2, fy + fs//3)], fill=(240, 200, 80))
        
    # Gold & Coral Nautical Frame
    draw.rectangle([40, 40, width - 40, height - 40], outline=(0, 195, 235), width=6)
    draw.rectangle([60, 60, width - 60, height - 60], outline=(255, 190, 80), width=2)
    
    # Title Banner
    draw.rectangle([110, 90, width - 110, 190], fill=(6, 20, 42), outline=(0, 195, 235), width=3)
    draw.text((width//2, 125), "SECTION 04: JOSEE, THE TIGER AND THE FISH (2020)", fill=(255, 255, 255), anchor="mm")
    draw.text((width//2, 160), "BONES • COURAGE TO BRAVE THE TIGERS & SWIM THE OCEAN", fill=(255, 200, 90), anchor="mm")
    
    # Bottom Note
    draw.rectangle([120, height - 170, width - 120, height - 90], fill=(6, 20, 42), outline=(255, 190, 80), width=2)
    draw.text((width//2, height - 142), "\"Someday, I want to dive into the ocean that I only saw in my dreams.\"", fill=(230, 245, 255), anchor="mm")
    draw.text((width//2, height - 114), "Josee (Kumiko) & Tsuneo Suzukawa • The Wheelchair of Wings", fill=(0, 215, 255), anchor="mm")
    
    return img

def create_lobby_banner(width=1536, height=768):
    img = Image.new('RGB', (width, height), (16, 17, 24))
    draw = ImageDraw.Draw(img)
    
    # Gold border
    draw.rectangle([30, 30, width - 30, height - 30], outline=(212, 175, 55), width=5)
    draw.rectangle([45, 45, width - 45, height - 45], outline=(120, 100, 40), width=2)
    
    # Header
    draw.text((width//2, 120), "MUSEUM KARAKTER FIKSI HIDUPKU", fill=(255, 235, 160), anchor="mm")
    draw.text((width//2, 175), "The Memorial Gallery of Cherished Stories & Lifelong Companions", fill=(190, 190, 205), anchor="mm")
    
    # Separator
    draw.line([width//4, 220, 3*width//4, 220], fill=(212, 175, 55), width=3)
    
    # Explanation
    lines = [
        "Museum ini bukan tentang lukisan purba atau patung abstrak dingin,",
        "melainkan galeri penghormatan untuk karakter-karakter fiksi yang hadir menemani,",
        "mengajarkan ketulusan, keberanian, cinta tanpa syarat, dan harapan di masa-masa hidupku.",
        "",
        "Jelajahi lorong ini dan masuki setiap sayap ruangan tematik:",
        "• Pintu 1 (Kiri): WALL-E — Ruang Angkasa, Kesepian, & Kehangatan Cinta Abadi",
        "• Pintu 2 (Kanan): A SILENT VOICE — Sakura, Ikan Koi, & Pengampunan Diri",
        "• Pintu 3 (Kiri): KIMI NI TODOKE — Angin Musim Semi, Ketulusan, & Cinta Pertama",
        "• Pintu 4 (Kanan): JOSEE, THE TIGER AND THE FISH — Kedalaman Laut, Mimpi, & Kebebasan",
        "",
        "KONTROL: [WASD] Berjalan  |  [Shift] Berlari  |  [Spasi] Lompat  |  [E] Interaksi Plakat & Karya  |  [Esc] Kursor"
    ]
    
    y = 265
    for line in lines:
        color = (255, 220, 120) if "•" in line or "KONTROL" in line else (225, 225, 235)
        draw.text((width//2, y), line, fill=color, anchor="mm")
        y += 38
        
    return img

print("1. Creating Thematic Portal Wallpapers...")
create_portal_walle().save("assets/themes/portal_walle.png")
create_portal_silent_voice().save("assets/themes/portal_silent_voice.png")
create_portal_kimi_ni_todoke().save("assets/themes/portal_kimi_ni_todoke.png")
create_portal_josee().save("assets/themes/portal_josee.png")
create_lobby_banner().save("assets/themes/lobby_banner.png")
print("Themes generated.")

print("2. Downloading Posters...")
fallbacks = {
    "poster_walle.png": lambda: make_fallback("WALL-E", "Disney • Pixar (2008)", (15, 20, 45), (0, 220, 255)),
    "poster_silent_voice.png": lambda: make_fallback("A SILENT VOICE", "Kyoto Animation (2016)", (240, 245, 250), (220, 110, 145)),
    "poster_kimi_ni_todoke.png": lambda: make_fallback("KIMI NI TODOKE", "Production I.G", (255, 245, 248), (240, 120, 160)),
    "poster_josee.png": lambda: make_fallback("JOSEE, THE TIGER AND THE FISH", "Studio Bones (2020)", (10, 30, 60), (0, 210, 255))
}

for name, url in POSTERS.items():
    download_or_fallback(url, os.path.join("assets/posters", name), fallbacks[name])

print("3. Downloading Character Photos...")
photo_fallbacks = {
    "photo_walle_1.png": lambda: make_fallback("WALL-E", "Curiosity & The Little Green Plant", (20, 25, 50), (0, 210, 255), 800, 600),
    "photo_walle_2.png": lambda: make_fallback("WALL-E & EVE", "Directive: Love Across The Stars", (15, 20, 45), (255, 215, 100), 800, 600),
    "photo_silent_voice_1.png": lambda: make_fallback("SHOKO'S NOTEBOOK", "Words Written When Voice Cannot Reach", (245, 245, 250), (220, 110, 140), 800, 600),
    "photo_silent_voice_2.png": lambda: make_fallback("SHOKO NISHIMIYA", "A Gentle Smile by Suimon River Bridge", (245, 240, 245), (140, 185, 230), 800, 600),
    "photo_kimi_ni_todoke_1.png": lambda: make_fallback("SAWAKO KURONUMA", "A Heartfelt Smile That Shines Brighter Than Rumors", (255, 245, 250), (240, 120, 160), 800, 600),
    "photo_kimi_ni_todoke_2.png": lambda: make_fallback("SAWAKO & KAZEHAYA", "Walking Together in Spring", (255, 245, 248), (150, 205, 165), 800, 600),
    "photo_josee_1.png": lambda: make_fallback("JOSEE'S SEA", "Dreaming of the Vast Blue Ocean", (10, 32, 65), (0, 200, 245), 800, 600),
    "photo_josee_2.png": lambda: make_fallback("JOSEE & TSUNEO", "Braving the Tigers, Flying with the Fish", (8, 25, 55), (255, 200, 80), 800, 600),
}

for name, url in PHOTOS.items():
    download_or_fallback(url, os.path.join("assets/photos", name), photo_fallbacks[name])

print("All assets ready!")
