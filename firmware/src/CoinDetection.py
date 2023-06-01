
# TODO Wahrscheinlich nicht nötig, wegen dem Matrix Bonnet
# import RPi.GPIO as GPIO

# TODO Arduino.h wurde in C++ importiert
# Eventuell wurde dort attachInterrupt() definiert, 
# welches in init() verwendet wird.

# TODO
#import RgbLed
from RgbLed import *
from Display import *

COIN_PIN = 19
GAME_COST = 1


class CoinDetection:
    _balance: int
    _rgbLed: RgbLed

    @classmethod
    def __setLed(cls):
        if cls._balance >= GAME_COST:
            cls._rgbLed.setLEDColorRGB(0, 3, 0)
        else:
            cls._rgbLed.setLEDColorRGB(3, 0, 0)

    @classmethod
    def __detectFallingEdge(cls):
        cls._balance += 1
        cls.__setLed()

    @classmethod
    def init(cls):
        # TODO Python Variante des C++ Codes, um die Pins zu aktivieren
        # Wahrscheinlich nicht mehr benötigt
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(COIN_PIN, GPIO.IN, GPIO.PUD_UP)
        # TODO Aus C++ Quellcode, wahrscheinlich nicht mehr benötigt
        # attachInterrupt(digitalPinToInterrupt(COIN_PIN, self._detectFallingEdge(), FALLING))
        cls._balance = 0

    @classmethod
    def startGame(cls):
        if cls._balance >= GAME_COST:
            cls._balance -= GAME_COST
            cls.__setLed()
            return True
        return False
