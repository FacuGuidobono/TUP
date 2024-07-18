'''
nombre: Facundo
apellido: Guidobono
---
Ejercicio: entrada_salida_08
---
Enunciado:
Realizar un programa que a partir del ingreso de un sueldo y de un porcentaje de aumento, calcule y muestre el sueldo con el aumento porcentual ingresado por el usuario.
'''

print("ingrese su sueldo con un porcentaje de aumento\n")

sueldo = float(input("Ingrese su sueldo: "))
porcentaje = float(input("Ingrese el porcentaje de aumento (%): "))


print(f"\nSu sueldo con incremento del {porcentaje}% es: ${sueldo + sueldo * (porcentaje / 100)}")
