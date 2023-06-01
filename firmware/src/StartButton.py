
from Microcontroller import *

START_BUTTON_IDLE = 0
START_BUTTON_PRESSED = 1
START_BUTTON_HOLD = 2

class StartButton:
    _status: int
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def init():
        pass

    @classmethod
    def isPressed() -> bool:
        pass

    @classmethod
    def getStatus() -> int:
        pass
