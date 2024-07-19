'''
nombre: Facundo
apellido: Guidobono
---
TP: Condicionales 09
---
Enunciado:

Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos naturalizados desde los dieciocho (18) años están habilitados a votar. 
A partir del ingreso de la edad del usuario y el estado (si es naturalizado o nativo), 
se deberá informar si es o no posible que la persona concurra a votar en base a la información suministrada.



'''

estado = input("Ingrese su estado (nativo/naturalizado): ")
edad = int(input("Ingrese su edad: "))

msg = 'No puede concurrir a votar.'
if (edad > 15 and estado == "nativo") or (edad > 17 and estado == 'naturalizado'):
    msg = 'Puede concurrir a votar.'
    
print(msg)