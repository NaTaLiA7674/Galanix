import webbrowser
from Aplicacion import *

class Navegador(Aplicacion):
    def __init__(self):
        super().__init__("Navegador", [""])

    def ejecutar(self, ventana):
        ventana.lift()  # Traer la ventana principal al frente
        ventana.attributes('-topmost', True)  # Hacer que la ventana esté al frente
        ventana.after_idle(lambda: ventana.attributes('-topmost', False))  # Luego permitir que otras ventanas estén al frente
        url = "http://www.google.com"
        webbrowser.open(url)