# Graphical User Interface
# Pixi - Graphical Portable Pixelmap Editor
# Created by Julius Bittner 04.03.2015
# Last change 25.03.2015

import pixi
import tkinter as tk
import os
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.messagebox import showerror, showinfo

class Gui:

    def __init__(self):
        # initialisiert Grafische Benutzeroberfläche
        self.root = tk.Tk()
        self.root.title("Pixi")
        self.root.config(bg="red")
        self.root.geometry("400x100+100+100")
        self.filename = None # Dateiname für Bild
        self.namelabel = tk.Label(self.root, text=self.filename, bg="red", fg="white")
        self.bild = None
        
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
        dateimenu.add_command(label="Anzeigen", command=self.showpgm)
        dateimenu.add_command(label="Eigenschaften", command=self.eigenschaften)
        dateimenu.add_command(label="Dateiinhalt anzeigen",command=self.plaintext)
        dateimenu.add_separator()
        dateimenu.add_command(label="Beenden", command=self.root.destroy)

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
        #if self.bild.kopf[0][:2] != "P2":
        self.bild.einlesen(self.filename)

        self.namelabel.config(text=self.filename.split("/")[-1])
        self.namelabel.pack()
        showinfo("Pixi", "Datei eingelesen (%s)" % self.filename.split("/")[-1])

    def speichern(self):
        # Speichert Datei unter gleichem Namen
        if self.f1(): return
        self.bild.schreiben(self.filename)
        showinfo("Pixi", "Datei gespeichert (%s)" % self.filename.split("/")[-1])

    def speichern_unter(self):
        # Speichert Datei unter (anderem) Namen
        if self.f1(): return

        self.sfa = tk.Tk()
        self.sfa.title("Datei speichern unter")
        
        tk.Label(self.sfa, text="Dateiname:").pack()
        
        self.ausgabename = tk.Entry(self.sfa)
        self.ausgabename.insert(0, "ausgabe.pgm")
        self.ausgabename.pack()

        tk.Button(self.sfa, text="Hilfe", command=self.speichern_unter3).pack()
        tk.Button(self.sfa, text="Speichern", command=self.speichern_unter2).pack()
        self.sfa.mainloop()

    def speichern_unter2(self):
        # setzt Vorgang von speichern_unter fort
        self.filename = self.ausgabename.get()
        self.bild.schreiben(self.filename)
        self.sfa.destroy()

        showinfo("Pixi", "Datei gespeichert (%s)" % self.filename.split("/")[-1])

        self.namelabel.config(text=self.filename)
        self.namelabel.pack()

    def speichern_unter3(self):
        # Hilfe für das "Speichern unter"-Fenster
        sfa3 = tk.Tk()
        sfa3.title("Pixi")
        sfa3.config(bg="red")

        text = """In den Eintrag einfach Dateinamen eingeben, dann Enter drücken oder auf Speichern klicken.
Ordnerebene höher speichern: ../ für jeden Überordner eingeben.
Ordnerebene tiefer speichern: <Ordner>/ für jeden Unterordner eingeben."""

        tk.Label(sfa3, text=text).pack()
        tk.Button(sfa3, text="Schließen", command=sfa3.destroy).pack()

    def showpgm(self):
        # zeigt Bild an
        if self.f1(): return
        bildf = tk.Tk()
        bildf.title(self.filename)
        binname = "bin_" + self.filename.split("/")[-1]
        self.bild.binschreiben(binname)

        img = tk.PhotoImage(binname)
        tk.Label(bildf, image=img).pack()

        bildf.mainloop()

    def plaintext(self):
        # zeigt Inhalt der Datei in Plaintext an
        if self.f1(): return
        
        ptext = str()
        for i in self.bild.kopf: ptext += i
        for x in range(self.bild.hoehe):
            for y in range(self.bild.breite):
                px = self.bild.punktliste[x][y]
                if px == 0: space = 1
                else: space = 0
                grave = (space + 3 - int(px) % 10) * " "
                ptext += str(px) + " "
            ptext += "\n"

        textf = tk.Tk()
        textf.title(self.filename)
        textf.config(bg="red")

        tk.Label(textf, text=ptext, bg="red", font=('courier new', 10), fg="white").pack()
        tk.Button(textf, text="Schließen", command=textf.destroy).pack()
        
        cbb = tk.Button(textf, text="In Zwischenablage kopieren")
        cbb.bind("<Button>", lambda event:self.cb(ptext))
        cbb.pack()

        textf.mainloop()

    def eigenschaften(self):
        # zeigt Inhalt der Datei gut erkennbar
        if self.f1(): return
        name = self.filename
        typ = str(self.bild.kopf[0][:2])
        hoehe = str(self.bild.hoehe)
        breite = str(self.bild.breite)
        farbtiefe = str(self.bild.farbtiefe)
        kommentar = self.bild.kopf[1][2:-1]
        n = "\n"

        descs = {"2": "PGM: Portable Greymap, Graustufen",
                 "5": "PGM: Portable Greymap Binary, Graustufen"}
        desc = descs[self.bild.kopf[0][1]]

        eigf = tk.Tk()
        eigf.title(self.filename)
        eigf.config(bg="red")

        tk.Label(eigf, text="Dateiname:\nTyp:\n\nHöhe:\nBreite:\nFarbtiefe:\nKommentar:",
                 font="Georgia 13", fg="white", bg="red").pack(side="left")
        tk.Label(eigf, text=name+n+typ+n+desc+n+hoehe+n+breite+n+farbtiefe+n+kommentar,
                 font="Georgia 13", fg="white", bg="red").pack(side="right")

        eigf.mainloop()

    def spiegeln_x(self):
        # Spiegelt Bild an x-Achse
        if self.f1(): return
        self.bild.spiegelx()

    def spiegeln_y(self):
        # Spiegelt Bild an y-Achse
        if self.f1(): return
        self.bild.spiegely()
    
    def invertieren(self):
        # invertiert Farben des Bilds
        if self.f1(): return
        self.bild.invertieren()

    def drehen_rechts(self):
        # Dreht Bild um 90 ° nach rechts
        if self.f1(): return
        self.bild.drehen()

    def drehen_links(self):
        # dreht Bild um 90 ° nach links
        if self.f1(): return
        for i in range(3):
            self.bild.drehen()

    def hilfe(self):
        # zeigt Hilfetext an
        hilfetext = """Hallo, hier bekommst Du alle wichtigen Informationen zur Funktionsweise dieses Programms.
Wir hoffen, dass wir Dir helfen können, dieses Programm zu verstehen.

Unser Programm dient zur Verarbeitung von Bildern. Zuerst öffnest Du ein Graustufenbild, indem Du in der
Menüleiste auf „Datei" klickst und auf die Schaltfläche „Öffnen“ drückst. Nachdem Du ein Bild ausgesucht hast,
kannst Du dieses Bild auf verschiedene Weisen bearbeiten.

Klicke in der Menüleiste auf „Bearbeiten“ und Du siehst die Arbeitsschritte, die unser Programm anbietet.
Du kannst Dein Bild an der x- und y-Achse spiegeln lassen, das Bild nach links und rechts drehen und
die Farbwerte des Bildes invertieren: Aus weiß wird schwarz und ebenso umgekehrt.

Wenn Du erneut auf „Datei“ in der Menüleiste klickst, siehst Du die Felder „Speichern“ und „Speichern unter“.
Entweder überschreibst Du mit „Speichern“ dein altes Bild oder Du speicherst das geänderte Bild als neue Datei. Du kannst
Dir natürlich auch den Dateiinhalt und die Eigenschaften des Bildes anschauen.

Wir hoffen, dass wir Dir helfen konnten und wünschen einen angenehmen Gebrauch des PGM-Editors Pixi."""

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

Version 1.0rc1

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
           lambda event:os.startfile("http://mailto:content.legoag@gmail.com"))
    
        kont.pack()

        tk.Label(about, text="\nAktuelle Version:", bg="red", font="Georgia 13", fg="white").pack()
        link="https://github.com/Jubi72/Pixi.git"
        gitlink = tk.Label(about, text=link, bg="red", font="Georgia 13", fg="yellow")
        gitlink.bind("<Button>", lambda event:os.startfile(link))
        gitlink.pack()        
        tk.Button(about, text="Schließen", command=about.destroy).pack()

        about.mainloop()

    def f1(self):
        # wenn self.bild nicht existiert, wird Fehlermeldung ausgegeben
        if not self.bild:
            showerror("Fehler", "Bild existiert nicht.\nBitte ein Bild einlesen!")
            return True

    def cb(self, text):
        # kopiert Text in Zwischenablage
        cbf = tk.Tk()
        cbf.withdraw()
        cbf.clipboard_clear()
        cbf.clipboard_append(text)
        cbf.destroy()
        
pic = Gui()

