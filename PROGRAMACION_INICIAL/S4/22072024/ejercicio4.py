'''
nombre: Facundo 
apellido: Guidobono
---
TP: Bucles 04
---
Enunciado:

Mostrar la suma de los números pares desde el 1 hasta el 10.


'''

rep = 1 #_inicializo las repeticiones   
num = 0 #_acumulador
while rep < 11:
    
    if rep % 2 == 0:
        num += rep #_sumo los N° 
    
    rep += 1

print(f'La suma de los numeros pares del 1 hasta 10 es : {num}') #muestro la suma de los N

