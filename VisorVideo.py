import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
from moviepy.editor import VideoFileClip
import threading

class VideoViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visor de Videos")
        self.root.geometry("800x600")

        self.label = tk.Label(root)
        self.label.pack()

        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.open_video)
        file_menu.add_command(label="Salir", command=root.quit)

        self.cap = None
        self.video_running = False
        self.audio_thread = None

    def open_video(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.video_clip = VideoFileClip(file_path)
            self.cap = cv2.VideoCapture(file_path)
            self.video_running = True
            self.play_video()

            # Reproduce el audio en un hilo separado
            self.audio_thread = threading.Thread(target=self.play_audio)
            self.audio_thread.start()

    def play_audio(self):
        self.video_clip.audio.preview()

    def play_video(self):
        if self.cap and self.video_running:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (800, 600))
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.label.imgtk = imgtk
                self.label.config(image=imgtk)
                self.root.after(10, self.play_video)
            else:
                self.cap.release()
                self.video_running = False

if __name__ == "__main__":
    root = tk.Tk()
    viewer = VideoViewer(root)
    root.mainloop()
