import tkinter as tk
from tkinter import ttk
from clase_MonteCarlo import montecarlo


def ejecutar():
    # Limpiar todos los mensajes antes de validar
    mensaje_a.config(text="")
    mensaje_b.config(text="")
    mensaje_k.config(text="")
    mensaje_n.config(text="")
    mensaje_v.config(text="")


    a = int(entry_a.get())
    b = int(entry_b.get())
    k = int(entry_k.get())
    n = int(entry_n.get())
    v = int(entry_v.get())

    errores = False  # banderita para detectar errores

    
    if b < a:
        mensaje_a.config(text="b debe ser mayor que a")
        errores = True

    if k <= 0:
        mensaje_k.config(text="k debe ser mayor que 0")
        errores = True
    
    elif isinstance(k, float):
        mensaje_k.config(text="k debe un numero entero")
        errores = True

    if n <= 0:
        mensaje_k.config(text="n debe ser mayor que 0")
        errores = True
    
    elif isinstance(k, float):
        mensaje_k.config(text="n debe un numero entero")
        errores = True

    if v <= 0:
        mensaje_k.config(text="v debe ser mayor que 0")
        errores = True
        
    elif isinstance(v, float):
        mensaje_k.config(text="v debe un numero entero")
        errores = True

    print(errores)
    
    if not errores:
        mc = montecarlo(a,b,n,k,v)
        mc.CalcularSumatoriaUnificada()
        estadistico_final, promedio, desviacion_estandar = mc.calcular_estadisticas()

        prom.config(text = f"Promedio: {promedio}")
        stdev.config(text = f"Desviación Estandar: {desviacion_estandar}")
        estad_f.config(text = f"Estadistico Final: {estadistico_final}")






# --- Interfaz Tkinter ---
root = tk.Tk()
root.title("Simulación de Monte Carlo")
root.geometry("380x350")
root.config(padx=20, pady=20)

tk.Label(root, text="Simulación de Monte Carlo", font=("Arial", 12, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

# --- Entrada a ---
tk.Label(frame, text="A (Limite Inferior)").grid(row=0, column=0, sticky="e", pady=5)
entry_a = tk.Entry(frame)
entry_a.grid(row=0, column=1)
mensaje_a = tk.Label(frame, text="", fg="red", font=("Arial", 10))
mensaje_a.grid(row=1, column=0, columnspan=2)

# --- Entrada c ---
tk.Label(frame, text="B (Limite Superior)").grid(row=2, column=0, sticky="e", pady=5)
entry_b = tk.Entry(frame)
entry_b.grid(row=2, column=1)
mensaje_b = tk.Label(frame, text="", fg="red", font=("Arial", 10))
mensaje_b.grid(row=3, column=0, columnspan=2)

# --- Entrada m ---
tk.Label(frame, text="k (Índice de selección)").grid(row=4, column=0, sticky="e", pady=5)
entry_k = tk.Entry(frame)
entry_k.grid(row=4, column=1)
mensaje_k = tk.Label(frame, text="", fg="red", font=("Arial", 10))
mensaje_k.grid(row=5, column=0, columnspan=2)

tk.Label(frame, text="n (Tamaño de la muestra)").grid(row=6, column=0, sticky="e", pady=5)
entry_n = tk.Entry(frame)
entry_n.grid(row=6, column=1)
mensaje_n = tk.Label(frame, text="", fg="red", font=("Arial", 10))
mensaje_n.grid(row=7, column=0, columnspan=2)

# --- Entrada semilla X0 ---
tk.Label(frame, text="v (cantidad de variables)").grid(row=8, column=0, sticky="e", pady=5)
entry_v = tk.Entry(frame)
entry_v.grid(row=8, column=1)
mensaje_v = tk.Label(frame, text="", fg="red", font=("Arial", 10))
mensaje_v.grid(row=9, column=0, columnspan=2)


# --- Botón ---
tk.Button(root, text="Validar", command=ejecutar, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=15)

# Frame para la tabla y scroll
frame_tabla = tk.Frame(root)
frame_tabla.pack(pady=10)  # se puede pack porque es un nuevo frame

prom = tk.Label(frame_tabla, text=f"", font=("Arial", 12))
prom.pack(pady=5)

stdev = tk.Label(frame_tabla, text=f"", font=("Arial", 12))
stdev.pack(pady=5)

estad_f = tk.Label(frame_tabla, text=f"", font=("Arial", 12))
estad_f.pack(pady=5)



root.mainloop()
