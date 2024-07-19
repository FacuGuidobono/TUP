'''
nombre: Facundo
apellido: Guidobono
---
TP: Condicionales 08
---
Enunciado:

A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, 
considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot

'''

altura = float(input("Ingrese la altura en centímetros (cm): "))

if altura < 160:
    print("Base")
if altura >= 160 and altura < 180:
    print("Escolta")
if altura >= 180 and altura < 200:
    print("Alero")
if altura >= 200:
    print("Ala-Pívot o Pívot")
    