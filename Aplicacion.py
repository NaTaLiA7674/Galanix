import subprocess
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter, ImageDraw
import datetime

class Aplicacion:
    def __init__(self, nombre, comando):
        self.nombre = nombre
        self.comando = comando

    def ejecutar(self):
        subprocess.run(self.comando, shell=True)

# Clases específicas para cada aplicación
class Juego(Aplicacion):
    def __init__(self):
        super().__init__("Juego", ["python", "juego.py"])

class ReproductorMusica(Aplicacion):
    def __init__(self):
        super().__init__("Reproductor de Música", ["python", "reproductorMusica.py"])

class VisorImagen(Aplicacion):
    def __init__(self):
        super().__init__("Visor de Imágenes", ["python", "visorImagen.py"])

class VisorVideo(Aplicacion):
    def __init__(self):
        super().__init__("Visor de Videos", ["python", "VisorVideo.py"])

class EditorTexto(Aplicacion):
    def __init__(self):
        super().__init__("Editor de Texto", ["python", "EditorTexto.py"])
