# Funktionen
# Pixi - Graphical Portable Pixelmap Editor
# Created by Julius Bittner 04.03.2015
# Last change 10.03.2015

class Pixi:

    def __init__(self):
        # initialisiert Editor
        self.einliste = []
        self.kopf = []
        self.masse = 0
        self.breite = 0
        self.hoehe = 0
        self.farbtiefe = 0
        self.punktliste = []

    def binary (self):
        # Bild muss eingelesen sein, dann wird Bild in Binary umgewandelt.
        neueliste = self.punktliste.copy()
        for reihe in range(len(self.punktliste)):
            for px in range(len(self.punktliste[reihe])):
                neueliste[reihe][px] = chr(punktliste[reihe][px])
        self.punktliste = neueliste.copy()
		
        kind = str(int(self.kopf[0][1]) + 3)
        self.kopf[0] = "P" + kind + "\n"
