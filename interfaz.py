from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import tkinter.messagebox as messagebox
import datetime
from archivos import *
from calculadora import *
from usuarios import *
from tkinter import simpledialog
import bcrypt
from juego import *
import subprocess
from reproductorMusica import *
from visorImagen import *
from VisorVideo import *
from EditorTexto import *

def iniciar_juego():
    subprocess.run(["python", "juego.py"])

def iniciar_reproductor():
    subprocess.run(["python", "reproductorMusica.py"])

def iniciar_visorImagen():
    subprocess.run(["python", "visorImagen.py"])

def iniciar_visorVideo():
    subprocess.run(["python", "VisorVideo.py"])

def iniciar_editorTexto():
    subprocess.run(["python", "EditorTexto.py"])

def validar_usuario(nombre, contraseña):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nata20031712++",
        database="galanix"
    )
    cursor = connection.cursor()
    query = "SELECT * FROM usuarios WHERE nombre = %s AND contraseña = %s"
    values = (nombre, contraseña)
    cursor.execute(query, values)
    resultado = cursor.fetchone()
    cursor.close()
    connection.close()
    return resultado is not None

def login():
    global e1, e2, formulario_frame
    nombre = e1.get()
    clave = e2.get()
    if validar_usuario(nombre, clave):
        formulario_frame.lower()
        escritorio_interfaz()
        mostrar_footer()
        mostrar_widgets()
    else:
        messagebox.showerror(message="Contraseña incorrecta", title="Error")

ventana = Tk()
ventana.title("Galanix")

# Tamaño de la pantalla completo que sea de toda la pantalla
ancho = ventana.winfo_screenwidth()  # Obtiene el ancho de la pantalla del usuario 
alto = ventana.winfo_screenheight()  # Obtiene el alto de la pantalla del usuario

# Margen para dejar espacio para la barra de tareas
margen = 30

# Tamaño de la ventana teniendo en cuenta el margen
ventana.geometry("%dx%d+0+0" % (ancho, alto - margen))
ventana.resizable(0, 0)

#FUNCIONES PARA LA PANTALLA PRINCIPAL

