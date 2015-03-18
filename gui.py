# Graphical User Interface
# Pixi - Graphical Portable Pixelmap Editor
# Created by Julius Bittner 04.03.2015
# Last change 13.03.2015

import pixi
import tkinter as tk
import os
from tkinter.filedialog import askopenfilename

class Gui:

    def __init__(self):
        # initialisiert Grafische Benutzeroberfläche
        self.root = tk.Tk()
        self.root.title("Pixi")
        self.root.config(bg="red")
        self.root.geometry("400x100+100+100")
        self.filename = "" # Dateiname für Bild
        
        tk.Label(self.root, text="Pixi", fg="white", bg="red", font="Georgia 48").pack()
        
        self.menu()

        self.root.mainloop()

    def menu(self):
        # erstellt Menü
        menubar = tk.Menu(self.root)
        
        dateimenu = tk.Menu(menubar) # Menü zum Verwalten der Datei
        dateimenu.add_command(label="Öffnen", command=self.einlesen)
        dateimenu.add_command(label="Speichern", command=self.speichern)
        dateimenu.add_command(label="Speichern unter",command=self.speichern_unter)
        dateimenu.add_separator()
        dateimenu.add_command(label="Eigenschaften", command=self.eigenschaften)
        dateimenu.add_command(label="Dateiinhalt anzeigen",command=self.plaintext)
        dateimenu.add_separator()
        dateimenu.add_command(label="Schließen", command=self.root.destroy)

        bearbeitenmenu = tk.Menu(menubar) # Menü zum Bearbeiten des Bilds
        bearbeitenmenu.add_command(label="Spiegeln an x",command=self.spiegeln_x)
        bearbeitenmenu.add_command(label="Spiegeln an y",command=self.spiegeln_y)
        bearbeitenmenu.add_separator()
        bearbeitenmenu.add_command(label="Drehen nach rechts", command=self.drehen_rechts)
        bearbeitenmenu.add_command(label="Drehen nach links",  command=self.drehen_links)
        bearbeitenmenu.add_separator()
        bearbeitenmenu.add_command(label="Farben invertieren",command=self.invertieren)

        hilfemenu = tk.Menu(menubar) # Menü zum Aufrufen von Hilfefunktionen
        hilfemenu.add_command(label="Hilfe anzeigen", command=self.hilfe)
        hilfemenu.add_separator()
        hilfemenu.add_command(label="Über Pixi", command=self.about)
        
        menubar.add_cascade(label="Datei", menu=dateimenu)
        menubar.add_cascade(label="Bearbeiten", menu=bearbeitenmenu)
        menubar.add_cascade(label="Hilfe", menu=hilfemenu)

        self.root.config(menu=menubar)
        
    def einlesen(self):
        # liest Bild ein
        self.filename = askopenfilename()
        self.bild = pixi.Pixi()
        self.bild.einlesen(self.filename)

        tk.Label(self.root, text=self.filename, bg="red", fg="white").pack()

    def speichern(self):
        # Speichert Datei unter gleichem Namen
        self.bild.schreiben(self.filename)

    def speichern_unter(self):
        # Speichert Datei unter (anderem) Namen
        self.filename = askopenfilename()
        self.bild.schreiben(self.filename)

    def plaintext(self):
        # zeigt Inhalt der Datei in Plaintext an
        pass

    def eigenschaften(self):
        # zeigt Inhalt der Datei gut erkennbar
        pass

    def spiegeln_x(self):
        # Spiegelt Bild an x-Achse
        self.bild.spiegelx()

    def spiegeln_y(self):
        # Spiegelt Bild an y-Achse
        self.bild.spiegely()
    
    def invertieren(self):
        # invertiert Farben des Bilds
        self.bild.invertieren()

    def drehen_rechts(self):
        # Dreht Bild um 90 ° nach rechts
        pass

    def drehen_links(self):
        # dreht Bild um 90 ° nach links
        pass

    def hilfe(self):
        # zeigt Hilfetext an
        hilfetext = """Hallo, hier bekommst Du alle wichtigen Informationen zur Funktionsweise dieses Programmes.
Wir hoffen, dass wir Dir helfen können dieses Programm zu verstehen.

Unser Programm dient zur Verarbeitung von Bildern. Zuerst öffnest Du ein Graustufenbild, indem Du in der
Menüleiste auf "Datei" klickst und auf die Schaltfläche "Öffnen" drückst. Nachdem Du ein Bild ausgesucht hast,
kannst Du verschiedene Sachen mit diesem Bild anstellen.

Klicke in der Menüleiste auf "Bearbeiten" und Du siehst die Arbeitsschritte, die unser Programm anbietet.
Du kannst dein Bild an der x- und y-Achse spiegeln lassen, das Bild nach links und rechts drehen und zu guterletzt
die Farbwerte des Bildes invertieren. Du kannst also die Farbwerte umkehren. Aus weiß wird schwarz und anders herum.

Wenn Du erneut auf "Datei" in der Menüleiste klickst, siehst Du die Felder "Speichern" und "Speichern unter".
Mit diesen Funktionen lässt sich dein geändertes Bild speichern. Du kannst Dir natürlich auch den Dateiinhalt
und die Eigenschaften des Bildes anschauen.

Wir hoffen, dass wir Dir helfen konnten und wünschen einen angenehmen gebrauch des PGM-Editor."""

        hilfef = tk.Tk()
        hilfef.title("Pixi-Hilfe")
        hilfef.config(bg="red")

        tk.Label(hilfef, text=hilfetext, bg="red", font="Georgia 13", fg="white").pack()
        tk.Button(hilfef, text="Schließen", command=hilfef.destroy).pack()

        hilfef.mainloop()

    def about(self):
        # zeigt Informationen über das Programm an
        abouttext = """Pixi

Grafischer PGM-Editor

Version 0.0.1

Copyright Lucas Herrenkind
und Julius Bittner 2015

Kontakt:"""
        email = "content.legoag@gmail.com"
        about = tk.Tk()
        about.title("Über Pixi")
        about.config(bg="red")

        tk.Label(about, text=abouttext, bg="red", font="Georgia 13", fg="white").pack()
        kont = tk.Label(about, text=email, bg="red", font="Georgia 13", fg="yellow")
        kont.bind("<Button>",
           lambda event:os.execl("http://mailto:content.legoag@gmail.com"))
    
        kont.pack()
        tk.Button(about, text="Schließen", command=about.destroy).pack()

        about.mainloop()
        
pic = Gui()

