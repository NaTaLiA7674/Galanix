import tkinter as tk
from tkinter import filedialog, Text

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")
        self.text_area = Text(self.root, undo=True)
        self.text_area.pack(fill="both", expand=1)
        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Nuevo", command=self.new_file)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Deshacer", command=self.undo)
        edit_menu.add_command(label="Rehacer", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cortar", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copiar", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Pegar", command=lambda: self.text_area.event_generate("<<Paste>>"))

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def undo(self):
        try:
            self.text_area.edit_undo()
        except tk.TclError:
            pass

    def redo(self):
        try:
            self.text_area.edit_redo()
        except tk.TclError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
