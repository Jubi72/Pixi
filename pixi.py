# Funktionen
# Pixi - Graphical Portable Pixelmap Editor
# Created by Julius Bittner 04.03.2015
# Last change 19.03.2015

class Pixi:

    def __init__(self):
        # initialisiert Editor
        self.einliste = []
        self.kopf = []
        self.groesse = 0
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

    def einlesen (self,datei):
        # liest Bild ein nach gegebenem Dateinamen
        f = open(datei,"r")    
        self.einliste = f.readlines() #die Rohdaten
        f.close()
        self.kopf        = self.einliste[0:4] 
        self.groesse     = self.kopf[2].split()
        self.breite      = int(self.groesse[0])
        self.hoehe       = int (self.groesse[1])
        self.farbtiefe   = int(self.einliste[3])
        self.punktliste  = []
        self.zeile       =[]
        for i in self.einliste[4:]:
            textzeile = i.strip()
            textzeile = i.split()
            for punkt in textzeile:
                self.zeile.append(int(punkt))
        for i in range(self.hoehe):
                anf  = self.breite*i
                ende = self.breite+anf
                self.punktliste.append(self.zeile[anf:ende])

    def spiegelx (self):
        # spiegelt Bild an x-Achse
        neue_punktliste = []
        for i in self.punktliste:
            neue_punktliste.insert(0,i)
        self.punktliste = neue_punktliste
            

    def spiegely (self):
        # spiegelt Bild an y-Achse
        neue_punktliste = []
        for i in range(self.hoehe):
            zeile=[]
            for j in range(self.breite,0,-1):
                zeile.append(self.punktliste[i][j-1])
            neue_punktliste.append(zeile)
        self.punktliste = neue_punktliste

    def invertieren (self):
        # invertiert Bild
        neue_punktliste=[]
        for zeile in self.punktliste:
            listenzeile=[]
            for wert in zeile:
                neuer_wert=self.farbtiefe-wert
                listenzeile.append(neuer_wert)
            neue_punktliste.append(listenzeile)
        self.punktliste=neue_punktliste
        
    def drehen(self):
        # dreht Bild um 90° nach rechts (oben ist nun rechts und rechts ist unten usw.; mathematisch negative Richtung)
        heohe = self.hoehe
        self.hoehe = self.breite
        self.breite = hoehe
        
        neueliste = list()
        for zeile in range(len(self.punktliste[0])):
            neueliste.append([])
            for elem in range(len(self.punktliste)):
                neueliste[zeile].append(self.punktliste[len(self.punktliste)-1-elem][zeile])
                
        self.punktliste = neueliste.copy()
        
    def schreiben(self,datei):
        # schreibt Bild in gegebenen Dateinamen
        a=open(datei,"w")
        s=''
        kopf=''
        for i in self.kopf:
            kopf+=i
        for i in range (self.hoehe):
            for j in range (self.breite):
                s+=str(self.punktliste[i][j])+" "
            s+="\n"
        a.write(kopf+s)
        a.close()
