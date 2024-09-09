import tkinter as tk
from tkinter import messagebox
import subprocess
from tkinter import PhotoImage

def guardar_y_correr():
    try:
        matriz_x = int(entry_matriz_x.get())
        matriz_y = int(entry_matriz_y.get())

        if matriz_x < 1 or matriz_x > 10 or matriz_y < 1 or matriz_y > 10:
            messagebox.showerror("Error", "Los valores de las columnas y filas deben estar entre 1 y 10.")
            return

        if (matriz_x * matriz_y) % 2 != 0:
            messagebox.showerror("Error", "La multiplicación de filas y columnas debe ser un número par.")
            return

        with open("datos.txt", "w") as f:
            f.write(f"MatrizX={matriz_x}\n")
            f.write(f"MatrizY={matriz_y}\n")

        messagebox.showinfo("Datos guardados", "Los datos han sido guardados y se abrirá el juego.")

        subprocess.run(['python', 'memoria.py'])

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números enteros válidos para las matrices.")

def salir():
    ventana.destroy()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ingresar Matrices")
ventana.geometry("500x400")
ventana.resizable(False, False)

# Fondo personalizado (imagen)
try:
    fondo_photo = PhotoImage(file="./fondo1.png")
    fondo_label = tk.Label(ventana, image=fondo_photo)
    fondo_label.place(relwidth=1, relheight=1)
except Exception as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")

# Estilos
fuente_subtitulo = ("Arial", 16, "bold")
fuente_label = ("Arial", 12, "bold")
fuente_entry = ("Arial", 12)
fuente_botones = ("Arial", 10, "bold")

# Color de fondo de los widgets para que coincida con la imagen
bg_color = '#f0f0f0'  # Ajusta este color según sea necesario

# Subtítulo
subtitulo = tk.Label(ventana, text="Bienvenido al juego de memoria", bg='lightblue', font=fuente_subtitulo, fg='black')
subtitulo.pack(pady=10)

# Contenedor para los campos de entrada
entrada_frame = tk.Frame(ventana, bg='lightblue')
entrada_frame.pack(pady=20)

# Etiquetas y campos de entrada
label_matriz_x = tk.Label(entrada_frame, text="Ingresa número de Columnas:", bg='lightblue', font=fuente_label, fg='black')
label_matriz_x.grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_matriz_x = tk.Entry(entrada_frame, font=fuente_entry, borderwidth=1, bg=bg_color)
entry_matriz_x.grid(row=0, column=1, padx=10, pady=5)

label_matriz_y = tk.Label(entrada_frame, text="Ingresa Número de Filas:", bg='lightblue', font=fuente_label, fg='black')
label_matriz_y.grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_matriz_y = tk.Entry(entrada_frame, font=fuente_entry, borderwidth=1, bg=bg_color)
entry_matriz_y.grid(row=1, column=1, padx=10, pady=5)

# Contenedor para los botones
botones_frame = tk.Frame(ventana, bg='lightblue')
botones_frame.pack(pady=20)

# Botones
btn_correr = tk.Button(botones_frame, text="Correr", command=guardar_y_correr, font=fuente_botones, bg='#4CAF50', fg='white', relief='flat', bd=0)
btn_correr.pack(side='left', padx=10)

btn_salir = tk.Button(botones_frame, text="Salir", command=salir, font=fuente_botones, bg='#f44336', fg='white', relief='flat', bd=0)
btn_salir.pack(side='left', padx=10)

ventana.mainloop()
