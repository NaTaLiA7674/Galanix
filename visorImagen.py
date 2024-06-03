import tkinter as tk
from tkinter import filedialog
from tkinter import Label
from PIL import Image, ImageTk

class VisorImagen:
    def __init__(self, root):
        self.root = root
        self.root.title("Visor de Imágenes")
        self.root.geometry("800x600")
        
        self.label = Label(root)
        self.label.pack()
        
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        
        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.open_image)
        file_menu.add_command(label="Salir", command=root.quit)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.resize((800, 600), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.label.config(image=img)
            self.label.image = img

if __name__ == "__main__":
    root = tk.Tk()
    viewer = VisorImagen(root)
    root.mainloop()
