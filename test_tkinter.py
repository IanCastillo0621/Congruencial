import tkinter as tk
from tkinter import ttk
from clase_congruencial import congruencial

def mcd(a, b):
    """Calcula el máximo común divisor (Euclides)."""
    while b:
        a, b = b, a % b
    return a

def factores_primos(n):
    """Devuelve los factores primos de un número."""
    factores = set()
    i = 2
    while i * i <= n:
        while n % i == 0:
            factores.add(i)
            n //= i
        i += 1
    if n > 1:
        factores.add(n)
    return factores

def ejecutar():
    # Limpiar todos los mensajes antes de validar
    mensaje_a.config(text="")
    mensaje_c.config(text="")
    mensaje_m.config(text="")
    mensaje_x0.config(text="")
    mensaje_enteros.config(text="")

    try:
        a = int(entry_a.get())
        c = int(entry_c.get())
        m = int(entry_m.get())
        x0 = int(entry_x0.get())

        errores = False  # banderita para detectar errores

        # Validación de m
        if m <= 0:
            mensaje_m.config(text="m debe ser mayor que 0")
            errores = True

        # Validación de a
        if a < 0 or a >= m:
            mensaje_a.config(text=f"Se debe cumplir que 0 < a < {m}")
            errores = True

        # Validación de c
        if c < 0 or c >= m:
            mensaje_c.config(text=f"Se debe cumlir que 0 < c < {m}")
            errores = True

        # Validación de semilla
        if x0 <= 0 or x0 >= m:
            mensaje_x0.config(text=f"Se debe cumplir que 0 < X₀ < {m}")
            errores = True

        # Si hubo errores de entrada, no continuar
        if errores:
            return

        if mcd(c, m) != 1:
            mensaje_c.config(text="c y m no son primos relativos")
            errores = True

        factores = factores_primos(m)
        for p in factores:
            if (a - 1) % p != 0:
                mensaje_a.config(text=f"a - 1 no es múltiplo de {p}")
                errores = True
        
        if m%4 == 0 and (a-1)%4 != 0:
            mensaje_m.config(text= f"a-1 debe ser un mútiplo de 4 dado que m es multiplo de 4")
            errores = True


    except ValueError:
        mensaje_enteros.config(text="Ingresa valores enteros en todos los campos")
        errores = True
    
    if not errores:
        con = congruencial(x0,a,c,m)
        resultado = con.generar_congruencial()

        for i in resultado:
            tree.insert("", tk.END, values=(i,))
        
        label_cantidad.config(text=f"Cantidad: {len(resultado)}")





# --- Interfaz Tkinter ---
root = tk.Tk()
root.title("Generador de secuencias mediante el Método Congruencial Lineal")
root.geometry("380x350")
root.config(padx=20, pady=20)

tk.Label(root, text="Validación de parámetros congruenciales", font=("Arial", 12, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

# --- Entrada a ---
tk.Label(frame, text="a (multiplicador):").grid(row=0, column=0, sticky="e", pady=5)
entry_a = tk.Entry(frame)
entry_a.grid(row=0, column=1)
mensaje_a = tk.Label(frame, text="", fg="red", font=("Arial", 10))
mensaje_a.grid(row=1, column=0, columnspan=2)

# --- Entrada c ---
tk.Label(frame, text="c (incremento):").grid(row=2, column=0, sticky="e", pady=5)
entry_c = tk.Entry(frame)
entry_c.grid(row=2, column=1)
mensaje_c = tk.Label(frame, text="", fg="red", font=("Arial", 10))
mensaje_c.grid(row=3, column=0, columnspan=2)

# --- Entrada m ---
tk.Label(frame, text="m (módulo):").grid(row=4, column=0, sticky="e", pady=5)
entry_m = tk.Entry(frame)
entry_m.grid(row=4, column=1)
mensaje_m = tk.Label(frame, text="", fg="red", font=("Arial", 10))
mensaje_m.grid(row=5, column=0, columnspan=2)

# --- Entrada semilla X0 ---
tk.Label(frame, text="Semilla (X₀):").grid(row=6, column=0, sticky="e", pady=5)
entry_x0 = tk.Entry(frame)
entry_x0.grid(row=6, column=1)
mensaje_x0 = tk.Label(frame, text="", fg="red", font=("Arial", 10))
mensaje_x0.grid(row=7, column=0, columnspan=2)

mensaje_enteros= tk.Label(frame, text="", fg="red", font=("Arial", 10))
mensaje_enteros.grid(row=8, column=0, columnspan=2)

# --- Botón ---
tk.Button(root, text="Validar", command=ejecutar, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=15)

# Frame para la tabla y scroll
frame_tabla = tk.Frame(root)
frame_tabla.pack(pady=10)  # se puede pack porque es un nuevo frame

# Treeview
tree = ttk.Treeview(frame_tabla, columns=("Xn"), show="headings", height=10)
tree.heading("Xn", text="Xn")
tree.pack(side=tk.LEFT)

# Scrollbar
scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree.configure(yscrollcommand=scrollbar.set)

# Label al lado mostrando la cantidad de números
label_cantidad = tk.Label(frame_tabla, text="Cantidad: 0")
label_cantidad.pack(side=tk.LEFT, padx=10)



root.mainloop()
