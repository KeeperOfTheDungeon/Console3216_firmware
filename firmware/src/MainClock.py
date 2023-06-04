
TIME_BASIS_MS = 20

MAIN_TIMER_PERIOD = 1250

class MainClockStatus_t:
    def __init__(self) -> None:
        # TODO Beide Variablen im C++ Struct auf nur ein Bit begrenzt
        # C++:
        # typedef struct{
        # 	uint8_t systemTick:1;
        # 	uint8_t systemTickOverflow:1;
        # }MainClockStatus_t;
        self.systemTick: int
        self.systemTickOverflow: int


class MainClock:
    __systemTime: int

    def __init__(self) -> None:
        self.__status: MainClockStatus_t
    
    def startTimer(self):
        # TODO C++ Quellcode:
        # cli();
        # Aus "Arduino.h", "avr/interrupt.h" oder "avr/io.h"

        mainClock = self

        # TODO C++ Quellcode:
        # TCCR3A =   (1<<WGM31) | (0<<WGM30);
        # TCCR3B = (1<<CS32) | (0<<CS31) | (0<<CS30)| ( 1<<WGM33 ) | (1<<WGM32 );
        
        # TCNT3H = 0;
        # TCNT3L = 0;

        # ICR3 = MAIN_TIMER_PERIOD;

        # TIMSK3 |= (1 << TOIE3);

        # OCR3AH=0;
        # OCR3AL=0;

        # OCR3BH=0;
        # OCR3BL=0;

        # sei();
        # Aus "Arduino.h", "avr/interrupt.h" oder "avr/io.h"

        MainClock.__systemTime = 0
        pass

    def setTick(self):
        pass
    def isTick(self) -> bool:
        pass
    def hasOverflow(self) -> bool:
        pass
    def clearOverflow(self):
        pass

    @classmethod
    def getSystemTime(cls) -> int:
        pass

# TODO Im C++ Quellcode ein pointer:
# MainClock * mainClock;
mainClock: MainClock