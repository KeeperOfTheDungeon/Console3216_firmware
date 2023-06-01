from enum import Enum
from ctypes import Structure, Union, c_ubyte, c_uint

# TODO In C++ unter namespace MIDI

# TODO C++ Code:
# enum CommandType {
#     NoteOn,
#     NoteOff,
#     ProgramChange,
#     ControllerChange,
#     EndOfTrack,
#     SetTempo,
# };

class CommandType(Enum):
    NoteOn = 0
    NoteOff = 1
    ProgramChange = 2
    ControllerChange = 3
    EndOfTrack = 4
    SetTempo = 5

# TODO C++ Code:
# struct EmptyEvent {};
class EmptyEvent(Structure):
    _fields_ = []


class NoteEvent(Structure):
    # TODO In C++ sind alle Variablen unsigned chars, c_uchar existiert nicht
    _fields_ = [("channel", c_ubyte), ("note", c_ubyte), ("velocity", c_ubyte)]


class ProgramChangeEvent(Structure):
    # TODO In C++ sind alle Variablen unsigned chars, c_uchar existiert nicht
    _fields_ = [("channel", c_ubyte), ("programNumber", c_ubyte)]


class ControllerChangeEvent(Structure):
    # TODO In C++ sind alle Variablen unsigned chars, c_uchar existiert nicht
    _fields = [("channel", c_ubyte), ("controller", c_ubyte), ("value", c_ubyte)]


# Externe Arraydefinition für SetTempoEvent
char_array = c_ubyte * 3


class SetTempoEvent(Structure):
    _fields_ = [("tempo", char_array)]


# Externe Union Definition für Command
class DataUnion(Union):
    _fields_ = [("noteOn", NoteEvent),
                ("noteOff", NoteEvent),
                ("programChange", ProgramChangeEvent),
                ("controllerChange", ControllerChangeEvent),
                ("endOfTrack", EmptyEvent),
                ("setTempo", SetTempoEvent)]


class Command(Structure):
    _fields_ = [("deltaTime", c_uint),
                ("type", CommandType),
                ("data", DataUnion)]
