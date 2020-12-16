import tkinter as Tk
from tkinter import messagebox
from tkinter import filedialog


# Definimos la raiz
raiz = Tk.Tk()
raiz.title("Clasificador leucemia")
raiz.iconbitmap("icon.ico")
raiz.config(bg="blue")


# raiz.geometry("640x480")

def info(adicional):
    if adicional == "Acerca de":
        messagebox.showinfo("Acerda de", "Clasificador de lecemia por davito")
    elif adicional == "Licencia":
        messagebox.showinfo("Licencia", "Producto bajo licencia GNU")
    elif adicional == "Manual":
        messagebox.showinfo("Manual", "1. Cargue una imagen \n2. presione el boton clasificar \n3. pulse guardar para \
        almacenar el resultado")


def archivo(op):
    if op == "abrir":
        fichero = filedialog.askopenfilename(title="Abrir", initialdir="./",
                                             filetypes=(("Todos los Archivos", "*.*"),
                                                        ("Archivos formato PNG", "*.png"),
                                                        ("Archivos formato JPG", "*.jpg")))
        print(fichero)
    elif op == "guardar como":
        filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                     filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        print(filename)
    elif op == "salir":
        valor = messagebox.askyesno("Salir", "¿Desea salir?")
        if valor:
            raiz.destroy()


# Definimos el frame que estará dentro de la raiz
frame = Tk.Frame(raiz, width=640, height=480)
frame.pack(fill="both", expand="True")

# barra menu
Barra_Menu = Tk.Menu(raiz)
raiz.config(menu=Barra_Menu)

file_menu = Tk.Menu(Barra_Menu, tearoff=0)
file_menu.add_command(label="abrir", command=lambda: archivo("abrir"))
file_menu.add_command(label="clasificar", command=lambda: archivo("clasi"))
file_menu.add_separator()
file_menu.add_command(label="Guardar", command=lambda: archivo("guardar"))
file_menu.add_command(label="Guardar como", command=lambda: archivo("guardar como"))
file_menu.add_separator()
file_menu.add_command(label="Salir", command=lambda: archivo("salir"))

help_menu = Tk.Menu(Barra_Menu, tearoff=0)
help_menu.add_command(label="Manual", command=lambda: info("Manual"))
help_menu.add_command(label="Licencia", command=lambda: info("Licencia"))
help_menu.add_command(label="Acerca de", command=lambda: info("Acerca de"))

Barra_Menu.add_cascade(label="Archivo", menu=file_menu)
Barra_Menu.add_cascade(label="ayuda", menu=help_menu)

raiz.mainloop()
