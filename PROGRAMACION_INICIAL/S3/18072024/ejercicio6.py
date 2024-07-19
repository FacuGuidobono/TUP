'''
nombre: Facundo
apellido: Guidobono
---
TP: Condicionales 06
---
Enunciado:

Pedirle al usuario su edad, determinar si el usuario NO es adolescente.


'''

edad = int(input("Ingrese su edad: "))

msg = 'Es adolescente'

if edad < 12 or edad > 18:
    msg = 'No es adolescente'
    
print(msg)