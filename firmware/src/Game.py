# TODO
# C++: #include <Arduino.h>

# TODO
import Joystick

# TODO
import NumericDisplay

# TODO
import MainClock

# TODO
import StartButton

import Display

from ctypes import c_ubyte, c_uint32, c_uint16

GAME_STATE_PREPARE_DEMO			= 0
GAME_STATE_PLAY_DEMO			= GAME_STATE_PREPARE_DEMO + 1

GAME_STATE_CONFIG	        	= GAME_STATE_PLAY_DEMO + 1
GAME_STATE_PLAY			        = GAME_STATE_CONFIG + 1

GAME_STATE_SCORE                = GAME_STATE_PLAY +1
GAME_STATE_HIGHSCORE_GRAPHIC    = GAME_STATE_SCORE +1 
GAME_STATE_HIGHSCORE_NEW        = GAME_STATE_HIGHSCORE_GRAPHIC + 1 
GAME_STATE_HIGHSCORE_NAME       = GAME_STATE_HIGHSCORE_NEW + 1
GAME_STATE_DISPLAY_HIGHSCORES   = GAME_STATE_HIGHSCORE_NAME +1
GAME_STATE_END					= GAME_STATE_DISPLAY_HIGHSCORES +1

PLAYER_TYPE_HUMAN		= 0
PLAYER_TYPE_AI_0		= 1
PLAYER_TYPE_AI_1		= 2
PLAYER_TYPE_AI_2		= 3
PLAYER_TYPE_AI_3		= 4
PLAYER_TYPE_AI_4		= 5
PLAYER_TYPE_AI_5		= 6
PLAYER_TYPE_AI_6		= 7
PLAYER_TYPE_AI_7		= 8
PLAYER_TYPE_AI_8		= 9
PLAYER_TYPE_AI_9		= 10

GAME_NAME_MAX_LENGHT = 6

# TODO Struct
# C++:
# typedef struct  {
#     uint16_t score;
#     char name[4];
# } Score_t;
class Score_t:
    def __init__(self, score, name) -> None:
        self.score: c_uint16 = score
        self.name: str = name

class Game:
    def __init__(self, leftJoystick: Joystick, rightJoystick: Joystick, name: str):
        # TODO Pointer
        # C++:  Joystick * joystickLeft;
        #       Joystick * joystickRight;
        self._joystickLeft: Joystick
        self._joystickRight: Joystick

        self._state: c_ubyte
        self._time: c_uint32

        # TODO Auf 4 Bits begrenzt
        # C++:  uint8_t player1Type:4;
        #       uint8_t player2Type:4;
        self._player1Type: c_ubyte
        self._player2Type: c_ubyte

        # TODO Auf 2 Bits begrenzt
        # C++:  uint8_t startButtonStatus:2;
        self._startButtonStatus: c_ubyte

        self._currentScore: Score_t(0, "   ")

        # Diese Zeile erstellt ein Objekt mit 3 Referenzen darauf
        # FALSCH: self._Highscores = [Score_t(0, "   ")] * 3
        # Diese Zeile erstellt 3 Objekte die unabhängig von einander verändert werden können
        self._Highscores = Score_t(0, "   "), Score_t(0, "   "), Score_t(0, "   ")
        # C++: Score_t Highscores[3] = { {0, "   "}, {0, "   "}, {0, "   "} };

        self.__isHighscore: int
        self.__click_Count: c_ubyte = 0

    # TODO BEGIN Virtuelle Methoden:
    def process(self):
        pass # TODO

    def _draw(self):
        pass # TODO

    def _play(self):
        pass # TODO

    def _prepareDemo(self):
        pass # TODO

    def _playDemo(self):
        pass # TODO

    def _prepareGame(self):
        pass # TODO

    def _playGame(self):
        pass # TODO

    def _gameOver(self):
        pass # TODO

    def _timeStart(self):
        pass # TODO

    def _timeCountUp(self):
        pass # TODO

    def _displayNewHighscore(self):
        pass # TODO

    def _displayHighscores(self):
        pass # TODO
    # TODO END Virtuelle Methoden

    def setState(self, newState: c_ubyte):
        pass # TODO

    def getState(self):
        pass # TODO 

    def _configMultiplayerGame(self):
        pass # TODO

    def _configurePlayer(self, playerNr: c_ubyte, joystick: Joystick, playerType: c_ubyte) -> c_ubyte:
        pass # TODO

    def __submitHighscore():
        pass # TODO

    def __enterName(self, s: Score_t):
        pass # TODO

    def __enterNameWithLoops(self, s: Score_t):
        pass # TODO

    def __insertHighscore(self, i: int):
        pass # TODO