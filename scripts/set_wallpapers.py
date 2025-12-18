#!/usr/bin/env python3

import os
import random
import subprocess
from pathlib import Path
import time

time.sleep(1)

landscape_wallpapers_folder = Path("/home/fed/Pictures/wallpapers/landscape")
portrait_wallpapers_folder = Path("/home/fed/Pictures/wallpapers/landscape/")

landscape_images = [
    f
    for f in landscape_wallpapers_folder.glob("*")
    if f.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
]
random_landscape_img = random.choice(landscape_images)
portrait_images = [
    f
    for f in portrait_wallpapers_folder.glob("*")
    if f.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
]
random_portrait_img = random.choice(portrait_images)

print(random_portrait_img)
subprocess.run(f'swww img -o DP-2 "{random_portrait_img}"', shell=True)
subprocess.run(f'swww img -o DP-1 "{random_landscape_img}"', shell=True)
