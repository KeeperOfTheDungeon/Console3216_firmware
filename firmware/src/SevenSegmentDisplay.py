
from Ht16k33 import *

# TODO In C++ Quellcode eine Konstante:
# static const uint8_t numbertable[] = { ... }
numbertable = [
    0x3F,  # 0
    0x06,  # 1
    0x5B,  # 2
    0x4F,  # 3
    0x66,  # 4
    0x6D,  # 5
    0x7D,  # 6
    0x07,  # 7
    0x7F,  # 8
    0x6F,  # 9
    0x77,  # a
    0x7C,  # b
    0x39,  # C
    0x5E,  # d
    0x79,  # E
    0x71,  # F
]

# TODO C++ Klassendeklaration:
# class SevenSegmentDisplay	: public Ht16k33 { ... };
class SevenSegmentDisplay(Ht16k33):
    def setNumberAt(self, number: int, position: int):
        pass
    def setSegmentsAt(self, segments: int, position: int):
        pass
    def clearDotAt(self, number: int, position: int):
        pass
    def setDotAt(self, number: int, position: int):
        pass
    def setColon(self):
        pass
    def clearColon(self):
        pass
    def toggleColon(self):
        pass
    def setNumber(self, value: int):
        pass
