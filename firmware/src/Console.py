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

import random

from ctypes import c_ubyte, c_byte, c_uint16

CONSOLE_STATE_COIN = 0
CONSOLE_STATE_DEMO = 1
CONSOLE_STATE_GAME = 2

# TODO Globaler Pointer
# C++ Game *game;
game: Game

color: c_ubyte

COIN_MOVEMENT_DELAY = 10
COIN_MOVEMENT_FRAME_MAX = 14

class Console:
    def __init__(self):
        self._joystickLeft: Joystick
        self._joystickRight: Joystick

        self._rgbLed: RgbLed

        self._display: Display

        self._mainClock: MainClock

        self._state: c_ubyte

        # TODO Pointer
        # C++: Game * games[10];
        # Leeres, 10 Elemente großes Array wird angelegt
        self._games: Game = [] * 10

        self._gameCount: c_ubyte
        self._gameindex: c_byte

        # TODO Pointer
        # C++: Game * actualGame;
        self._actualGame: Game

        # TODO auf 12 Bits beschränken
        # C++: uint16_t coinMovementDelay:12;
        self._coinMovementDelay: c_uint16

        # TODO auf 4 Bits beschränken
        # C++: uint16_t coinMovementFrame:4;
        self._coinMovementFrame: c_uint16

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
        if (self._mainClock.isTick()):
            self._joystickLeft.process()
            self._joystickRight.process()
            color += 1
            # TODO Auskommentierte Zeile
            # C++: Serial.println(color);
            # Serial.println(color)
        
        # C++ Switch zu if/else umgewandelt
        if (self._state == CONSOLE_STATE_COIN):
            self.displayCoinAnimation()

            # TODO Auskommentierte Zeile
            # C++: CoinDetection::toggleAnimation();
            # CoinDetection.toggleAnimation()

            if (CoinDetection.startGame()):
                self._state = CONSOLE_STATE_DEMO
        elif (self._state == CONSOLE_STATE_DEMO):
            self.stateDemo()
        elif (self._state == CONSOLE_STATE_GAME):
            self._games[self._gameindex].process()
            if (self._games[self._gameindex].getState() == GAME_STATE_PLAY_DEMO):
                self._state = CONSOLE_STATE_COIN
        
        # TODO Funktionsaufruf
        # C++: random();
        random.random()

        # TODO Auskommentierte Zeile
        # C++: Serial.println("alive");
        # Serial.println("alive")

    def addGame(self, newGame: Game):
        # In C++ mit this->gameCount++ post-incrementiert
        self._games[self._gameCount] = newGame
        self._gameCount += 1

    def stateDemo(self):
        if ((self._joystickLeft.getControlStatus(JOYSTICK_SWITCH_LEFT) == JOYSTICK_STATUS_PRESSED) or
            self._joystickRight.getControlStatus(JOYSTICK_SWITCH_LEFT) == JOYSTICK_STATUS_PRESSED):
            self._gameindex -= 1
            if (self._gameindex < 0):
                self._gameindex = self._gameCount - 1
        
        if ((self._joystickLeft.getControlStatus(JOYSTICK_SWITCH_RIGHT) == JOYSTICK_STATUS_PRESSED) or
            self._joystickRight.getControlStatus(JOYSTICK_SWITCH_RIGHT) == JOYSTICK_STATUS_PRESSED):
            self._gameindex += 1
            if (self._gameindex > (self._gameCount - 1)):
                self._gameindex = 0
        
        self._games[self._gameindex].process()
        if (self._games[self._gameindex].getState() == GAME_STATE_CONFIG):
            self._state = CONSOLE_STATE_GAME

    def displayCoinAnimation(self):
        coinXPos: c_ubyte
        self._coinMovementDelay += 1

        if (self._coinMovementDelay < COIN_MOVEMENT_DELAY):
            return
        
        self._coinMovementDelay = 0
        coinXPos = 18 - self._coinMovementFrame

        Display.clearDisplay()
        Display.matrix.drawRect(7, 1, 4, 14, Display.getColor(7, 7, 7))
        Display.matrix.fillCircle(coinXPos, 8, 5, Display.getColor(7, 4, 0))
        Display.matrix.fillRect(0, 0, 7, 16, Display.getColor(0, 0, 0))
        Display.matrix.drawLine(7, 1, 7, 14, Display.getColor(7, 7, 7))

        self._coinMovementFrame += 1

        if (self._coinMovementFrame > COIN_MOVEMENT_FRAME_MAX):
            self._coinMovementFrame = 0

    def getJoystick(self, index: c_ubyte) -> Joystick:
        # C++ Switch zu if/else umgewandelt
        if (index == 1):
            return self._joystickRight
        else:
            return self._joystickLeft

    @classmethod
    def checkMem(self):
        # Original C++ Methode:
        # void Console::checkMem()
        # { 

        #     uint8_t * t;
        #     t = malloc(1);
        #     Serial.print("mem : ");
        #     Serial.println((uint32_t)t,HEX);
        #     free(t);

        #     uint8_t a;
        #     Serial.print("heap : ");
        #     Serial.println((uint32_t)&a,HEX);
        # }

        # Die Methode macht nur ein wenig mit Speicher rum und gibt was aus.
        # Unwichtig für die Ausführung.
        pass