# LIBRERIA TKINTER
import tkinter as tk
from tkinter import messagebox

# VARIABLES
caja = 0
clientes = 0
IVA = 0.16

# FUNCION PARA REGISTRAR VENTA
def venta():
    global caja
    global clientes

    try:
        clientes += 1

        producto = campo_producto.get()
        cantidad = int(campo_cantidad.get())
        precio = float(campo_precio.get())
        pago = float(campo_pago.get())

        subtotal = cantidad * precio
        iva = subtotal * IVA
        total = subtotal + iva

        if pago < total:
            resultado.config(
                text="Dinero insuficiente",
                fg="red"
            )

        else:
            cambio = pago - total
            caja += total

            resultado.config(
                text=
                "Cliente: " + str(clientes) +
                "\nProducto: " + producto +
                "\nSubtotal: $" + str(round(subtotal, 2)) +
                "\nIVA: $" + str(round(iva, 2)) +
                "\nTotal: $" + str(round(total, 2)) +
                "\nCambio: $" + str(round(cambio, 2)) +
                "\nCaja Total: $" + str(round(caja, 2)),
                fg="green"
            )

    except:
        messagebox.showerror("Error", "Ingrese datos correctos")

# FUNCION LIMPIAR
def limpiar():
    campo_producto.delete(0, tk.END)
    campo_cantidad.delete(0, tk.END)
    campo_precio.delete(0, tk.END)
    campo_pago.delete(0, tk.END)

    resultado.config(text="")

# FUNCION CAMBIAR COLOR
def cambiar_color():
    colores = ["#AED6F1", "#A9DFBF", "#F9E79F", "#F5CBA7", "#D7BDE2"]

    import random
    color = random.choice(colores)

    ventana.config(bg=color)

    titulo.config(bg=color)
    texto_producto.config(bg=color)
    texto_cantidad.config(bg=color)
    texto_precio.config(bg=color)
    texto_pago.config(bg=color)
    resultado.config(bg=color)

# CREAR VENTANA
ventana = tk.Tk()
ventana.title("Sistema de Ventas")
ventana.geometry("500x500")
ventana.config(bg="#AED6F1")

# TITULO
titulo = tk.Label(
    ventana,
    text="SISTEMA DE VENTAS",
    font=("Arial", 18, "bold"),
    bg="#AED6F1",
    fg="black"
)
titulo.pack(pady=10)

# PRODUCTO
texto_producto = tk.Label(
    ventana,
    text="Nombre del producto",
    bg="#AED6F1",
    font=("Arial", 11)
)
texto_producto.pack()

campo_producto = tk.Entry(
    ventana,
    width=30,
    font=("Arial", 11)
)
campo_producto.pack(pady=5)

# CANTIDAD
texto_cantidad = tk.Label(
    ventana,
    text="Cantidad",
    bg="#AED6F1",
    font=("Arial", 11)
)
texto_cantidad.pack()

campo_cantidad = tk.Entry(
    ventana,
    width=30,
    font=("Arial", 11)
)
campo_cantidad.pack(pady=5)

# PRECIO
texto_precio = tk.Label(
    ventana,
    text="Precio",
    bg="#AED6F1",
    font=("Arial", 11)
)
texto_precio.pack()

campo_precio = tk.Entry(
    ventana,
    width=30,
    font=("Arial", 11)
)
campo_precio.pack(pady=5)

# PAGO
texto_pago = tk.Label(
    ventana,
    text="Pago del cliente",
    bg="#AED6F1",
    font=("Arial", 11)
)
texto_pago.pack()

campo_pago = tk.Entry(
    ventana,
    width=30,
    font=("Arial", 11)
)
campo_pago.pack(pady=5)

# BOTON REGISTRAR
boton_venta = tk.Button(
    ventana,
    text="Registrar Venta",
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    command=venta
)
boton_venta.pack(pady=10)

# BOTON LIMPIAR
boton_limpiar = tk.Button(
    ventana,
    text="Limpiar Datos",
    bg="orange",
    fg="white",
    font=("Arial", 11, "bold"),
    command=limpiar
)
boton_limpiar.pack(pady=5)

# BOTON CAMBIAR COLOR
boton_color = tk.Button(
    ventana,
    text="Cambiar Color",
    bg="blue",
    fg="white",
    font=("Arial", 11, "bold"),
    command=cambiar_color
)
boton_color.pack(pady=5)

# BOTON SALIR
boton_salir = tk.Button(
    ventana,
    text="Salir",
    bg="red",
    fg="white",
    font=("Arial", 11, "bold"),
    command=ventana.destroy
)
boton_salir.pack(pady=10)

# RESULTADO
resultado = tk.Label(
    ventana,
    text="",
    bg="#AED6F1",
    font=("Arial", 11, "bold")
)
resultado.pack(pady=20)

# EJECUTAR
ventana.mainloop()
