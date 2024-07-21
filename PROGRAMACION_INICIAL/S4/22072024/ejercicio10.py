'''
nombre: Facundo
apellido: Guidobono
---
TP: Bucles 10
---
Enunciado:

Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.


'''


op = True
err = 'La nota ingresada debe estar comprendida entre 1 y 10 inclusive.'

while op:
    
    nota = int(input('Ingrese una nota: '))
    
    if nota < 1 or nota > 10:
        print(err)
    else:
        op = False  
print('='*40)
print(f'Nota ingresada: {nota}')
print('='*40)