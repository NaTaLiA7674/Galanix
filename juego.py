import tkinter as tk
import random
import tkinter.messagebox

class JuegoCulebrita(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Juego de la culebrita")
        self.canvas = tk.Canvas(self, width=500, height=600, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.filas = 18
        self.columnas = 18
        self.ancho_celda = 500 / self.columnas
        self.alto_celda = 500 / self.filas
        self.comida = None
        self.serpiente = [(0, 0)]
        self.direccion = "Right"
        self.contador_comida = 0  # Variable para contar la cantidad de comida
        self.puntuacion_maxima = self.cargar_puntuacion_maxima()  # Cargar puntuación máxima
        self.dibujar_celdas()
        self.dibujar_serpiente()
        self.generar_comida()
        self.mover_serpiente()
        self.mostrar_contador_comida()  # Llama a la función para mostrar el contador de comida

        # Configurar cierre de ventana
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

    def cargar_puntuacion_maxima(self):
        try:
            with open("puntuacion_maxima.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def cerrar_ventana(self):
        self.puntuacion_maxima = 0  # Reinicia la puntuación máxima antes de cerrar la ventana
        self.destroy()


    def dibujar_celdas(self):
        for column in range(self.columnas):
            for row in range(self.filas):
                x1 = column * self.ancho_celda
                y1 = row * self.alto_celda
                x2 = x1 + self.ancho_celda
                y2 = y1 + self.alto_celda
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags="celda")

    def dibujar_serpiente(self):
        self.canvas.delete("serpiente")
        for segmento in self.serpiente:
            x, y = segmento
            x1 = x * self.ancho_celda
            y1 = y * self.alto_celda
            x2 = x1 + self.ancho_celda
            y2 = y1 + self.alto_celda
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", tags="serpiente")

    def generar_comida(self):
        while True:
            comida_x = random.randint(0, self.columnas - 1)
            comida_y = random.randint(0, self.filas - 1)
            if (comida_x, comida_y) not in self.serpiente:
                break

        x1 = comida_x * self.ancho_celda
        y1 = comida_y * self.alto_celda
        x2 = x1 + self.ancho_celda
        y2 = y1 + self.alto_celda
        self.comida = self.canvas.create_oval(x1, y1, x2, y2, fill="red", tags="comida")

    def mover_serpiente(self):
        cabeza = self.serpiente[-1]
        nueva_cabeza = cabeza
        if self.direccion == "Up":
            nueva_cabeza = (cabeza[0], cabeza[1] - 1)
        elif self.direccion == "Down":
            nueva_cabeza = (cabeza[0], cabeza[1] + 1)
        elif self.direccion == "Left":
            nueva_cabeza = (cabeza[0] - 1, cabeza[1])
        elif self.direccion == "Right":
            nueva_cabeza = (cabeza[0] + 1, cabeza[1])

        # Verificar colisión con los bordes de la ventana
        if (nueva_cabeza[0] < 0 or nueva_cabeza[0] >= self.columnas or
                nueva_cabeza[1] < 0 or nueva_cabeza[1] >= self.filas):
            self.mostrar_mensaje_perdida()
            return

        # Verificar colisión consigo misma
        if nueva_cabeza in self.serpiente[:-1]:
            self.mostrar_mensaje_perdida()
            return

        self.serpiente.append(nueva_cabeza)
        self.dibujar_serpiente()
        if nueva_cabeza == self.obtener_posicion_comida():
            self.canvas.delete(self.comida)
            self.generar_comida()
            self.contador_comida += 1
            if self.contador_comida > self.puntuacion_maxima:  # Actualizar puntuación máxima si es necesario
                self.puntuacion_maxima = self.contador_comida
            self.mostrar_contador_comida()
        else:
            self.serpiente.pop(0)
        self.after(100, self.mover_serpiente)

    def mostrar_mensaje_perdida(self):
        mensaje = tk.messagebox.askyesno("¡Perdiste!", f"Tu puntaje final fue: {self.contador_comida}. ¿Quieres jugar de nuevo?")
        if mensaje:
            # Si el usuario quiere jugar de nuevo, reinicia el juego
            self.reiniciar_juego()
        else:
            # Si el usuario no quiere jugar de nuevo, cierra la ventana
            self.quit()

    def reiniciar_juego(self):
        # Reinicia todas las variables del juego
        self.canvas.delete("all")
        self.serpiente = [(0, 0)]
        self.direccion = "Right"
        self.contador_comida = 0
        self.dibujar_celdas()
        self.dibujar_serpiente()
        self.generar_comida()
        self.mostrar_contador_comida()
        # Vuelve a iniciar el movimiento de la serpiente
        self.mover_serpiente()

    def obtener_posicion_comida(self):
        pos = self.canvas.coords(self.comida)
        comida_x = int(pos[0] / self.ancho_celda)
        comida_y = int(pos[1] / self.alto_celda)
        return (comida_x, comida_y)

    def cambiar_direccion(self, event):
        nueva_direccion = event.keysym
        if nueva_direccion in ["Up", "Down", "Left", "Right"]:
            self.direccion = nueva_direccion

    def mostrar_contador_comida(self):
        # Borra el contador de comida anterior
        self.canvas.delete("contador_comida")
        # Muestra el nuevo contador de comida en la parte inferior de la ventana
        texto_x = 250 # Centra el texto en el eje x
        texto_y = 550 # Posiciona el texto en la parte inferior de la ventana
        self.canvas.create_text(texto_x, texto_y, text=f"Puntaje: {self.contador_comida}   Puntaje Máximo: {self.puntuacion_maxima}", fill="black", font=("Arial", 12), tags="contador_comida")

if __name__ == "__main__":
    juego = JuegoCulebrita()
    juego.bind("<KeyPress>", juego.cambiar_direccion)
    juego.mainloop()

