'''
nombre: Facundo
apellido: Guidobono
---
TP: Bucles integrador
---
Enunciado:

Permitir que el usuario ingrese todos los números que desee. Los mismos deben estar comprendidos entre -10000 y 10000, y deben ser distintos de 0. Determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El número positivo más grande.
El porcentaje de números negativos ingresados, respecto del total de ingresos.



'''

#_intervalo de numeros permitidos
MIN = -10000
MAX = 10000
CERO = 0

max_pos = 0 #_ N positivo mas grande

sum_pos = 0 #_ suma de numeros positivos
sum_neg = 0 #_ suma de numeros negativos

cant_pos = 0 #_ cantidad de numeros positivos
cant_neg = 0 #_ cantidad de numeros negativos

while True:
    
    num = int(input(f"Ingrese un numero comprendidos entre -10000 y 10000. (No puede ingresar 0): "))
    
    #_ validamos el ingreso
    if num == CERO or num < MIN or num > MAX:   
        print("ERROR: El numero ingresado no esta permitido.")
        
    #_discriminamos numeros neg  
    elif num < 0: #_ numeros negativos
        sum_neg += num
        cant_neg += 1
        
    #_discriminamos numeros pos       
    elif num > 0: #_ numeros positivos
        sum_pos += num
        cant_pos += 1
        
        if num >= max_pos: #_ buscamos  N positivo mayor
            max_pos = num
        
        
    
    #_confirmacion continuar carga
    op = input("¿Desea ingresar otro numero? (s/n): ") 
    
    if op.lower() == 'n': #solo evaluo la condicion de salida 
        break  #rompe el bulce 


#_El promedio de los números positivos.
prom = sum_pos / cant_pos if cant_pos > 0 else 0  # se puede usar operador ternario o un if normal para no dividir por 0

#_porcentaje de numeros negativos respecto al total
porcentaje_negativos = (cant_neg / (cant_neg + cant_pos)) * 100 if (cant_neg + cant_pos) > 0 else 0 # aunque el denominador nunca deberia ser 0 xq se ingresa 1 num por lo -

print('='*40)
print(f'''
* La suma acumulada de los números negativos es: {sum_neg}
* La suma acumulada de los números positivos es: {sum_pos}
* La cantidad de números negativos ingresados es: {cant_neg}
* El promedio de los números positivos es: {prom}
* El número positivo más grande es: {max_pos}
* El porcentaje de números negativos ingresados respecto del total de ingresos es: {porcentaje_negativos}%
''')
print('='*40)