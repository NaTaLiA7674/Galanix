from Aplicacion import *
from navegador import *

class GestorAplicaciones:
    def __init__(self):
        self.aplicaciones = {
            "navegador": Navegador(),
            "juego": Juego(),
            "musica": ReproductorMusica(),
            "imagen": VisorImagen(),
            "video": VisorVideo(),
            "editor": EditorTexto()
        }

    def ejecutar_aplicacion(self, nombre, ventana=None):
        if nombre in self.aplicaciones:
            if ventana:
                self.aplicaciones[nombre].ejecutar(ventana)
            else:
                self.aplicaciones[nombre].ejecutar()

# Instancia del gestor
gestor = GestorAplicaciones()
