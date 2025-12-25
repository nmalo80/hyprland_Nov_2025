#!/usr/bin/env python3

import random
import subprocess
from pathlib import Path
from PIL import Image
import time

time.sleep(1)

# Folder with ultrawide wallpapers
wallpaper_dir = Path("/home/fed/Pictures/wallpapers/wide")

# Pick random image
images = [
    f
    for f in wallpaper_dir.glob("*")
    if f.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
]
img_path = random.choice(images)

# Open image
img = Image.open(img_path)
width, height = img.size

# Split image in half
left_crop = img.crop((0, 0, width // 2, height))
right_crop = img.crop((width // 2, 0, width, height))

# Temp output paths
left_img = "/tmp/wallpaper_left.png"
right_img = "/tmp/wallpaper_right.png"

left_crop.save(left_img)
right_crop.save(right_img)

# Apply wallpapers
subprocess.run(["swww", "img", "-o", "DP-2", right_img])
subprocess.run(["swww", "img", "-o", "DP-2", right_img])
subprocess.run(["swww", "img", "-o", "DP-1", left_img])
