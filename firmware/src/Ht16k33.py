
HT16K33_DISPLAY_SIZE = 16

class Ht16k33:
    def __init__(self) -> None:
        self._i2CAddres: int
        self._dataBuffer: int = [] * HT16K33_DISPLAY_SIZE
    
    def init(self, i2CAddress: int):
        pass
    def writeDisplay(self):
        pass
    def setBrightness(self, brightness: int):
        pass
    def refresh(self):
        pass
