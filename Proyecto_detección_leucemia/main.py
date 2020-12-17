import tkinter as Tk
from tkinter import messagebox
from tkinter import filedialog
"""
import os
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

size = (640, 480)
model = os.getcwd() + "/Modelo/leucemiamodel.h5"
height = os.getcwd() + "/Modelo/leucemiamodel.h5"
cnn = load_model(model)
cnn.load_weights(height)

file1 = os.getcwd() + '/Data/Validacion/sanas/BloodImage_00340.jpg'
file0 = os.getcwd() + '/Data/Validacion/leucemia/FB_IMG_1582862764903.jpg'
x = load_img(file1, target_size=size)
x = img_to_array(x)
x = np.expand_dims(x, axis=0)
array = cnn.predict(x)
result = array[0]
print(result)icon.ico
if result == 0:
    print("pred: Leucemia")
else:
    print("pred: Sanas")
"""

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

abrir = Tk.Button(frame, text="Abrir Archivo", command=lambda :archivo("abrir"))
abrir.config(padx=15, pady=10, justify="center")
abrir.grid(row=0,column=0)

raiz.mainloop()
"""

import tensorflow as tf
tf.config.experimental.list_physical_devices('GPU')
"""