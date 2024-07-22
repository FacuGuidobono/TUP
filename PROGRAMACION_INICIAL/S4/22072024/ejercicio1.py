'''
nombre: Facundo
apellido: Guidobono
---
TP: Bucles 01
---
Enunciado:

Mostrar 10 repeticiones de números ascendentes desde el 1 al 10


'''

rep = 1  #_inicializo las repeticiones
while rep < 11: 
    num=1 #_inicializo los N°
   
    print('='*50)
    print (f'N° rep: {rep}') #?Muestro el N° de rep
    print('='*50)
   
    while num < 11: 
        print(num) #?muestro los N°
        num += 1 #_aumento el N° en 1
    rep += 1 #_aumento la rep en 1