'''
nombre: Facundo
apellido: Guidobono
---
TP: Condicionales 07
---
Enunciado:

Pedirle al usuario su edad, determinar si es mayor (18 años o más), niño/a (menor de 10), 
pre-adolescente (edad entre 10 y 13 años inclusive) o adolescente (edad entre 13 y 17 años).


'''

edad = int(input("Ingrese su edad: "))

if edad > 17:
    print("Es mayor de edad")
    
if edad < 10:
    print("Es niño/a")
    
if edad > 9 and edad < 14:
    print("Es pre-adolescente")
    
if edad > 13 and edad < 18:
    print("Es adolescente")

    