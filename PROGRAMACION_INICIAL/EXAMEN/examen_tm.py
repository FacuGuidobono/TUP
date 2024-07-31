'''
Nombre: Facundo
Apellido: Guidobono

UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
franquicia que se insertará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:
A. nombre
B. edad (no menor a 18)
C. está empleado (si-no)
D. género (Masculino - Femenino - Otro)
E. voto (APPLE, DUNKIN, IKEA)
Se necesita saber:
1. Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA,
cuya edad esté entre 25 y 50 años inclusive.
2. Nombre y voto del encuestado de género Masculino con menor edad.
3. Porcentaje de votos de cada género.
4. Promedio de edad de los encuestados de género Femenino que votaron
IKEA.

'''



#_ SISTEMA DE VOTO ELECTRONICO

op = 's'

cant_desempleados = 0
cant_votos_masculinos = 0
cant_votos_femeninos = 0
cant_votos_otro = 0

suma_edades_femeninos = 0

menor_edad = None
nombre_menor_edad = 'None'
voto_menor_edad = 'None'


while op == 's':
    
#! ----------- ingreso y validacion de datos ------------- 
    
    nombre = input('ingrese el nombre del encuestado: ')
    
    edad = int(input('Ingrese la edad (mayor de edad): '))
    while edad < 18:
        edad = int(input('ERROR: ingrese la edad nuevamente: '))
    
    empleado = input('está empleado (si-no)?: ')
    while empleado != 'si' and empleado != 'no':
        empleado = input('ERROR: ingrese (si-no): ')
        
    gender = input('Ingrese el genero (Masculino - Femenino - Otro): ')
    while gender != 'Masculino' and gender != 'Femenino' and gender != 'Otro':
        gender = input('ERROR: ingrese (Masculino - Femenino - Otro): ')

    voto = input('Ingrese el voto (APPLE, DUNKIN, IKEA): ')
    while voto != 'APPLE' and voto != 'DUNKIN' and voto != 'IKEA':
        voto = input('ERROR: ingrese (APPLE, DUNKIN, IKEA): ')
    
    
    #_ Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad esté entre 25 y 50 años inclusive.
    
    if empleado == 'no' and voto != 'apple' and (edad >= 25 and edad <= 50):
        cant_desempleados += 1
        
    
    if gender == 'Masculino':
        
        cant_votos_masculinos += 1
        
        
        #_ Nombre y voto del encuestado de género Masculino con menor edad.
        if menor_edad == None or edad < menor_edad:
            menor_edad = edad
            nombre_menor_edad = nombre
            voto_menor_edad = voto
    else:
        
        if gender == 'Femenino':
            cant_votos_femeninos += 1
            
            if voto == 'IKEA':
                suma_edades_femeninos += edad
                
        else:
            cant_votos_otro += 1
    
    op = input('Desea realizar otra encuesta (s/n)?: ')
    

#_ Porcentaje de votos de cada género.
total_votos = cant_votos_masculinos + cant_votos_femeninos + cant_votos_otro

if total_votos != 0 :
    porcentaje_votos_masculinos = (cant_votos_masculinos / total_votos) * 100
    porcentaje_votos_femeninos  = (cant_votos_femeninos / total_votos) * 100
    porcentaje_votos_otros      = (cant_votos_otro/ total_votos) * 100
else:
    porcentaje_votos_masculinos = 'None'
    porcentaje_votos_femeninos  = 'None'
    porcentaje_votos_otros      = 'None'
    
    
#_Promedio de edad de los encuestados de género Femenino que votaron IKEA.
if cant_votos_femeninos != 0:
    promedio_edad_fem_ikea = suma_edades_femeninos/cant_votos_femeninos
else:
    promedio_edad_fem_ikea = 'None'
    


print(f'''

1. Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad esté entre 25 y 50 años inclusive: {cant_desempleados}

2. Nombre y voto del encuestado de género Masculino con menor edad: 
    
    - Nombre: {nombre_menor_edad}
    - Voto :  {voto_menor_edad}

3. Porcentaje de votos de cada género: 
    
    - Masculinos: {porcentaje_votos_masculinos}%
    - Femeninos:  {porcentaje_votos_femeninos}%
    - Otros:      {porcentaje_votos_otros}%

4. Promedio de edad de los encuestados de género Femenino que votaron IKEA: {promedio_edad_fem_ikea}
    
''')



       