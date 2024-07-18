'''
nombre: Facundo 
apellido: Guidobono
---
Ejercicio: entrada_salida_09
---
Enunciado:
Realizar un programa que a partir del ingreso del importe de una compra, aplique un 25% de descuento. 
Mostrar por pantalla cuánto es el total a pagar y cuánto fue el descuento obtenido.
'''

print("Ingrese el precio de un producto para realizarse un 25% de descuento\n")

precio = float(input("Ingrese el precio del producto: "))
descuento = precio * 0.25

print(f"\nEl total a pagar es de : ${precio - descuento}")
print(f"El descuento aplicado es de: ${descuento}")