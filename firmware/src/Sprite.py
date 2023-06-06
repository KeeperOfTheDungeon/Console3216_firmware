
from Display import *

# TODO Die Farben werden jetzt mit 3 ints (RGB) angegeben
# Die Liste _bitmap ist in C++ ein Array aus ints, die
# auf jeder Position einen Farbcode beinhalten.
# In Dieser Implementierung wird ein neues Color Objekt
# an jeder Position angelegt
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class Sprite:
    def __init__(self, xPos: int, yPos: int, xExtend: int, yExtend: int) -> None:
        self._xPos: int = xPos
        self._yPos: int = yPos
        self._xExtend: int = xExtend
        self._yExtend: int = yExtend
        # C++ Quellcode:
        # this->bitmap = new uint16_t [yExtend * xExtend];
        self._bitmap = [Color(0, 0, 0)] * (xExtend * yExtend)
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

    # TODO Farbe wird nicht mehr mit nur einem int angegeben
    def draw(self):
        if self._active:
            i = 0

            for x in range(self._xPos, self._xExtend + self._xPos):
                for y in range(self._yPos, self._yExtend + self._yPos):
                    Display.drawPixel(x, y, self._bitmap[i].r, self._bitmap[i].g, self._bitmap[i].b)
                    i += 1
        pass

    def mirrorY(self):
        pass
