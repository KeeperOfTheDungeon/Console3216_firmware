
CHANNEL_1 = 0
CHANNEL_2 = 1
CHANNEL_3 = 2
CHANNEL_DRUM = 9

SOUNDEFFECTS_LENGTH = 3

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

    @classmethod
    def __sortSoundEffects(idx: int):
        pass

    @classmethod
    def init(cls):
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
