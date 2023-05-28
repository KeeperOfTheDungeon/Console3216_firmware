# TODO C++ includes:
# Adafruit_GFX.h
# gfxfront.h
# RGBMatrixPanel.h

import os
# TODO Unbenutzter Import
# import Microcontroller
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

DISPLAY_X_EXTEND = 32
DISPLAY_Y_EXTEND = 16

# Matrix Options
DISPLAY_X = 32
DISPLAY_Y = 16
DISPLAY_SCALE_FACTOR = 64
DISPLAY_CHAIN = 1
HARDWARE_MAPPING = "adafruit-hat"

# TODO Schriftarten
# In der C++ Implementierung konnte ein Skalierungsfaktor angegeben werden,
# das simulieren wir indem wir einfach mehrere Schriftarten verwenden
# TODO Liste nicht fertig
FONT_LIST = ["4x6.bdf", "6x9.bdf"]


class Display:
    matrix: RGBMatrix
    fonts: list

    # def __rescale_to_local(self, coordinate: int):
    #     return coordinate / DISPLAY_SCALE_FACTOR

    # TODO Konstruktor in C++ vorhanden
    def __init__(self):
        # TODO Aus C++ übernommen, wird aber anscheinend nirgendwo verwendet
        self.__prevBallX: int
        self.__prevBallY: int
        self.__prevP1: int
        self.__prevP2: int

    @classmethod
    def init(cls):
        # TODO Alter Matrix Init Code
        # Wurde in C++ mit "new" angelegt, weil matrix ein Pointer ist
        # Display.matrix = RGBMatrixPanel(A, B, C, CLK, LAT, OE, True)
        # Display.matrix.begin()
        # Display.matrix.fillScreen(self.matrix.Color333(0, 0, 7)) # BLUE
        # Display.matrix.fillScreen(self.matrix.Color333(0, 0, 0)) # CLEAR

        # Neuer Matrix Init Code
        matrix_options = RGBMatrixOptions()
        matrix_options.rows = DISPLAY_X
        matrix_options.cols = DISPLAY_Y
        matrix_options.chain_length = DISPLAY_CHAIN
        matrix_options.hardware_mapping = HARDWARE_MAPPING

        # Schriftarten laden
        cls.import_fonts()

        cls.matrix = RGBMatrix(options=matrix_options)
        cls.matrix.Clear()

    @classmethod
    def import_fonts(cls):
        """_summary_
        Importiert die Schriftarten für die Textausgabe
        """
        font_path = os.path.join(os.path.curdir, "fonts")

        # TODO 2 mögliche Methoden zum importieren von Schriftarten

        # Methode 1:
        # Schriftarten werden manuell in ein Array eingetragen
        # Vorteil: Reihenfolge kann direkt festgelegt werden
        # Nachteil: Hardcoded und muss im Code angepasst werden,
        # wenn nötog.
        for font in FONT_LIST:
            cls.fonts.append(graphics.Font())
            cls.fonts[-1].LoadFont(os.path.join(font_path, font))

        # Methode 2:
        # Alle Schriftarten, die sich im Ordner befinden, werden geladen
        # Vorteil: Code muss nicht angepasst werden, wenn die Schriftarten
        # sich ändern.
        # Nachteil: Reihenfolge muss im Dateinamen festgemacht werden,
        # Tests nötig, ob die Dateien in der gewünschten Reihenfolge
        # behandelt werden
        for filename in os.listdir(font_path):
            if filename.endswith(".bdf"):
                file_path = os.path.join(os.path.curdir, filename)
                cls.fonts.append(graphics.Font())
                cls.fonts[-1].LoadFont(file_path)

    @classmethod
    def refresh(cls):
        Display.matrix.SwapOnVSync()

    @classmethod
    def drawPixel(cls, x: int, y: int, r: int, g: int, b: int):
        if ((x < DISPLAY_X_EXTEND) and (y < DISPLAY_Y_EXTEND)):
            Display.matrix.SetPixel(x, y, r, g, b)

    # TODO Auskommentierte Zeile
    # C++: static void drawRect(int16_t x, int16_t y,
    #                           int16_t w, int16_t h, uint16_t color);
    # @classmethod
    # def drawRect(self, x: int, y: int, w: int, h: int, color: int)

    @classmethod
    def clearDisplay(cls):
        cls.matrix.Clear()

    @classmethod
    def drawText(cls, text: str, x: int, y: int, r, g, b, scaleFactor: int):
        # cls.matrix.setCursor(x, y)
        # cls.matrix.setTextColor(color)
        # cls.matrix.setTextSize(scaleFactor)
        # cls.matrix.print(text)
        color = graphics.Color(r, g, b)
        # TODO Skalierungsfaktor mit mehreren Schriftarten simulieren
        # TODO Erster Parameter gibt Canvas an
        # Eventuell muss neuer Hintergrund Canvas erzeugt werden
        graphics.DrawText(cls.matrix,
                          cls.fonts[scaleFactor],
                          x, y,
                          color,
                          text)

    # TODO Nicht mehr benötigt
    # Farbe wird nun als 3 ints, 0-255 r, g, b angegeben
    # @classmethod
    # def getColor(self, red: int, green: int, blue: int) -> int:
    #    return Display.matrix.Color333(red, green, blue)

    # TODO Kein Python Äquivalent, dafür können jetzt Bilddateien angezeigt werden
    # Wird aber eventuell nicht benötigt
    # @classmethod
    # def drawBitmap(cls, x: int, y: int, bitmap: int, width: int, height: int, color: int):
    #     self.matrix.drawBitmap(self.__rescaleToLocal(x), self.__rescaleToLocal(y), bitmap, width, height, color)
