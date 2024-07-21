'''
nombre: Facundo
apellido: Guidobono
---
TP: Bucles 08
---
Enunciado:

Ingresar 10 números enteros. Determinar el máximo y el mínimo.


'''

rep = 0

while rep < 10:
    
    num = int(input("Ingrese un numero entero: "))
    
    # para la primera repeticion guardamos el valor en ambas variables para compararlas luego
    if rep == 0:  
        max = num
        min = num
    else:  # sino es la primera repeticion comparo 
        if num >= max:
            max = num
        if num < min:
            min = num
    rep += 1 
    
    
print('='*40)
print(f'''
El numero maximo ingresado es: {max}
EL numero minimo ingresado es: {min}
      
      ''')
print('='*40)