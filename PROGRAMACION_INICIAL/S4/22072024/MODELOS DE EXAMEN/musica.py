'''
Para una escuela de música se necesita un programa que permita ingresar los datos de los estudiantes, hasta que el cliente quiera. Por cada estudiante, 
se ingresa:
A- Nombre completo
B- Instrumento que toca (validar "guitarra", "piano", "batería").
C- Edad (entre 7 y 18),
D- Horas de estudio por semana (más de 0 y menos de 57),
E- Precio por clase (desde 200 hasta 500).

Se pide informar por print: 


1- El estudiante con más horas de estudio por semana de batería. 
2- El promedio recaudado por actividad (guitarra, piano, batería). 
3- Cantidad de estudiantes que tocan piano y tienen más de 12 años. 
4- La actividad que posee menos estudiantes.
5- Nombre completo e instrumento del estudiante más joven.
'''



#!Inicializacion de variables

op = True

cant_hs_bateria = 0

recaudado_bateria = 0
recaudado_guitarra = 0
recaudado_piano = 0 

cont_bateria = 0
cont_guitarra = 0
cont_piano = 0  

cant_hs_bateria = 0
cont_piano_doce_anios = 0
edad_mas_joven = None
mas_hs_estudio = None
alumno_bateria = "No hay ningun alumno que toque la bateria"



while op == True:
    
    #_ A Ingreso de nombre
    nombre = input('Ingrese el nombre del estudiante: ')
    
    
    
    #_ B Validacion de instrumento
    instrumento = input('Ingrese el instrumento que toca (guitarra, piano, batería): ')
    while instrumento != 'guitarra' and instrumento != 'piano' and instrumento  != 'bateria':
        instrumento = input('Error: Ingrese un instrumento válido (guitarra, piano, batería): ')
    
    
    
    #_ C Validacion edad
    edad = int(input('Ingrese la edad del estudiante (entre 7 y 18):'))
    while edad > 18 or edad < 7:
        edad = int(input('Error: Ingrese nuevamente la edad del estudiante (entre 7 y 18):'))
    
    
    
    #_ D Validacion horas de estudio
    horas = int(input('Ingrese las horas de estudio por semana (mas de 0 y menos de 57):')) 
    while horas > 57 or horas < 0:
        horas = int(input('Error: Ingrese nuevamente las horas de estudio por semana (mas de 0 y menos de 57):'))

    
    #_ E Validacion precio por clase
    precio = float(input('Ingrese el precio por clase (desde 200 hasta 500):'))
    while precio > 500 or precio < 200:
        precio = float(input('Error: Ingrese nuevamente el precio por clase (desde 200 hasta 500):'))
    
    
    
    #_ Alumnos mas joven
    
    if edad_mas_joven == None or edad < edad_mas_joven:
        edad_mas_joven = edad
        nombre_mas_joven = nombre
        instrumento_mas_joven = instrumento
    
        
    if instrumento == 'bateria':
        recaudado_bateria += precio
        cont_bateria += 1
        if cant_hs_bateria == None or horas > cant_hs_bateria:
            cant_hs_bateria += horas
            alumno_bateria = nombre      
    else:
        if instrumento == 'guitarra':
            cont_guitarra += 1
            recaudado_guitarra += precio
        else: #_piano
            cont_piano += 1
            recaudado_piano += precio
            if edad > 12:
                cont_piano_doce_anios += 1
    
    #_ingreso de datos hasta que el cliente quiera
    op2 = input('Desea continuar ingresando estudiantes (s/n) ?: ')
    if op2 == 'n':
        op = False

#-----------------------------------------------------------------------------------------
    
#_ Actividad con menos estudiantes

if cont_guitarra < cont_bateria and cont_guitarra < cont_piano:
        actividad_menos_estudiantes =  'Guitarra'
        cont_menos_estudiantes = cont_guitarra
else:
    if cont_bateria < cont_piano:
        actividad_menos_estudiantes = 'Batería'
        cont_menos_estudiantes = cont_bateria
    else:
        actividad_menos_estudiantes = 'Piano'
        cont_menos_estudiantes = cont_piano

#________________________________________________________________  

cantidad_total = cont_piano + cont_guitarra + cont_bateria


promedio_guitarra = recaudado_guitarra / cantidad_total
promedio_piano = recaudado_piano / cantidad_total
promedio_bateria = recaudado_bateria / cantidad_total

#________________________________________________________________ 


#_MUESTA DE DATOS   
    
print(f'''

1- El estudiante con más horas de estudio por semana de batería: {alumno_bateria} con {cant_hs_bateria} horas.

2- El promedio recaudado por actividad (guitarra, piano, batería): 
    * Guitarra: ${promedio_guitarra}
    * Piano: ${promedio_piano}
    * Batería: ${promedio_bateria}
    
3- La cantidad de estudiantes de piano que son mayores de 12 años: {cont_piano_doce_anios}

4- La actividad que posee menos estudiantes es: {actividad_menos_estudiantes} con {cont_menos_estudiantes} estudiantes.

5- Nombre completo e instrumento del estudiante más joven: {nombre_mas_joven} de {edad_mas_joven} años y su instrumento es {instrumento_mas_joven}.

''')