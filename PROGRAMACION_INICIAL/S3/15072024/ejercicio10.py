'''
nombre: Facundo
apellido: Guidobono
---
Ejercicio: entrada_salida_10
---
Enunciado:
Realizar un programa que a partir del ingreso del importe de una compra, y el ingreso de un valor a descontar aplique dicho descuento a la compra. 
Mostrar por pantalla cuánto es el total a pagar y cuánto fue el descuento obtenido.
'''


print("Ingrese el precio de un producto y un porcentaje (%) para realizarse un de descuento\n")

precio = float(input("Ingrese el precio del producto: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))
descuento = precio * (porcentaje / 100)

print(f"\nEl total a pagar es de : ${precio - descuento}")
print(f"El descuento aplicado es de: ${descuento}")