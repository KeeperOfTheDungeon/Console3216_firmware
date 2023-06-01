
# TODO
# C++: #include <Arduino.h>

from Joystick import *
from NumericDisplay import *
from MainClock import *
from StartButton import *
from Display import *


GAME_STATE_PREPARE_DEMO = 0
GAME_STATE_PLAY_DEMO = GAME_STATE_PREPARE_DEMO + 1

GAME_STATE_CONFIG = GAME_STATE_PLAY_DEMO + 1
GAME_STATE_PLAY = GAME_STATE_CONFIG + 1

GAME_STATE_SCORE = GAME_STATE_PLAY + 1
GAME_STATE_HIGHSCORE_GRAPHIC = GAME_STATE_SCORE + 1
GAME_STATE_HIGHSCORE_NEW = GAME_STATE_HIGHSCORE_GRAPHIC + 1
GAME_STATE_HIGHSCORE_NAME = GAME_STATE_HIGHSCORE_NEW + 1
GAME_STATE_DISPLAY_HIGHSCORES = GAME_STATE_HIGHSCORE_NAME + 1
GAME_STATE_END = GAME_STATE_DISPLAY_HIGHSCORES + 1

PLAYER_TYPE_HUMAN = 0
PLAYER_TYPE_AI_0 = 1
PLAYER_TYPE_AI_1 = 2
PLAYER_TYPE_AI_2 = 3
PLAYER_TYPE_AI_3 = 4
PLAYER_TYPE_AI_4 = 5
PLAYER_TYPE_AI_5 = 6
PLAYER_TYPE_AI_6 = 7
PLAYER_TYPE_AI_7 = 8
PLAYER_TYPE_AI_8 = 9
PLAYER_TYPE_AI_9 = 10

GAME_NAME_MAX_LENGHT = 6


# TODO Struct
# C++:
# typedef struct  {
#     uint16_t score;
#     char name[4];
# } Score_t;
class Score_t:
    def __init__(self, score, name) -> None:
        self.score: int = score
        self.name: str = name