def pantallaPrincipal():
    global imagen_borrosa, logo, usuario_imagen, e2, e1, fondo_label, formulario_frame

    # Eliminar el footer si ya existe
    if 'footer_frame' in globals():
        footer_frame.destroy()

    # Cargar la imagen y aplicar el filtro de desenfoque
    imagen = Image.open("imagenes/fondo.jpg")
    imagen = imagen.filter(ImageFilter.GaussianBlur(10)) 
    imagen = imagen.resize((ancho, alto - margen), Image.ANTIALIAS)
    imagen_borrosa = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen de fondo borrosa
    fondo_label = Label(ventana, image=imagen_borrosa)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Cargar la imagen del logo
    imagen_logo = Image.open("imagenes/logo.jpg")  
    imagen_logo = imagen_logo.resize((40, 40), Image.ANTIALIAS)

    # Crear una máscara redonda
    mask = Image.new("L", (40, 40), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 40, 40), fill=255)

    # Aplicar la máscara a la imagen del logo
    imagen_logo.putalpha(mask)

    # Convertir la imagen a formato ImageTk
    logo = ImageTk.PhotoImage(imagen_logo)

    # Agregar un Label para mostrar la imagen del logo
    logo_label = Label(ventana, image=logo, bg="#272829").place(x=10, y=10)

    # Agregar un Label para el texto "Galanix"
    label_galanix = Label(ventana, text="Galanix", font=("Arial", 20), bg="#272829", fg="white")
    label_galanix.place(x=60, y=15)

    # Crear un frame para el formulario
    formulario_frame = Frame(ventana, bg="#D8D9DA", width=400, height=400, highlightthickness=5, highlightbackground="#272829")
    formulario_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Función para crear un usuario
    def crear_usuario():
        # Función para abrir la ventana emergente y crear el usuario
        dialog = tk.Toplevel()
        dialog.title("Crear Usuario")
        dialog.geometry("400x200")  # Tamaño de la ventana emergente

        # Obtener el tamaño de la pantalla y de la ventana emergente
        ancho_pantalla = dialog.winfo_screenwidth()
        alto_pantalla = dialog.winfo_screenheight()
        ancho_ventana = 400
        alto_ventana = 200

        # Calcular la posición para centrar la ventana
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        dialog.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Crear un marco centrado dentro de la ventana emergente
        frame = tk.Frame(dialog)
        frame.pack(expand=True)

        tk.Label(frame, text="Nombre de usuario:").grid(row=0, column=0, padx=10, pady=5)
        entry_nombre = tk.Entry(frame)
        entry_nombre.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(frame, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5)
        entry_contrasena = tk.Entry(frame, show='*')
        entry_contrasena.grid(row=1, column=1, padx=10, pady=5)
        
        def confirmar():
            nombre = entry_nombre.get()
            contrasena = entry_contrasena.get()
            if nombre and contrasena:
                nuevo_usuario = Usuarios(nombre, contrasena)
                guardar_usuario(nuevo_usuario)
                messagebox.showinfo("Éxito", "Usuario creado correctamente.")
                dialog.destroy()
            else:
                messagebox.showwarning("Advertencia", "Por favor, ingrese nombre de usuario y contraseña.")
        
        tk.Button(frame, text="Confirmar", command=confirmar).grid(row=2, column=0, columnspan=2, pady=10)
        
        dialog.transient(ventana)
        dialog.grab_set()
        ventana.wait_window(dialog)

    #Crear un botón para crear un usuario en la parte superior derecha de la ventana
    b2 = Button(ventana, text="Crear Usuario", font=("Berlin Sans FB", 14), bg="#61677A", borderwidth=0, highlightthickness=0, fg="white", command=crear_usuario)
    b2.place(x=ancho-150, y=20)

    # Cargar la imagen del usuario
    usuario = Image.open("imagenes/usuario.jpg")  
    usuario = usuario.resize((200, 200), Image.ANTIALIAS)

    # Convertir la imagen a formato ImageTk
    usuario_imagen = ImageTk.PhotoImage(usuario)

    # Crear un widget Label para mostrar la imagen de usuario
    usuario_label = Label(formulario_frame, image=usuario_imagen, highlightthickness=3, highlightbackground="#272829")
    usuario_label.grid(row=1, column=1, padx=70, pady=20)

    def on_entry_click2(event):
        if e1.get() == '  Usuario':
            e1.delete(0, "end")

    def on_entry_click(event):
        if e2.get() == '  Contraseña':
            e2.delete(0, "end")
            e2.config(show="*")

    def on_focus_out(event):
        if not e2.get():
            e2.insert(0, '  Contraseña')
            e2.config(show="")
            ventana.focus_set()

    def reset_entry(event):
        if e2.get() == '':
            e2.insert(0, '  Contraseña')
            e2.config(show="")
            ventana.focus_set()  # Cambiar el foco a la ventana para ocultar el cursor

    # Crear una casilla para ingresar el usuario
    e1 = Entry(formulario_frame, font=("Berlin Sans FB", 11), fg='gray', highlightthickness=2, highlightbackground="#272829")
    e1.insert(0, '  Usuario')
    e1.grid(row=2, column=1, padx=10, pady=10, ipady=10, ipadx=40)
    e1.bind('<FocusIn>', on_entry_click2)

    e2 = Entry(formulario_frame, font=("Berlin Sans FB", 11), fg='gray', show="", highlightthickness=2, highlightbackground="#272829")
    e2.insert(0, '  Contraseña')
    e2.bind('<FocusIn>', on_entry_click)
    e2.bind('<FocusOut>', on_focus_out)
    e2.grid(row=3, column=1, padx=10, pady=10, ipady=10, ipadx=40)

    ventana.bind('<Button-1>', reset_entry)  # Detecta clics en cualquier lugar de la ventana

    b1 = Button(formulario_frame, text="Iniciar Sesión", font=("Berlin Sans FB", 14), command=login, bg="#61677A", borderwidth=0, highlightthickness=0, fg="white")
    b1.grid(row=4, column=1, padx=10, pady=20, ipadx=60, ipady=5)

    def on_enter(event):
        b1.config(bg="#272829", cursor="hand2")

    def on_leave(event):
        b1.config(bg="#61677A", cursor="")

    b1.bind("<Enter>", on_enter)
    b1.bind("<Leave>", on_leave)


