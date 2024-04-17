from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import tkinter.messagebox as messagebox
import datetime
from archivos import *
from calculadora import *

def login():
    global e2, formulario_frame
    clave = e2.get()
    if clave == "123":
        #Ocultar el formulario
        formulario_frame.lower()
        # Cargar la imagen sin desenfoque
        escritorio_interfaz()
        # Mostrar el footer
        mostrar_footer()
        #mostrar los widgets
        mostrar_widgets()
    else:
        messagebox.showerror(message="contraseña incorrecta", title="Error")

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
    global imagen_borrosa, logo, usuario_imagen, e2, fondo_label, formulario_frame

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

    # Cargar la imagen del usuario
    usuario = Image.open("imagenes/usuario.jpg")  
    usuario = usuario.resize((200, 200), Image.ANTIALIAS)

    # Convertir la imagen a formato ImageTk
    usuario_imagen = ImageTk.PhotoImage(usuario)

    # Crear un widget Label para mostrar la imagen de usuario
    usuario_label = Label(formulario_frame, image=usuario_imagen, highlightthickness=3, highlightbackground="#272829")
    usuario_label.grid(row=1, column=1, padx=70, pady=20)

    # Mensaje de bienvenida en el centro de la pantalla
    mensaje_bienvenida = Label(formulario_frame, text="¡Bienvenida, Natalia!", font=("Berlin Sans FB", 16), bg="#D8D9DA")
    mensaje_bienvenida.grid(row=2, column=1, pady=10)

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
    global archivos_ventana, google_ventana, calculadora_ventana  
   
    # Agregar un espacio para mostrar archivos en el escritorio
    imagen_archivos = Image.open("imagenes/archivos.jpg")
    imagen_archivos = imagen_archivos.resize((60, 60), Image.ANTIALIAS)
    archivos_ventana = ImageTk.PhotoImage(imagen_archivos)
    archivos_boton = Button(ventana, image=archivos_ventana, text='Archivos', bg="#61677A", compound="top", fg="white", command=abrir_explorador_archivos_windows)
    archivos_boton.place(x=50, y=530)

    # Agregar un espacio para abrir el navegador google
    imagen_google = Image.open("imagenes/google.jpg")
    imagen_google = imagen_google.resize((60, 60), Image.ANTIALIAS)
    google_ventana = ImageTk.PhotoImage(imagen_google)
    google_boton = Button(ventana, image=google_ventana, text='Google', bg="#61677A", compound="top", fg="white")
    google_boton.place(x=50, y=410)

    #Agregar un espacio para abrir la calculadora científica
    imagen_calculadora = Image.open("imagenes/calculadora.jpg")
    imagen_calculadora = imagen_calculadora.resize((60, 60), Image.ANTIALIAS)
    calculadora_ventana = ImageTk.PhotoImage(imagen_calculadora)
    calculadora_boton = Button(ventana, image=calculadora_ventana, text='Calculadora', bg="#61677A", compound="top", fg="white", command=open_calculator)
    calculadora_boton.place(x=50, y=290)
   

# Ejecutar la ventana
pantallaPrincipal()
ventana.mainloop()

