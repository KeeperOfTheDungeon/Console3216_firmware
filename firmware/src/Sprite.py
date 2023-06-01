
from Display import *

class Sprite:
    def __init__(self, xPos: int, yPos: int, xExtend: int, yExtend: int) -> None:
        self._xPos: int
        self._yPos: int
        self._xExtend: int
        self._yExtend: int
        self._bitmap: int
        self._direction: int
        self._active: bool

    def setPosition(self, newXPos: int, newYPos: int):
        pass
    def move(self, xDelta: int, yDelta: int):
        pass
    def getXPos(self) -> int:
        pass
    def getYPos(self) -> int:
        pass
    def isActive(self) -> bool:
        pass
    def activate(self):
        pass
    def deActivate(self):
        pass
    def draw(self):
        pass
    def mirrorY(self):
        pass