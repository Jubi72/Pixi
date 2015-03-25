# Funktionen
# Pixi - Graphical Portable Pixelmap Editor
# Created by Julius Bittner 04.03.2015
# Last change 23.03.2015

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
        self.bintext = []

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
        self.binary()
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
        # invertiert Bild/kehrt Farbwerte um
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
        hoehe = self.hoehe
        self.hoehe = self.breite
        self.breite = hoehe
        self.kopf[2] = str(self.breite) + " " + str(self.hoehe) + "\n"
        
        neueliste = list()
        for zeile in range(len(self.punktliste[0])):
            neueliste.append([])
            for elem in range(len(self.punktliste)):
                neueliste[zeile].append(self.punktliste[len(self.punktliste)-1-elem][zeile])
                
        self.punktliste = neueliste.copy()

    def binary(self):
        # schreibt Bild als Binary
        self.bintext = str()
        for i in self.punktliste:
            for j in i: self.bintext += chr(j)

    def binschreiben(self,datei):
        # schreibt Bild in gegebenen Dateinamen als Binary
        self.binary()
        a=open(datei,"w")
        kopf=''
        for i in self.kopf: kopf+= i
        a.write(kopf+self.bintext)
        a.close()
        
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
