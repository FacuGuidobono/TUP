'''
nombre: Facundo
apellido: Guidobono
---
Ejercicio: entrada_salida_06
---
Enunciado:
Realizar un programa que pida dos números enteros. 
Calcular y mostrar el resto de la división entre ambos números. Ej: "El resto de dividir 7 por 2 es: 1" .
'''

print("Ingrese dos números enteros para calcular su resto\n")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print(f"El resto de dividir {num1} por {num2} es: {num1 % num2}")