import os
import json
from typing import Union
from functools import partial

from pythonosc.udp_client import SimpleUDPClient
import keyboard
from atem_board.board import Board


SETTINGS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        "settings.json")

def get_settings() -> dict:
    with open(SETTINGS_PATH, "r") as f:
        return json.load(f)

def get_client(ip: str, port: int):
    return SimpleUDPClient(ip, port)

def main() -> None:
    settings = get_settings()
    board = Board(settings["server_ip"], int(settings["server_port"]))
    send_5 = partial(board._send_message, message="/atem/program/5")
    send_6 = partial(board._send_message, message="/atem/program/6")
    keyboard.hook_key("5", send_5)
    keyboard.hook_key("6", send_6)


    keyboard.wait("0")
if __name__ == "__main__":
    main()