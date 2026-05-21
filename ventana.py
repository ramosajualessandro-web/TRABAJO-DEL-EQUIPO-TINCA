import tkinter as tk
from tkinter import messagebox

IVA = 0.16
caja = 0.0
clientes = 0

root = tk.Tk()
root.title("Sistema de ventas de una tienda")
root.geometry("420x380")
root.resizable(False, False)

# Variables
producto_var = tk.StringVar()
cantidad_var = tk.StringVar()
precio_var = tk.StringVar()
pago_var = tk.StringVar()

# Funciones

def actualizar_estado():
    lbl_clientes.config(text=f"Clientes atendidos: {clientes}")
    lbl_caja.config(text=f"Dinero total en caja: ${caja:.2f}")


def registrar_venta():
    global caja, clientes

    producto = producto_var.get().strip()
    if not producto:
        messagebox.showwarning("Advertencia", "Ingrese el nombre del producto.")
        return

    try:
        cantidad = int(cantidad_var.get())
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Advertencia", "Ingrese una cantidad válida.")
        return

    try:
        precio = float(precio_var.get())
        if precio < 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Advertencia", "Ingrese un precio válido.")
        return

    subtotal = cantidad * precio
    iva = subtotal * IVA
    total = subtotal + iva

    try:
        pago = float(pago_var.get())
        if pago < 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Advertencia", "Ingrese un pago válido.")
        return

    if pago < total:
        messagebox.showerror("Error", "Dinero insuficiente para cubrir el total de la compra.")
        return

    cambio = pago - total
    caja += total
    clientes += 1
    actualizar_estado()

    resultado = (
        f"Producto: {producto}\n"
        f"Cantidad: {cantidad}\n"
        f"Precio unitario: ${precio:.2f}\n"
        f"Subtotal: ${subtotal:.2f}\n"
        f"IVA (16%): ${iva:.2f}\n"
        f"Total: ${total:.2f}\n"
        f"Pago: ${pago:.2f}\n"
        f"Cambio: ${cambio:.2f}"
    )
    lbl_resultado.config(text=resultado)

    producto_var.set("")
    cantidad_var.set("")
    precio_var.set("")
    pago_var.set("")


