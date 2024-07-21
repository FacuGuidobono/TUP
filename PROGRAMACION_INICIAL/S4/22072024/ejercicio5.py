'''
nombre:
apellido:
---
TP: Bucles 05
---
Enunciado:

Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar por pantalla.


'''

rep = 0 #_cantidad de repeticiones
suma = 0 #
while rep < 5:
    num = int(input(f"Ingrese un numero: "))
    rep += 1
    suma = suma + num
    
promedio = suma / rep

print('='*40)
print(f'''
La suma de los numeros es: {suma}
El promedio es: {promedio}
''')

