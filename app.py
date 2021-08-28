import os
import json
from functools import partial


from pythonosc.udp_client import SimpleUDPClient
import keyboard
from atem_board.board import Board


SETTINGS_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "settings.json"
)
KEYMAP_PATH = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "keymap.json")


def get_settings() -> dict:
    with open(SETTINGS_PATH, "r") as f:
        return json.load(f)


def get_keymap() -> dict:
    with open(KEYMAP_PATH, "r") as f:
        return json.load(f)


def get_client(ip: str, port: int):
    return SimpleUDPClient(ip, port)


def main() -> None:
    settings = get_settings()
    key_map = get_keymap()
    board = Board(settings["server_ip"], int(settings["server_port"]))
    print("[INFO] Binding ...")
    for key, msg in key_map.items():
        callback = partial(board._send_message, message=msg)
        keyboard.hook_key(key, callback, suppress=True)
    # keyboard.add_hotkey('p', lambda: print('space was pressed!'))
    print("[INFO] Running ...")
    keyboard.wait("0")
    keyboard.unhook_all()
    print("[INFO] Stopped")


if __name__ == "__main__":
    main()
