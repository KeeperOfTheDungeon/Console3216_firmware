
TIME_BASIS_MS = 20


class MainClockStatus_t:
    def __init__(self) -> None:
        # TODO Beide Variablen im C++ Struct auf nur ein Bit begrenzt
        # C++:
        # typedef struct{
        # 	uint8_t systemTick:1;
        # 	uint8_t systemTickOverflow:1;
        # }MainClockStatus_t;
        systemTick: int
        systemTickOverflow: int


class MainClock:
    __systemTime: int

    def __init__(self) -> None:
        __status: MainClockStatus_t
    
    def startTimer(self):
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
