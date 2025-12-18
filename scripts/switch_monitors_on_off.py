#!/usr/bin/env python3
import sys
from pathlib import Path

if len(sys.argv) != 2 or sys.argv[1] not in ("1", "2"):
    print("Usage: ./switch_monitors_on_off.py [1|2]")
    sys.exit(1)

target = int(sys.argv[1])

monitors_conf = Path(__file__).resolve().parent.parent / "monitors.conf"

with open(monitors_conf, "r") as f:
    lines = f.readlines()

line_screen_1 = lines[3].rstrip("\n")
line_screen_2 = lines[4].rstrip("\n")

print(line_screen_1)
print(line_screen_2)

# determine current comment state
c3 = line_screen_1.lstrip().startswith("#")
c4 = line_screen_2.lstrip().startswith("#")

# If user tries to disable last remaining active monitor → block
if target == 2 and not c3 and c4:
    print("❗ Cannot disable monitor 1 — monitor 2 is already disabled!")
    sys.exit(1)

if target == 1 and not c4 and c3:
    print("❗ Cannot disable monitor 2 — monitor 1 is already disabled!")
    sys.exit(1)

# Now toggle normally
line_index = 2 if target == 1 else 3
line = lines[line_index].rstrip("\n")

if line.lstrip().startswith("#"):
    lines[line_index] = line.lstrip()[1:].lstrip() + "\n"
else:
    lines[line_index] = "# " + line + "\n"

with open(monitors_conf, "w") as f:
    f.writelines(lines)
