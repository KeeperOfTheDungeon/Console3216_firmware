
sinetable = [
    0, 6, 13, 19, 25, 31, 37, 43,
    49, 55, 60, 66, 71, 76, 81, 86,
    91, 95, 99, 103, 106, 110, 113, 116,
    118, 121, 122, 124, 126, 127, 127, 128, 128
]

class Sine:
    def __init__(self) -> None:
        pass

    @classmethod
    def getSineValue(cls, angle: int) -> int:
        angle %= 128

        if angle < 0:
            angle = 128 + angle
        
        if angle < 33:
            return sinetable[angle]
        elif angle < 65:
            return sinetable[64 - angle]
        elif angle < 97:
            return -sinetable[angle - 64]
        elif angle < 128:
            return -sinetable[128 - angle]
        
        return 0

    @classmethod
    def getCosineValue(cls, angle: int) -> int:
        return cls.getSineValue(32 - angle)
