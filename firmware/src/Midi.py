
MIDI_COMMAND_NOTE_OFF = 0x80
MIDI_COMMAND_NOTE_ON = 0x90
MIDI_COMMAND_CONTROL_CHANGE = 0xB0
MIDI_COMMAND_PROGRAMM_CHANGE = 0xC0

class Midi:
    @classmethod
    def init(cls):
        pass

    @classmethod
    def noteOn(cls, channel: int, note: int, velocity: int):
        pass

    @classmethod
    def noteOff(cls, channel: int, note: int):
        pass

    @classmethod
    def controlChange(channel: int, control: int, value: int):
        pass

    @classmethod
    def programChange(channel: int, preset: int):
        pass
