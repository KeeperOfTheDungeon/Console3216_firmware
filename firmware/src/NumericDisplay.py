
from SevenSegmentDisplay import *

DISPLAY_LEFT = 0
DISPLAY_MIDDLE = 1
DISPLAY_RIGHT = 2

class NumericDisplay:
    _leftDisplay: SevenSegmentDisplay
    _middleDisplay: SevenSegmentDisplay
    _rightDisplay: SevenSegmentDisplay

    def __init__(self) -> None:
        pass

    @classmethod
    def test(cls):
        pass

    @classmethod
    def displayTime(cls, display: int, seconds: int):
        pass
    @classmethod
    def displayValue(cls, display: int, value: int):
        pass
