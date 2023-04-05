from ctypes import c_ubyte

import RPi.GPIO as GPIO
# TODO
import RgbLed

COIN_PIN = 19
GAME_COST = 1

class CoinDetection:
    # TODO
    _balance: c_ubyte
    # TODO
    _rgbLed: RgbLed

    @classmethod
    def __setLed(self):
        if (self._balance >= GAME_COST):
            self._rgbLed.setLEDColor(0,3,0)
        else:
            self._rgbLed.setLEDColor(3,0,0)

    @classmethod
    def __detectFallingEdge(self):
        self._balance += 1
        self._setLed()

    @classmethod
    def init(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(COIN_PIN, GPIO.IN, GPIO.PUD_UP)
        # TODO
        attachInterrupt(digitalPinToInterrupt(COIN_PIN, self._detectFallingEdge(), FALLING))
        self._balance = 0

    @classmethod
    def startGame(self):
        if (self._balance >= GAME_COST):
            self._balance -= GAME_COST
            self._setLed()
            return True
        return False
