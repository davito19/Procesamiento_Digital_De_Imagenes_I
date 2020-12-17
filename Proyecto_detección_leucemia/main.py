# --------------------------------------------------------------------------
# ------- Clasificador de Leucemia Mieloide --------------------------------
# ------- Por: Manuela Restrepo  manuela.restrepoc@udea.edu.co -------------
# -------      CC 1152704892, Tel 3194707181,  Wpp 3194707181  -------------
# -------      David Vargas Bonett  odavid.vargas@udea.edu.co  -------------
# -------      CC 1036685469, Tel 3122505311,  Wpp 3122505311  -------------
# ------- Curso Básico de Procesamiento de Imágenes y Visión Artificial-----
# ------- V1 Diciembre de 2020----------------------------------------------
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# --1. Importando las librerias  -------------------------------------------
# --------------------------------------------------------------------------

import os  # Libreria paraa manejo de Sistema Operativo
import numpy as np  # Libreria numerica
import tkinter as Tk  # Libreria para diseño de interfaz graficas
from tkinter import messagebox  # Modulo para el despliegue de ventanas emergentes
from tkinter import filedialog  # Modulo para el despliegue de ventanas de archivos
from PIL import ImageTk, Image  # Modulos utilizados para procesar imagenes
from keras.preprocessing.image import load_img, img_to_array  # Modulos utilizados para procesar imagenes
from keras.models import load_model  # Modulo para cargar modelos de Deep Learning

# --------------------------------------------------------------------------
# -- 2. Definición de Variables Globales del juego   -----------------------
# --------------------------------------------------------------------------

# Variables del Modelo
model = os.getcwd() + "/Modelo/leucemiamodel.h5"  # Ruta donde se encuentran el modelo
height = os.getcwd() + "/Modelo/leucemiamodel.h5"  # Ruta donde se encuentran los pesos del modelo
cnn = load_model(model)  # Se carga el modelo en el objeto cnn
cnn.load_weights(height)  # Se asignan los pesos a cada neurona que conforma la red

# Variables para la interfaaz Grafica
# Definimos la raiz
raiz = Tk.Tk()  # Se construye el objeto raiz de la clase Tk
raiz.title("Clasificador leucemia")  # Se le asigna un nombre a la ventana
raiz.iconbitmap("icon.ico")  # Agregamos un icono
raiz.config(bg="blue")  # Definimos el background de la raiz
# Definimos el frame
frame = Tk.Frame(raiz, width=480, height=380)  # Se construye el frame que se va empaquetar en la ventana
frame.pack(fill="both", expand="True")  # Empaquetamps el frame en la ventana

# Variables Auxiliares
fichero = 'No.png'  # Ruta de la imagen a mostrar una vez inicie el programa


# --------------------------------------------------------------------------
# -- 3. Definición de funciones del juego   --------------------------------
# --------------------------------------------------------------------------

def clasificacion(path):
    size = (640, 480)

    x = load_img(path, target_size=size)
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = cnn.predict(x)
    result = array[0]
    print(result)
    if result == 0:
        print("pred: Leucemia")
        return True
    else:
        print("pred: Sanas")
        return False


def info(adicional):
    if adicional == "Acerca de":
        messagebox.showinfo("Acerda de", "Clasificador de lecemia por davito")
    elif adicional == "Licencia":
        messagebox.showinfo("Licencia", "Producto bajo licencia GNU")
    elif adicional == "Manual":
        messagebox.showinfo("Manual", "1. Cargue una imagen \n2. presione el boton clasificar \n3. pulse guardar para \
        almacenar el resultado")


def archivo(op):
    global mostrar
    global fichero

    if op == "abrir":
        fichero = filedialog.askopenfilename(title="Abrir", initialdir="./",
                                             filetypes=(("Todos los Archivos", "*.*"),
                                                        ("Archivos formato PNG", "*.png"),
                                                        ("Archivos formato JPG", "*.jpg")))
        print(fichero)
        mostrar = ImageTk.PhotoImage(Image.open(fichero).resize((240, 240)))
        mostrar_image.config(image=mostrar)

    elif op == "clasi":
        clasi = clasificacion(fichero)
        if clasi:
            resultado.config(text="Tenes leucemia")
        else:
            resultado.config(text="Estas sano")
    # elif op == "guardar como":
    #     filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
    #                                             filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    elif op == "salir":
        valor = messagebox.askyesno("Salir", "¿Desea salir?")
        if valor:
            raiz.destroy()


# Definimos el frame que estará dentro de la raiz


# -------------------------------barra menu--------------------------------- #
Barra_Menu = Tk.Menu(raiz)
raiz.config(menu=Barra_Menu)

file_menu = Tk.Menu(Barra_Menu, tearoff=0)
file_menu.add_command(label="abrir", command=lambda: archivo("abrir"))
file_menu.add_command(label="clasificar", command=lambda: archivo("clasi"))
# file_menu.add_separator()
# file_menu.add_command(label="Guardar", command=lambda: archivo("guardar"))
# file_menu.add_command(label="Guardar como", command=lambda: archivo("guardar como"))
file_menu.add_separator()
file_menu.add_command(label="Salir", command=lambda: archivo("salir"))

help_menu = Tk.Menu(Barra_Menu, tearoff=0)
help_menu.add_command(label="Manual", command=lambda: info("Manual"))
help_menu.add_command(label="Licencia", command=lambda: info("Licencia"))
help_menu.add_command(label="Acerca de", command=lambda: info("Acerca de"))

Barra_Menu.add_cascade(label="Archivo", menu=file_menu)
Barra_Menu.add_cascade(label="ayuda", menu=help_menu)
# ------------------------------------------------------------------------------ #

# -------------------------------Frame------------------------------------------ #
abrir = Tk.Button(frame, text="Abrir Archivo", command=lambda: archivo("abrir"))
abrir.config(padx=15, pady=10, justify="center")
abrir.place(x=10, y=10)

clasificar = Tk.Button(frame, text="Clasificar", command=lambda: archivo("clasi"))
clasificar.config(padx=15, pady=10, justify="center")
clasificar.place(x=160, y=10)

mostrar = ImageTk.PhotoImage(Image.open("No.png").resize((240, 240)))
mostrar_image = Tk.Label(frame, image=mostrar)
mostrar_image.place(x=10, y=100)

resultado = Tk.Label(frame, text='No se ha clasificado')
resultado.config(padx=15, pady=10, justify="center")
resultado.place(x=300, y=220)

raiz.mainloop()
