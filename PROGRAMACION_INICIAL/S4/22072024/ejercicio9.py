'''
nombre: Facundo
apellido: Guidobono
---
TP: Bucles 09
---
Enunciado:

Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.


'''

passw = 'UTN2024'  # default password


while passw != input('Ingrese la clave: '):  #comparamos
    print('Clave incorrecta, intente de nuevamente')
    

print('Bienvenido')