'''
nombre: Facundo 
apellido: Guidobono
---
TP: Bucles 02
---
Enunciado:

Mostrar 10 repeticiones de números descendentes desde el 10 al 1.


'''

rep = 1  #_inicializo las repeticiones
while rep < 11: 
    num=10 #_inicializo los N°
   
    print('='*50)
    print (f'N° rep: {rep}') #?Muestro el N° de rep
    print('='*50)
   
    while num > 0:  #! N° desc [10,1]
        print(num) #?muestro los N°
        num -= 1 #_decremento el N° en 1
    rep += 1 #_aumento la rep en 1