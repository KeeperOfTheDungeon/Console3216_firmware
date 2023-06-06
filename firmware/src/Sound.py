
from Midi import *

CHANNEL_1 = 0
CHANNEL_2 = 1
CHANNEL_3 = 2
CHANNEL_DRUM = 9

SOUNDEFFECTS_LENGTH = 3

CONTROL_CHANNEL_VOLUME = 7
CONTROL_CHANNEL_BALANCE = 10

CONTROL_CHANNEL_VELOCITY = 64

class Sound:
    # Kommentare aus dem C++ Quellcode herauskopiert:

    # faengt bei 1 an zu zaehlen, 0 ist reserviert, siehe alarmSound[]
    __steps: int
    # 3 Elemente: Einen fuer jeden Voice-Channel, alarmSound[] = 0 -> dauerhafter Ton, bzw. kein Endzeitpunkt
    __alarmSound = [0] * 3
    # 3 Elemente: 3 gleichzeitig abspielbare SoundEffects auf der 3x-Polyfonen Drum-Map
    __alarmSoundEffect = [0] * 3
    # Hier werden die Sounds passend zu den Voice-Channels gespeichert, d.h. sound[0] wird auf CHANNEL_1 gespielt
    __sound = [0] * 3
    # Hier werden die SoundEffects auf der Drum-Map gespeichert
    # WICHTIG: Diese sind sortiert, zuletzt hinzugefuegte SoundEffects haben immer den kleineren Index.
    # BSP: [Neuester][Mittlerer][Aeltester]
    __soundEffects = [0] * SOUNDEFFECTS_LENGTH

    # Private Funktion, um die zeitliche Hierarchie im SoundEffect-Array
    # zu erhalten und um einen SoundEffect nach dem Stoppen aus dem Array zu loeschen
    @classmethod
    def __sortSoundEffects(cls, idx: int):
        for i in range(idx, SOUNDEFFECTS_LENGTH):
            cls.__soundEffects[i] = cls.__soundEffects[i + 1]
            cls.__alarmSoundEffect[i] = cls.__soundEffects[i + 1]
        
        # letzte Stelle im Array "freiraeumen"
        cls.__soundEffects[SOUNDEFFECTS_LENGTH - 1] = 0
        cls.__alarmSoundEffect[SOUNDEFFECTS_LENGTH - 1] = 0
        pass

    @classmethod
    def init(cls):
        Midi.init()
        cls.__steps = 1
        pass

    @classmethod
    def reset(cls):
        pass

    @classmethod
    def setPreset(cls, index: int):
        pass
    @classmethod
    def setPresetCh(cls, index: int, channel: int):
        pass

    @classmethod
    def setVolume(cls, volume: int):
        pass
    @classmethod
    def setVolumeCh(cls, volume: int, channel: int):
        pass

    @classmethod
    def setPanorama(cls, panorama: int):
        pass
    @classmethod
    def setPanoramaCh(cls, panorama: int, channel: int):
        pass

    @classmethod
    def playSound(cls, note: int, channel: int):
        pass
    @classmethod
    def playSoundDura(cls, note: int, channel: int, duration: int):
        pass

    @classmethod
    def stopSound(cls, note: int, channel: int):
        pass
    @classmethod
    def stopSounds(cls):
        pass

    @classmethod
    def playSoundEffect(cls, soundEffect: int):
        pass
    @classmethod
    def playSoundEffectDura(cls, soundEffect: int, duration: int):
        pass

    @classmethod
    def stopSoundEffect(cls, soundEffect: int):
        pass
    @classmethod
    def stopSoundEffects(cls):
        pass

    @classmethod
    def step(cls):
        pass
