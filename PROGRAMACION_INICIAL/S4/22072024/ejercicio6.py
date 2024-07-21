'''
nombre: Facundo
apellido: Guidobono
---
TP: Bucles 06
---
Enunciado:

Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.


'''


rep = True
cantidad = 0
suma = 0 #

while rep:
    num = int(input(f"Ingrese un numero: "))
    
    suma = suma + num
    cantidad += 1
    
    op = input("¿Desea ingresar otro numero? (s/n): ") 
    
    if op.lower() == 'n': #solo evaluo la condicion de salida 
        rep = False   # se podria usar break tambien y evitar el uso de una variable
        

promedio = suma / cantidad

print('='*40)
print(f'''
La suma de los numeros es: {suma}
El promedio es: {promedio}
''')
print('='*40)