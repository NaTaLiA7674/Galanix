import pygame
from tkinter import Tk, filedialog, Button

class MusicPlayer:
    def __init__(self):
        # Inicializar pygame
        pygame.mixer.init()

        # Crear la ventana principal
        self.root = Tk()
        self.root.title("Reproductor de Música")
        self.root.geometry("300x250")  # Ajustar el tamaño de la ventana

        # Configurar la ventana para que esté siempre en primer plano
        self.root.lift()
        self.root.call('wm', 'attributes', '.', '-topmost', '1')
        self.root.after_idle(self.root.call, 'wm', 'attributes', '.', '-topmost', '0')

        # Botones de control
        Button(self.root, text="Seleccionar Archivo", command=self.select_file).pack(pady=10)
        Button(self.root, text="Pausar", command=self.pause_music).pack(pady=10)
        Button(self.root, text="Reanudar", command=self.unpause_music).pack(pady=10)
        Button(self.root, text="Detener", command=self.stop_music).pack(pady=10)
        Button(self.root, text="Reiniciar", command=self.restart_music).pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3 *.wav")])
        if file_path:
            self.play_music(file_path)

    def play_music(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def restart_music(self):
        pygame.mixer.music.rewind()
        pygame.mixer.music.play()

    def run(self):
        self.root.mainloop()

# Esto es para probar que funcione si se ejecuta directamente
if __name__ == "__main__":
    player = MusicPlayer()
    player.run()
