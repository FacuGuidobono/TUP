'''
nombre: Facundo
apellido: guidobono
---
TP: Condicionales 05
---
Enunciado:

Pedirle al usuario su edad, determinar si el usuario es adolescente.


'''

edad = int(input("Ingrese su edad: "))

msg = 'no es adolescente'

if edad > 12 and edad < 18:
    msg = 'es adolescente'
    
print(msg)