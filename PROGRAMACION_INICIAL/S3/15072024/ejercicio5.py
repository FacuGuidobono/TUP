'''
nombre: Facundo
apellido: Guidobono
---
Ejercicio: entrada_salida_05
---
Enunciado:
Realizar un programa que permita el ingreso de dos números. Calcular la suma, resta, multiplicación y división de los mismos. 
Mostrar los resultados por pantalla. Utilizar una variable para mostrar el resultado (concatenar).
'''

print("Ingrese dos números para operar con ellos\n")
num1 = float(input("Ingrese el primer número: ")) 
num2 = float(input("Ingrese el segundo número: "))

#suma
resultado = num1 + num2
print("La suma de los dos numeros es:" + str(resultado))

#resta
resultado = num1 - num2
print(f"La resta de los dos numeros es: " + str(resultado))

#multiplicacion
resultado = num1 * num2
print(f"La multiplicacion de los dos numeros es: " + str(resultado))

#division
resultado = num1 / num2
print(f"La division de los dos numeros es: " + str(resultado))
