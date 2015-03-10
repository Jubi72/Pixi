# Graphical User Interface
# Pixi - Graphical Portable Pixelmap Editor
# Created by Julius Bittner 04.03.2015
# Last change 10.03.2015

import pixi
import tkinter as tk
from tkinter.filedialog import askopenfile

class Gui:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Pixi")
        
    def import(self):
        # liest Bild ein
        filename = askopenfilename()
        pixi.import(filename)