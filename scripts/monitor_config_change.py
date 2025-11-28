#!/usr/bin/env python3

import subprocess
import json
import os
import re
import sys

hypr_base_dir = "~/.config/hypr/"
monitors_2 = "monitors_2.conf"
monitors_1 = "monitors_1.conf"


def get_monitors():
    result = subprocess.run(
        ["hyprctl", "monitors", "-j"], capture_output=True, text=True
    )
    monitors = json.loads(result.stdout)
    return monitors


def list_monitors():
    monitors = get_monitors()
    print("Connected monitors:")
    for mon in monitors:
        print(
            f"- {mon['name']} : {mon['width']}x{mon['height']} @ {mon['refreshRate']}Hz"
        )


def set_hypr_monitors_conf(new_monitor_conf_file):
    hypr_conf_path = os.path.expanduser(os.path.join(hypr_base_dir, "hyprland.conf"))
    # read hyprland conf file
    with open(hypr_conf_path, "r") as f:
        content = f.read()

    new_monitor_conf_file_path = f"source = {hypr_base_dir}{new_monitor_conf_file}"

    # replace monitor.conf in hyprland.conf
    content = re.sub(
        rf"source = {re.escape(hypr_base_dir)}monitors.*?\.conf",
        new_monitor_conf_file_path,
        content,
    )

    # Write back
    with open(hypr_conf_path, "w") as f:
        f.write(content)


def set_hypr_monitors_and_workspaces_auto():
    monitors = get_monitors()

    if len(monitors) == 1:
        set_hypr_monitors_conf(monitors_1)
        print("hyprland configured for 1 landscape monitor")
    elif len(monitors) == 2:
        set_hypr_monitors_conf(monitors_2)
        print(
            "hyprland configured for a left portrait monitor and a right landscape monitor"
        )


def set_1_monitor():
    set_hypr_monitors_conf(monitors_1)


def set_2_monitors():
    set_hypr_monitors_conf(monitors_2)


if __name__ == "__main__":
    # list_monitors()

    if len(sys.argv) > 1:
        if sys.argv[1] == "1":
            set_1_monitor()
        elif sys.argv[1] == "2":
            set_2_monitors()
        else:
            print("wrong arguments")
    else:
        set_hypr_monitors_and_workspaces_auto()
