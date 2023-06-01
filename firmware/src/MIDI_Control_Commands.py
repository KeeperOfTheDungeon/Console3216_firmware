
# TODO Nicht sicher, ob es auch ohne die C Union geht
from ctypes import Union, c_int16, c_int8, Structure

class halfValue(Structure):
        _fields_ = [("secondByte", c_int8),
                    ("firstByte", c_int8)]

class MIDI_Control_Commands:
    __SERIAL_BAUD = 74880
    __COMMAND_CODE_PLAY_TRACK = 0x01
    __COMMAND_CODE_CHANGE_TEMPO = 0x02
    __COMMAND_CODE_PAUSE_TRACK = 0x03
    __COMMAND_CODE_STOP_TRACK = 0x04
    __COMMAND_CODE_RESUME_TRACK = 0x05
    __COMMAND_CODE_RESTART_TRACK = 0x06

    # TODO Eventuell kommen wir auch ohne aus
    # C++ Code:
    # union byteConverter {
    #     uint16_t value;
    #     struct {
    #         int8_t secondByte;
    #         int8_t firstByte;
    #     };
    # };

    # TODO Muss getestet werden
    class byteConverter(Union):
        _anonymous_ = ("h",)
        _fields_ = [("value", c_int16),
                    ("h", halfValue)]

    def __init__(self) -> None:
        pass

    @classmethod
    def playTrack(cls, trackId: int, tempo: int):
        pass

    @classmethod
    def changeTempo(cls, trackId: int, tempo: int):
        pass

    @classmethod
    def pauseTrack(cls, trackId: int):
        pass

    @classmethod
    def stopTrack(cls, trackId: int):
        pass

    @classmethod
    def resumeTrack(cls, trackId: int):
        pass

    @classmethod
    def restartTrack(cls, trackId: int):
        pass

    @classmethod
    def setupMidi(cls):
        pass
