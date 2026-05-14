# Sistema de ventas de una tienda

caja = 0
clientes = 0
IVA = 0.16

print("Bienvenido al sistema de ventas")

while True:

    clientes += 1

    print("\nCliente", clientes)

    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad comprada: "))
    precio = float(input("Precio del producto: $"))

    subtotal = cantidad * precio
    iva = subtotal * IVA
    total = subtotal + iva

    print("\nProducto:", producto)
    print("Cantidad:", cantidad)
    print("Precio unitario: $", round(precio, 2))
    print("Subtotal: $", round(subtotal, 2))
    print("IVA: $", round(iva, 2))
    print("Total a pagar: $", round(total, 2))

   