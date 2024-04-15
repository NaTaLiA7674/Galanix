import os

#Función para abrir el explorador de archivos en Windows
def abrir_explorador_archivos_windows():
    try:
        os.system("start explorer")

    except Exception as e:
        print("Error:", e)

