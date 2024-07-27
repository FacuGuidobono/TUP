'''

En un gimnasio se necesita un programa que permita ingresar datos de 50 socios Por cada socio, se ingresa:

•	Nombre completo.
•	Tarifa Base (3500, no se podrá ingresar otro valor)
•	Edad (entre 18 y 100 años).
•	Altura (en centímetros, mayor a 100 y menor a 250).
•	Peso (en kilogramos, mayor a 30 y menor a 200).
•	Rutina de entrenamiento: Debe elegir entre las opciones "Cardio", "Musculación" o "Funcional".

Se pide calcular e informar por alert o document write:

1.	Los socios que realicen:
1.	Musculacion, tendrán un descuento del 20%.
2.	Cardio, tendrán un descuento del 20 %.
3.	Funcional, un incremento del 15%
2.	La actividad que mayor recaudo sin considerar el incremento o el descuento. #!es el precio base
3.	La cantidad de socios que hacen Musculacion y tienen entre 35 y 40 años de edad inclusive.
4.	El  Nombre del socio con mayor peso, que hace "Funcional".
5.	La diferencia entre el total recaudado sin descuento/incremento y el total recaudado con descuento/incremento.


'''
TARIFA_BASE = 3500
descuento = -1.2
socios = 0


tarifa_musculacion = 0
tarifa_funcional   = 0
tarifa_cardio      = 0

peso_funcional = None
total_sin_descuento = 0
total_con_descuento = 0
cant_musculacion    = 0

while socios < 50:
    
    #_NOMBRE
    nombre = input('Ingrese el nombre del socio: ')
    
    #_VALIDACION TARIFA
    tarifa = float(input('Ingrese la tarifa base ($3500): '))
    while tarifa != TARIFA_BASE:
        tarifa = float(input('ERROR: Ingrese la tarifa base ($3500): '))
        
    #_VALIDACION EDAD
    edad = int(input('Ingrese la edad del socio (18 a 100 anios): '))
    while edad < 17 or edad > 100:
        edad = int(input('ERROR: Ingrese la edad del socio: '))
        
    #_VALIDACION ALTURA
    altura = float(input('Ingrese la altura del socio'))
    while altura < 100 and altura > 250:
        altura = float(input('ERROR: Ingrese la altura del socio'))
        
    #_VALIDACION PESO
    peso = float(input('Ingrese el peso del socio: '))
    while peso < 30  and peso > 200 : 
        peso = float(input('ERROR: Ingrese el peso del socio: '))
    
    #_VALIDACION RUTINA
    rutina = input('Ingrese la rutina de socio "Cardio", "Musculación" o "Funcional": ')
    while rutina != 'Cardio' and rutina != 'Musculacion' and 'Funcional':
        rutina = input('ERROR: Ingrese la rutina de socio "Cardio", "Musculación" o "Funcional": ')
    
    total_sin_descuento += tarifa
    
    #_VARIACIONES DE TARIFA
    if rutina == 'Cardio':
        tarifa = tarifa * descuento 
        
    else:
        
        if rutina == 'Musculacion':
            tarifa = tarifa * descuento 
            tarifa_musculacion += tarifa
            if edad >35 and edad < 41:
                cant_musculacion += 1
                tarifa_musculacion += tarifa
        else:
            tarifa = tarifa *1.15
            tarifa_funcional += tarifa
            if peso_funcional == None or peso_funcional < peso:
                peso_funcional = peso
        
    total_con_descuento += tarifa
    
    
    socios+=1
  
  
#_DIFERENCIA ENTRE TOTALES
diff_total = total_sin_descuento - total_con_descuento



print(f'''


*	La actividad que mayor recaudo sin considerar el incremento o el descuento: {TARIFA_BASE}


*   La cantidad de socios que hacen Musculacion y tienen entre 35 y 40 años de edad inclusive: {cant_musculacion}


*   El  Nombre del socio con mayor peso, que hace "Funcional" es: {peso_funcional}


*   La diferencia entre el total recaudado sin descuento/incremento y el total recaudado con descuento/incremento: {diff_total}





''')