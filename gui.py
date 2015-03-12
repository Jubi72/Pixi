# Graphical User Interface
# Pixi - Graphical Portable Pixelmap Editor
# Created by Julius Bittner 04.03.2015
# Last change 11.03.2015

import pixi
import tkinter as tk
from tkinter.filedialog import askopenfilename

class Gui:

    def __init__(self):
        # initialisiert Grafische Benutzeroberfläche
        self.root = tk.Tk()
        self.root.title("Pixi")
        self.root.config(bg="yellow")
        self.root.geometry("300x100+100+100")
        
        tk.Label(self.root, text="Pixi", fg="blue", bg="yellow", font="Georgia 48").pack()
        
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
        filename = askopenfilename()
        pixi.einlesen(filename)

    def speichern(self):
        # Speichert Datei unter gleichem Namen
        pass

    def speichern_unter(self):
        # Speichert Datei unter anderem Namen
        pass

    def plaintext(self):
        # zeigt Inhalt der Datei in Plaintext an
        pass

    def eigenschaften(self):
        # zeigt Inhalt der Datei gut erkennbar
        pass

    def spiegeln_x(self):
        # Spiegelt Bild an x-Achse
        pass

    def spiegeln_y(self):
        # Spiegelt Bild an y-Achse
        pass
    
    def invertieren(self):
        # invertiert Farben des Bilds
        pass

    def drehen_rechts(self):
        # Dreht Bild um 90 ° nach rechts
        pass

    def drehen_links(self):
        # dreht Bild um 90 ° nach links
        pass

    def hilfe(self):
        # zeigt Hilfetext an
        pass

    def about(self):
        # zeigt Informationen über das Programm an
        abouttext = """Copyright Lucas Herrenkind\nund Julius Bittner 2015"""
        about = tk.Tk()
        about.title("Über Pixi")
        about.geometry("300x300+500+100")

        tk.Label(about, text=abouttext, bg="yellow", font="Georgia 13").pack()
        tk.Button(about, text="Schließen", command=about.destroy).pack()

        about.mainloop()
        
pic = Gui()

