# TODO C++ includes:
# Adafruit_GFX.h
# gfxfront.h
# RGBMatrixPanel.h

import Microcontroller

from ctypes import c_int16, c_uint16, c_ubyte, c_char

DISPLAY_X_EXTEND = 32
DISPLAY_Y_EXTEND = 16

CLK = 11

# TODO
# C++: #define LAT A3
LAT = A3

OE = 9

# TODO
# C++:  #define A A0
#       #define B A1
#       #define C A2
A = A0
B = A1
C = A2

DISPLAY_X: c_int16 = 32
DISPLAY_Y: c_int16 = 16
DISPLAY_SCALE_FACTOR: c_int16 = 64

# TODO Auskommentierte Zeilen
# C++:  const int16_t CALCULATION_SIZE = 512

#       #define WHITE   0xFFFF
#       #define BLACK   0x0000
#       #define CYAN    0x07FF

# CALCULATION_SIZE: c_int16 = 512

# WHITE = 0xFFFF
# BLACK = 0x0000
# CYAN  = 0x07FF#

# TODO Macros
# C++:  #define GREEN this->matrix->Color333(0, 7, 0)
#       #define BLUE  this->matrix->Color333(0, 0, 7)
#       #define RED   this->matrix->Color333(7, 0, 0)
#       #define CLEAR this->matrix->Color333(0, 0, 0)

class Display:
    # TODO Pointer
    # C++: static RGBmatrixPanel* matrix;
    matrix: RGBMatrixPanel
    
    def __rescaleToLocal(coordinate: c_int16):
        pass # TODO

    def __init__(self) -> None:
        self.__prevBallX: c_int16
        self.__prevBallY: c_int16
        self.__prevP1: c_int16
        self.__prevP2: c_int16

        # TODO Auskommentierte Zeile
        # C++: RGBmatrix RGBmtr;
        # self.__RGBmtr: RGBMatrix

    def init(self):
        pass # TODO

    @classmethod
    def refresh(self):
        pass # TODO

    @classmethod
    def drawPixel(self, x: c_ubyte, y: c_ubyte, color: c_uint16):
        pass # TODO

    # TODO Auskommentierte Zeile
    # C++: static void drawRect(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color);
    # @classmethod
    # def drawRect(self, x: c_int16, y: c_int16, w: c_int16, h: c_int16, color: c_uint16)

    @classmethod
    def clearDisplay(self):
        pass # TODO

    @classmethod
    def drawText(self, text: c_char, x: c_int16, y: c_int16, color: c_int16, scaleFactor: c_int16):
        pass # TODO

    @classmethod
    def getColor(self, red: c_ubyte, green: c_ubyte, blue: c_ubyte) -> c_uint16:
        pass # TODO

    @classmethod
    def drawBitmap(self, x: c_int16, y: c_int16, bitmap: c_ubyte, width: c_int16, height: c_int16, color: c_int16):
        pass # TODO