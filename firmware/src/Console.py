# TODO
import Microcontroller
# TODO
import Joystick
# TODO
import StartButton
# TODO
import RgbLed
# TODO
import Display
# TODO
import MainClock
# TODO
import Game

import CoinDetection

from ctypes import c_ubyte, c_byte, c_uint16

CONSOLE_STATE_COIN = 0
CONSOLE_STATE_DEMO = 1
CONSOLE_STATE_GAME = 2

# TODO Globaler Pointer
# C++ Game *game;
game: Game

color: c_ubyte

class Console:
    _joystickLeft: Joystick
    _joystickRight: Joystick

    _rgbLed: RgbLed

    _display: Display

    _mainClock: MainClock

    _state: c_ubyte
    
    # TODO Pointer
    # C++: Game * games[10];
    # Leeres, 10 Elemente großes Array wird angelegt
    _games: Game = [] * 10
    
    _gameCount: c_ubyte
    _gameindex: c_byte
    
    # TODO Pointer
    # C++: Game * actualGame;
    _actualGame: Game

    # TODO auf 12 Bits beschränken
    # C++: uint16_t coinMovementDelay:12;
    _coinMovementDelay: c_uint16

    # TODO auf 4 Bits beschränken
    # C++: uint16_t coinMovementFrame:4;
    _coinMovementFrame: c_uint16

    def init(self):
        self._gameCount = 0
        self._gameindex = 0
        self._state = CONSOLE_STATE_COIN

        # Ursprungscode hatte einen Tippfehler im Namen:
        # C++: JoystickPins_t joyctickPins;
        joystickPins: JoystickPins_t


        joystickPins.left = PIN_JOYSTICK_LEFT_LEFT
        joystickPins.up = PIN_JOYSTICK_LEFT_UP
        joystickPins.right = PIN_JOYSTICK_LEFT_RIGHT
        joystickPins.down = PIN_JOYSTICK_LEFT_DOWN
        joystickPins.buttonTop = PIN_JOYSTICK_LEFT_BUTTON_TOP
        joystickPins.buttonBody = PIN_JOYSTICK_LEFT_BUTTON_BODY

        # TODO Übergabe als Referenz in C++
        # C++: this->joystickLeft.init(&joyctickPins);
        self._joystickLeft.init(joystickPins)

        joystickPins.left = PIN_JOYSTICK_RIGHT_LEFT
        joystickPins.up = PIN_JOYSTICK_RIGHT_UP
        joystickPins.right = PIN_JOYSTICK_RIGHT_RIGHT
        joystickPins.down = PIN_JOYSTICK_RIGHT_DOWN
        joystickPins.buttonTop = PIN_JOYSTICK_RIGHT_BUTTON_TOP
        joystickPins.buttonBody = PIN_JOYSTICK_RIGHT_BUTTON_BODY

        # TODO Übergabe als Referenz in C++
        # C++: this->joystickRight.init(&joyctickPins);
        self._joystickRight.init(joystickPins)

        self._display.init()

        # TODO Herausfinden was das ist
        # C++: randomSeed(analogRead(0));
        StartButton.init()

        self._mainClock.startTimer()

        CoinDetection.init()

    def process(self):
        pass # TODO

    def addGame(self, newGame: Game):
        pass # TODO

    def stateDemo(self):
        pass # TODO

    def displayCoinAnimation(self):
        pass # TODO

    def getJoystick(self, index: c_ubyte) -> Joystick:
        pass # TODO

    @staticmethod
    def checkMem():
        pass # TODO