#!/bin/bash

# Pick a color in HEX
picked_hex=$(hyprpicker -f hex)

# Convert HEX to RGB
r=$(printf "%d" 0x${picked_hex:1:2})
g=$(printf "%d" 0x${picked_hex:3:2})
b=$(printf "%d" 0x${picked_hex:5:2})

# Copy both formats to clipboard
echo "$picked_hex rgb($r,$g,$b)" | wl-copy
