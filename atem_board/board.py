import os
import json
from typing import Union, Optional, Any

from pythonosc.udp_client import SimpleUDPClient

class Board(object):
    def __init__(self, ip: str, port: int) -> None:
        self._ip = ip
        self._port = port
        self._client = SimpleUDPClient(self._ip, self._port)

    def _send_message(self, event, message: str, param: Any = None) -> None:
        if event.event_type == "up":
            self._client.send_message(message, param)