# FUNCIONES PARA EL ESCRITORIO

# Función para organizar el escritorio
def escritorio_interfaz():
    global fondo_label, imagen_clara, archivos
    fondo_label.configure(image=imagen_clara)
    fondo_label.image = imagen_clara

# Cargar la imagen sin desenfoque
imagen_clara = Image.open("imagenes/fondo.jpg")
imagen_clara = imagen_clara.resize((ancho, alto - margen), Image.ANTIALIAS)
imagen_clara = ImageTk.PhotoImage(imagen_clara)

def mostrar_footer():
    global salir, archivos, google, label_footer, calculadora, footer_frame  # Agregar referencias globales

    footer_frame = Frame(ventana, bg="#61677A", width=ancho, height=50)
    footer_frame.pack(side=BOTTOM, fill=X)

    # Agregar un Label para el footer
    label_footer = Label(footer_frame, bg="#61677A", fg="white")
    label_footer.pack(side=RIGHT, pady=10, padx=20)
    actualizar_hora(label_footer)  # Llamar a la función para actualizar la hora

    # Agregar un botón para cerrar sesión, que muestre el formulario y sea un ícono
    imagen_salir = Image.open("imagenes/salir.jpg")
    imagen_salir = imagen_salir.resize((30, 30), Image.ANTIALIAS)
    salir = ImageTk.PhotoImage(imagen_salir)
    salir_boton = Button(footer_frame, image=salir, bg="#61677A", command=pantallaPrincipal)
    salir_boton.pack(side=LEFT, pady=10, padx=10)

    # Agregar otro ícono para archivos
    imagen_archivos = Image.open("imagenes/archivos.jpg")
    imagen_archivos = imagen_archivos.resize((30, 30), Image.ANTIALIAS)
    archivos = ImageTk.PhotoImage(imagen_archivos)
    archivos_boton = Button(footer_frame, image=archivos, bg="#61677A", command=abrir_explorador_archivos_windows)
    archivos_boton.pack(side=LEFT, pady=10, padx=10)

    # Agregar otro ícono para el navegador google
    imagen_google = Image.open("imagenes/google.jpg")
    imagen_google = imagen_google.resize((30, 30), Image.ANTIALIAS)
    google = ImageTk.PhotoImage(imagen_google)
    google_boton = Button(footer_frame, image=google, bg="#61677A")
    google_boton.pack(side=LEFT, pady=10, padx=10)

    # Agregar un botón para abrir la calculadora
    imagen_calculadora = Image.open("imagenes/calculadora.jpg")
    imagen_calculadora = imagen_calculadora.resize((30, 30), Image.ANTIALIAS)
    calculadora = ImageTk.PhotoImage(imagen_calculadora)
    calculadora_boton = Button(footer_frame, image=calculadora, bg="#61677A", command=open_calculator)
    calculadora_boton.pack(side=LEFT, pady=10, padx=10)

# Función para actualizar la hora actual
def actualizar_hora(label_footer):
    ahora = datetime.datetime.now().strftime("%H:%M:%S")
    label_footer.config(text=ahora)
    ventana.update()  # Forzar la actualización de la ventana
    label_footer.after(1000, lambda: actualizar_hora(label_footer))  # Actualiza cada segundo

