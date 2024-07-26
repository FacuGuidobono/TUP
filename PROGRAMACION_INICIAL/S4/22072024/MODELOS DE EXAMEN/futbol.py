'''

Para una tienda de deportes se necesita un programa que permita ingresar los datos de los jugadores de fútbol que han comprado una camiseta, 
hasta que el cliente quiera. 
Por cada jugador, se ingresa:

Nombre del jugador
Equipo al que pertenece (validar "Barcelona", "Real Madrid", "Bayern Munich").
Posición en el campo (validar "delantero", "defensa", "portero").
Edad (entre 18 y 40),


Precio de la camiseta (mas de 5 digitos, sin ceros a la izquierda).
Se pide informar por print
1- El porcentaje de camisetas vendidas por equipo [Barcelona: 40%, Real Madrid: 40%, Bayer Munich: 20%] la suma debe dar 100%.
2- El importe total recaudado por la venta de camisetas.
3- Promedio de edad de los jugadores que compraron camisetas.
4- Nombre, equipo y posición del jugador más longevo.


'''


op = True

cont_barsa = 0
cont_madrid = 0
cont_bayern = 0

suma_edades = 0


importe_total = 0

#_Datos del jugador mas longevo
longevo = None




while op:
    
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    
    #_ Validacion Equipo
    equipo = input(f'Ingrese el equipo al que pertence {nombre_jugador} ("Barcelona", "Real Madrid", "Bayern Munich"): ')
    
    while equipo != 'Barcelona' and equipo != 'Real Madrid' and equipo != 'Bayern Munich':
        equipo = input(f'ERROR: Ingrese el equipo al que pertence {nombre_jugador} ("Barcelona", "Real Madrid", "Bayern Munich"): ')
    
    #_ Cantidad de camisetas vendidas por equipo
    if equipo == 'Barcelona':
        cont_barsa += 1
    else:
        if equipo == 'Real Madrid':
            cont_madrid += 1
        else:
            if equipo == 'Bayern Munich':
                cont_bayern += 1
    
    
    
    
    
    
    #_Valdiacion posicion en el campo
    posicion = input(f'Ingrese la posicion en el campo de {nombre_jugador} ("delantero", "defensa", "portero"): ')
    
    while posicion != 'delantero' and posicion!= 'defensa' and posicion != 'portero':
        posicion = input(f'Error: Ingrese nuevamente la posicion en el campo de {nombre_jugador} ("delantero", "defensa", "portero"): ')
    
    #_validacion edad
    edad = int(input(f'Ingrese la edad de {nombre_jugador} (entre 18 y 40):'))
    while edad > 40 or edad < 18:
        edad = int(input(f'Error: Ingrese nuevamente la edad de {nombre_jugador} (entre 18 y 40):'))
    
    suma_edades += edad
    
    
    
    precio_camiseta = float(input('ingrese el precio de la camiseta: '))
    
    #_validacion precio camiseta
    while precio_camiseta < 10000:
        precio_camiseta = float(input('Error: Ingrese nuevamente el precio de la camiseta (mas de 5 digitos, sin ceros a la izquierda): '))
    

    #_importe total
    importe_total += precio_camiseta
    
    
    #_Datos jugador mas longevo  
    if longevo is None or edad > longevo:
        longevo = edad
        nombre_mas_longevo = nombre_jugador
        equipo_mas_longevo = equipo
        posicion_mas_longevo = posicion
        
        
        #_ingreso de datos hasta que el cliente quiera
        op2 = input('Desea continuar ingresando jugadores (s/n) ?: ')
        if op2 == 'n':
            op = False
    
    

#_cantidad total de ventas
cantidad_total = cont_barsa + cont_madrid + cont_bayern

#_Promedio de edades de los jugadores
promedio_edad = suma_edades / cantidad_total
#_Porcentaje de camisetas vendidas por equipo
porcentaje_barsa = (cont_barsa * 100) / cantidad_total
porcentaje_madrid = (cont_madrid * 100) / cantidad_total
porcenteje_bayern = (cont_bayern * 100) / cantidad_total


print('='*50)
print(f'''

* Porcentaje de camisetas vendidas por equipo:
    Barcelona: {porcentaje_barsa:2f}%
    Real Madrid: {porcentaje_madrid:2f}%
    Bayern Munich: {porcenteje_bayern:2f}%

* importe total recaudado: ${importe_total}

* Promedio de edad de los jugadores que compraron camisetas: {promedio_edad:2f}

* Jugador mas longevo: {nombre_mas_longevo}, {equipo_mas_longevo}, {posicion_mas_longevo}

''')
print('='*50)




