
from Display import *

class Sprite:
    def __init__(self, xPos: int, yPos: int, xExtend: int, yExtend: int) -> None:
        self._xPos: int = xPos
        self._yPos: int = yPos
        self._xExtend: int = xExtend
        self._yExtend: int = yExtend
        # C++ Quellcode:
        # this->bitmap = new uint16_t [yExtend * xExtend];
        self._bitmap = [0] * (xExtend * yExtend)
        self._direction: int
        self._active: bool

    def setPosition(self, newXPos: int, newYPos: int):
        self._xPos = newXPos
        self._yPos = newYPos
        pass

    def move(self, xDelta: int, yDelta: int):
        self._xPos += xDelta
        self._yPos += yDelta
        pass

    def getXPos(self) -> int:
        return self._xPos

    def getYPos(self) -> int:
        return self._yPos

    def isActive(self) -> bool:
        return self._active

    def activate(self):
        self._active = True
        pass

    def deActivate(self):
        self._active = False
        pass

    def draw(self):
        pass

    def mirrorY(self):
        pass
