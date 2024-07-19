'''
nombre: Facundo
apellido: Guidobono
---
TP: Condicionales 04
---
Enunciado:

A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. 
Para serlo el mismo deberá medir más de 1.80 metros.


'''

altura = float(input("Ingrese su altura: "))

msg = 'No es pivot'
if altura > 1.80 :
    msg = 'Es pivot'
    
print(msg)