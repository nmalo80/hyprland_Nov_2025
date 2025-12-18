#!/usr/bin/env python3

import sys
import subprocess
import json
from pathlib import Path
import configparser
import shutil
import os


def find_desktop(app_id):
    paths = [Path.home() / ".local/share/applications", Path("/usr/share/applications")]

    for base in paths:
        if not base.exists():
            continue
        for f in base.glob("*.desktop"):
            if app_id in f.name:
                return f
    return None


def get_icon_from_desktop(desktop_file):
    cfg = configparser.ConfigParser(interpolation=None)
    cfg.read(desktop_file)
    return cfg["Desktop Entry"].get("Icon")


def find_icon_file(icon_name):
    icon_dirs = [
        Path.home() / ".local/share/icons",
        Path("/usr/share/icons"),
        Path("/usr/share/pixmaps"),
    ]

    for base in icon_dirs:
        if not base.exists():
            continue
        for ext in ("png", "svg"):
            matches = list(base.rglob(f"{icon_name}.{ext}"))
            if matches:
                return matches[0]
    return None


# find current app ID
win = subprocess.check_output(["hyprctl", "activewindow", "-j"], text=True)
data = json.loads(win)
app_id = data["class"]

# find desktop app associated to app_id
desktop = find_desktop(app_id)

icon_name = get_icon_from_desktop(desktop)

icon_path = find_icon_file(icon_name)

# Fixed path in RAM for Waybar
dest_path = "/dev/shm/waybar_dynamic.png"

# Only copy if it differs to avoid unnecessary writes
if not os.path.exists(dest_path) or not os.path.samefile(icon_path, dest_path):
    shutil.copyfile(icon_path, dest_path)
