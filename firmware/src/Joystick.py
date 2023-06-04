
import RPi.GPIO as GPIO

from Microcontroller import *

JOYSTICK_STATUS_NOT_PRESSED = 0
JOYSTICK_STATUS_PRESSED = 1
JOYSTICK_STATUS_HOLD = 2

JOYSTICK_SWITCH_LEFT = 0
JOYSTICK_SWITCH_UP = (JOYSTICK_SWITCH_LEFT + 1 )
JOYSTICK_SWITCH_RIGHT = (JOYSTICK_SWITCH_UP	 + 1 )
JOYSTICK_SWITCH_DOWN = (JOYSTICK_SWITCH_RIGHT + 1 ) 
JOYSTICK_SWITCH_BUTTON_TOP = (JOYSTICK_SWITCH_DOWN + 1 )
JOYSTICK_SWITCH_BUTTON_BODY = (JOYSTICK_SWITCH_BUTTON_TOP + 1 )

JOYSTICK_SWITCHES_COUNT = (JOYSTICK_SWITCH_BUTTON_BODY + 1)


class JoystickPins_t:
    def __init__(self) -> None:
        left: int
        up: int
        right: int
        down: int
        buttonTop: int
        buttonBody: int


class JoystickEdge_t:
    def __init__(self) -> None:
        # TODO In C++ Quellcode auf 2 Bits begrenzt
        # typedef struct {
        # 	uint16_t left:2;
        # 	uint16_t up:2;
        # 	uint16_t right:2;
        # 	uint16_t down:2;
        # 	uint16_t buttonTop:2;
        # 	uint16_t buttonBody:2;
        # } JoystickEdge_t;
        left: int
        up: int
        right: int
        down: int
        buttonTop: int
        buttonBody: int


class Joystick:
    def __init__(self) -> None:
        self.__pins: JoystickPins_t
        self.__edges: JoystickEdge_t

        self.__value: int
    
    # TODO Parameter pins ein Pointer
    # C++:
    # void init(JoystickPins_t * pins);
    def init(self, pins: JoystickPins_t):
        self.__pins = pins

        # BCM Pinmodus verwenden
        GPIO.setmode(GPIO.BCM)

        # TODO C++ Quellcode:
        # pinMode(this->pins.left, INPUT_PULLUP);
        # pinMode(this->pins.up, INPUT_PULLUP);
        # pinMode(this->pins.right, INPUT_PULLUP);
        # pinMode(this->pins.down, INPUT_PULLUP);
        # pinMode(this->pins.buttonTop, INPUT_PULLUP);
        # pinMode(this->pins.buttonBody, INPUT_PULLUP);

        GPIO.setup(self.__pins.left, GPIO.IN)
        GPIO.setup(self.__pins.up, GPIO.IN)
        GPIO.setup(self.__pins.right, GPIO.IN)
        GPIO.setup(self.__pins.down, GPIO.IN)
        GPIO.setup(self.__pins.buttonTop, GPIO.IN)
        GPIO.setup(self.__pins.buttonBody, GPIO.IN)
        pass

    def isLeft(self) -> bool:
        pass
    def isUp(self) -> bool:
        pass
    def isRight(self) -> bool:
        pass
    def isDown(self) -> bool:
        pass
    def isButtonTop(self) -> bool:
        pass
    def isButtonBody(self) -> bool:
        pass

    def process(self):
        pass

    def getSwitchStatus(self, switchId: int) -> bool:
        pass

    def getControlStatus(self, switchId: int) -> int:
        pass
    def setControlStatus(self, switchId: int, status: int):
        pass
