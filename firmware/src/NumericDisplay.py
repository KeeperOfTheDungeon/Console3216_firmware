
from SevenSegmentDisplay import *

DISPLAY_LEFT = 0
DISPLAY_MIDDLE = 1
DISPLAY_RIGHT = 2

class NumericDisplay:
    _leftDisplay: SevenSegmentDisplay
    _middleDisplay: SevenSegmentDisplay
    _rightDisplay: SevenSegmentDisplay

    def __init__(self) -> None:
        # TODO C++ Quellcode:
        # Wire.setClock(400000L);
        # Aus Arduino Wire.h

        self._leftDisplay.init(0x70)
        self._leftDisplay.init(0x71)
        self._leftDisplay.init(0x72)

    @classmethod
    def test(cls):
        cls._leftDisplay.init(0x72)
        cls._middleDisplay.init(0x71)
        cls._rightDisplay.init(0x70)

        cls._leftDisplay.setNumber(190)
        cls._middleDisplay.setNumber(191)
        cls._rightDisplay.setNumber(192)

    @classmethod
    def displayTime(cls, display: int, seconds: int):
        minutes: int
        # TODO In C++ ein Pointer:
        # SevenSegmentDisplay * actualDisplay;
        actualDisplay: SevenSegmentDisplay

        minutes = seconds / 60
        seconds = seconds % 60

        if display == DISPLAY_LEFT:
            # TODO in C++ wird Speicheradresse übergeben:
            # actualDisplay = & NumericDisplay::leftDisplay;
            actualDisplay = cls._leftDisplay
        elif display == DISPLAY_MIDDLE:
            # TODO in C++ wird Speicheradresse übergeben:
            # actualDisplay = & NumericDisplay::middleDisplay;
            actualDisplay = cls._middleDisplay
        elif display == DISPLAY_RIGHT:
            # TODO in C++ wird Speicheradresse übergeben:
            # actualDisplay = & NumericDisplay::rightDisplay;
            actualDisplay = cls._rightDisplay
        else:
            return
        
        actualDisplay.setNumber(minutes * 100 + seconds)

        if seconds & 1:
            actualDisplay.setColon()
        else:
            actualDisplay.clearColon()

    @classmethod
    def displayValue(cls, display: int, value: int):
        # TODO In C++ ein Pointer:
        # SevenSegmentDisplay * actualDisplay;
        actualDisplay: SevenSegmentDisplay

        if display == DISPLAY_LEFT:
            # TODO in C++ wird Speicheradresse übergeben:
            # actualDisplay = & NumericDisplay::leftDisplay;
            actualDisplay = cls._leftDisplay
        elif display == DISPLAY_MIDDLE:
            # TODO in C++ wird Speicheradresse übergeben:
            # actualDisplay = & NumericDisplay::middleDisplay;
            actualDisplay = cls._middleDisplay
        elif display == DISPLAY_RIGHT:
            # TODO in C++ wird Speicheradresse übergeben:
            # actualDisplay = & NumericDisplay::rightDisplay;
            actualDisplay = cls._rightDisplay
        else:
            return
        
        actualDisplay.setNumber(value)