class Game:
    # TODO gameName ist ein char Pointer in C++
    def __init__(self, leftJoystick: Joystick, rightJoystick: Joystick, gameName: int):
        # TODO Pointer
        # C++:  Joystick * joystickLeft;
        #       Joystick * joystickRight;
        self._joystickLeft: Joystick
        self._joystickRight: Joystick

        # C++: char name[GAME_NAME_MAX_LENGHT];
        self._name: int = [0] * GAME_NAME_MAX_LENGHT

        self._state: int
        self._time: int

        # TODO Auf 4 Bits begrenzt
        # C++:  uint8_t player1Type:4;
        #       uint8_t player2Type:4;
        self._player1Type: int
        self._player2Type: int

        # TODO Auf 2 Bits begrenzt
        # C++:  uint8_t startButtonStatus:2;
        self._startButtonStatus: int

        self._currentScore: Score_t(0, "   ")

        # Diese Zeile erstellt ein Objekt mit 3 Referenzen darauf
        # FALSCH: self._Highscores = [Score_t(0, "   ")] * 3
        # Diese Zeile erstellt 3 Objekte die unabhängig von einander verändert werden können
        self._Highscores = Score_t(0, "   "), Score_t(0, "   "), Score_t(0, "   ")
        # C++: Score_t Highscores[3] = { {0, "   "}, {0, "   "}, {0, "   "} };

        self.__isHighscore: int
        self.__click_Count: int = 0

        # TODO Serial nicht implementiert/importiert
        # C++ Code:
        # Serial.print("stick : ");
        # Serial.println((uint32_t) &leftJoystick, HEX);
        self._joystickLeft = leftJoystick
        # Serial.println((uint32_t) &rightJoystick, HEX);
        self._joystickRight = rightJoystick

        # TODO C++:
        # for (uint8_t counter = 0; counter < GAME_NAME_MAX_LENGHT; counter++) {
        # this->name[counter] = *gameName++;
        # }
        # this->name[GAME_NAME_MAX_LENGHT - 1] = 0;
        for counter in range(0, GAME_NAME_MAX_LENGHT):
            self._name[counter] = gameName
            gameName += 1

        self._name[-1] = 0
        self._state = GAME_STATE_PREPARE_DEMO

    # TODO BEGIN Virtuelle Methoden:
    def process(self):
        if self._state == GAME_STATE_PREPARE_DEMO:
            self._prepareDemo()
            self._state = GAME_STATE_PLAY_DEMO
        elif self._state == GAME_STATE_PLAY_DEMO:
            # TODO Noch nicht implementiert
            if StartButton.getStatus() == START_BUTTON_PRESSED:
                self._state = GAME_STATE_CONFIG
        elif self._state == GAME_STATE_CONFIG:
            self._configMultiplayerGame()
            if StartButton.getStatus() == START_BUTTON_PRESSED:
                self._prepareGame()
                self._state = GAME_STATE_PLAY
        elif self._state == GAME_STATE_PLAY:
            self._playGame()
        elif self._state == GAME_STATE_SCORE:
            self.__submitHighscore()
            if self.__isHighscore < 0:
                self._state = GAME_STATE_DISPLAY_HIGHSCORES
            else:
                self._state = GAME_STATE_HIGHSCORE_GRAPHIC
        elif self._state == GAME_STATE_HIGHSCORE_GRAPHIC:
            self._displayNewHighscore()
            if StartButton.getStatus() == START_BUTTON_PRESSED:
                self._state = GAME_STATE_HIGHSCORE_NAME
        elif self._state == GAME_STATE_HIGHSCORE_NAME:
            self.__enterName(self._Highscores[self.__isHighscore])
        elif self._state == GAME_STATE_DISPLAY_HIGHSCORES:
            self._displayHighscores()
            if StartButton.getStatus() == START_BUTTON_PRESSED:
                self.__click_Count = 0
                self._state = GAME_STATE_PREPARE_DEMO
        elif self._state == GAME_STATE_END:
            self._gameOver()
            if StartButton.getStatus() == START_BUTTON_PRESSED:
                self._state = GAME_STATE_PREPARE_DEMO
    
        self._timeCountUp()

    def _draw(self):
        # TODO In C++ game.cpp leer
        pass

    def _play(self):
        # TODO In C++ game.cpp leer
        pass

    def _prepareDemo(self):
        # TODO In C++ game.cpp leer
        pass

    def _playDemo(self):
        # TODO In C++ game.cpp leer
        pass

    def _prepareGame(self):
        # TODO In C++ game.cpp leer
        pass

    def _playGame(self):
        # TODO In C++ game.cpp leer
        pass

    def _gameOver(self):
        # Farbe wird nicht mehr in 9 bit angegeben, sondern 24 bit (3x 255)
        # Umrechnung erfolgt wie folgt: 256 / 8 * x - 1
        # C++ Code:
        # uint16_t textColor;
        # textColor = Display::getColor(2, 2, 0);
        Display.Display.clearDisplay()
        Display.Display.drawText("GAME", 4, 0, 63, 63, 0, 1)
        Display.Display.drawText("OVER", 4, 8, 63, 63, 0, 1)

        Display.Display.refresh()
        pass

    def _timeStart(self):
        self._time = 0
        pass

    def _timeCountUp(self):
        # TODO Noch nicht klar, wo TIME_BASIS_MS in C++ deklariert wurde
        self._time += TIME_BASIS_MS
        pass

    def _displayNewHighscore(self):
        Display.Display.clearDisplay()
        Display.Display.drawText("NEW HS", 4, 0, 63, 63, 0, 1)

        Display.Display.refresh()
        # TODO Noch nicht implementiert
        # TODO C++ Code:
        # NumericDisplay::displayValue(1, this->currentScore.score);
        NumericDisplay.NumericDisplay.displayValue(1, self._currentScore.score)
        pass

    def _displayHighscores(self):
        pass # TODO
    # TODO END Virtuelle Methoden

    def setState(self, newState: int):
        pass # TODO

    def getState(self):
        pass # TODO 

    def _configMultiplayerGame(self):
        pass # TODO

    def _configurePlayer(self, playerNr: int, joystick: Joystick, playerType: int) -> int:
        pass # TODO

    def __submitHighscore(self):
        pass # TODO

    def __enterName(self, s: Score_t):
        pass # TODO

    def __enterNameWithLoops(self, s: Score_t):
        pass # TODO

    def __insertHighscore(self, i: int):
        pass # TODO
