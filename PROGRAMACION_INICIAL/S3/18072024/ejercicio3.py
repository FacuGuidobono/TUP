'''
nombre: Facundo
apellido: Guidobono
---
TP: Condicionales 03
---
Enunciado:

A partir del ingreso de una edad, determinar si la persona es mayor de edad o no. 
Si es mayor de 18 se mostrará el mensaje “UD ES MAYOR DE EDAD” caso contrario “UD ES MENOR DE EDAD”.


'''

edad = int(input("Ingrese su edad: "))

msg = 'UD ES MENOR DE EDAD'

if edad > 18 :
    msg = 'UD ES MAYOR DE EDAD'
    
print(msg)