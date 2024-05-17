import os
import mysql.connector

class Usuarios:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

    def crear_estructura_directorios(self):
        #Lista de nombre de archivos a crear
        directorios = [
            "Búsquedas", "Contactos", "Descargas", "Documentos", 
            "Escritorio", "Favoritos", "Imágenes", "Juegos guardados", 
            "LocalOneDrive", "Música", "Objetos 3D", "Vídeos", "Vínculos"
        ]

        #Ruta base para los directorios de usuario
        ruta_base = f"C:/Users/57311/Documents/Sistemas Operativos/Usuarios/{self.nombre}/"

        #Crear cada directorio
        for directorio in directorios:
            ruta_directorio = os.path.join(ruta_base, directorio)
            os.makedirs(ruta_directorio, exist_ok=True)

def guardar_usuario(usuario):
    #conexión a la base de datos
    connection = mysql.connector.connect(
        host="localhost",
        user = "root",
        password = "Nata20031712++",
        database = "galanix"
    )

    cursor = connection.cursor()

    #Insertar el usuario en la tabla correspondiente
    query = "INSERT INTO usuarios (nombre, contraseña) VALUES (%s, %s)"
    values = (usuario.nombre, usuario.contraseña)
    cursor.execute(query, values)

    #Hacer commit para aplicar los cambios
    connection.commit()

    #Crear la estructura de directorios para el usuario
    usuario.crear_estructura_directorios()

    