# Función para mostrar los widgets en el escritorio
def mostrar_widgets():
    global archivos_ventana, google_ventana, calculadora_ventana, juego_ventana, musica_ventana, imagen_ventana, video_ventana, editor_ventana
   
    # Agregar un espacio para mostrar archivos en el escritorio
    imagen_archivos = Image.open("imagenes/archivos.jpg")
    imagen_archivos = imagen_archivos.resize((50, 50), Image.ANTIALIAS)
    archivos_ventana = ImageTk.PhotoImage(imagen_archivos)
    archivos_boton = Button(ventana, image=archivos_ventana, text='Archivos', bg="#61677A", compound="top", fg="white", command=abrir_explorador_archivos_windows)
    archivos_boton.place(x=50, y=530)

    # Agregar un espacio para abrir el navegador google
    imagen_google = Image.open("imagenes/google.jpg")
    imagen_google = imagen_google.resize((50, 50), Image.ANTIALIAS)
    google_ventana = ImageTk.PhotoImage(imagen_google)
    google_boton = Button(ventana, image=google_ventana, text='Google', bg="#61677A", compound="top", fg="white")
    google_boton.place(x=50, y=430)

    #Agregar un espacio para abrir la calculadora científica
    imagen_calculadora = Image.open("imagenes/calculadora.jpg")
    imagen_calculadora = imagen_calculadora.resize((50, 50), Image.ANTIALIAS)
    calculadora_ventana = ImageTk.PhotoImage(imagen_calculadora)
    calculadora_boton = Button(ventana, image=calculadora_ventana, text='Calculadora', bg="#61677A", compound="top", fg="white", command=open_calculator)
    calculadora_boton.place(x=50, y=330)

    #Agregar un espacio para abrir el juego de la serpiente
    imagen_juego = Image.open("imagenes/culebrita.webp")
    imagen_juego = imagen_juego.resize((50, 50), Image.ANTIALIAS)
    juego_ventana = ImageTk.PhotoImage(imagen_juego)
    juego_boton = Button(ventana, image=juego_ventana, text='Juego', bg="#61677A", compound="top", fg="white", command=iniciar_juego)
    juego_boton.place(x=50, y=230)

    #Agregar un espacio para abrir el reproductor de música
    imagen_musica = Image.open("imagenes/musica.jpg")
    imagen_musica = imagen_musica.resize((50, 50), Image.ANTIALIAS)
    musica_ventana = ImageTk.PhotoImage(imagen_musica)
    musica_boton = Button(ventana, image=musica_ventana, text='Música', bg="#61677A", compound="top", fg="white", command=iniciar_reproductor)
    musica_boton.place(x=50, y=130)

    #Agregar un espacio para abrir el visor de imágenes
    imagen_imagen = Image.open("imagenes/Imagen.webp")
    imagen_imagen = imagen_imagen.resize((50, 50), Image.ANTIALIAS)
    imagen_ventana = ImageTk.PhotoImage(imagen_imagen)
    imagen_boton = Button(ventana, image=imagen_ventana, text='Imagen', bg="#61677A", compound="top", fg="white", command=iniciar_visorImagen)
    imagen_boton.place(x=150, y=130)

    #Agregar un espacio para abrir el visor de videos
    imagen_video = Image.open("imagenes/video.webp")
    imagen_video = imagen_video.resize((50, 50), Image.ANTIALIAS)
    video_ventana = ImageTk.PhotoImage(imagen_video)
    video_boton = Button(ventana, image=video_ventana, text='Video', bg="#61677A", compound="top", fg="white", command=iniciar_visorVideo)
    video_boton.place(x=150, y=230)

    #Agregar un espacio para abrir el editor de texto
    imagen_editor = Image.open("imagenes/editor.webp")
    imagen_editor = imagen_editor.resize((50, 50), Image.ANTIALIAS)
    editor_ventana = ImageTk.PhotoImage(imagen_editor)
    editor_boton = Button(ventana, image=editor_ventana, text='Editor', bg="#61677A", compound="top", fg="white", command=iniciar_editorTexto)
    editor_boton.place(x=150, y=330)
   

# Ejecutar la ventana
pantallaPrincipal()
ventana.mainloop()

