# Enunciado:
# De los 3 Jugadores de un Reality Show, se registra:
# nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
# Informar:
# a. nombre del candidato con más votos
# b. nombre y edad del candidato con menos votos
# c. el promedio de edades de los candidatos
# d. total de votos emitidos.
# Todos los datos se ingresan mediante input()
#@Facu Guidobono

#*-----------------------------------------------------------------
#*           CARA DE DATOS DE LOS JUGADORES
#*-----------------------------------------------------------------

i = 0 

while i < 3:  #! CARGA DE 3 JUGADORES
    
    print('-'*50)
    print (f'Datos del jugador N°{i+1}') #?Muestro el N° de rep 
    print('-'*50)
    
    
    a = True
    while a: #!validamos que el nombre no este vacio
        nombre = input("Ingrese nombre del jugador: ")
        if len(nombre) == 0 or nombre == ' ':
            print("Error, el campo nombre no puede estar vacio")
        
        else:
            a = False
    
    a = True
    while a: #!valida que la edad sea mayor a 25
        edad = int(input("Ingrese la edad del jugador: "))
        
        if edad < 26:
            print("Error, la edad debe ser mayor a 25")
            
        elif edad > 79:
            print('Deje al abuelo tranquilo en casa')
            
        else:
            a = False
            
    a = True
    while a: #!valida que los votos no sean menores a 0
        votos = int(input("Ingrese los votos del jugador: "))
        if votos < 0:
            print("Error, los votos no pueden ser menores a 0")
        else:
            a = False
            
#! GUARDAMOS EN LAS VARIABLES SEGUN ORDEN DE CARGA
    if i == 0:
        nombre1 = nombre
        edad1 = edad
        votos1 = votos
    elif i == 1:
        nombre2 = nombre
        edad2 = edad
        votos2 = votos
        
    elif i == 2:
        nombre3 = nombre
        edad3 = edad
        votos3 = votos  
    else:
        print("Error, no se pueden registrar mas de 3 jugadores") #nunca se llega o deberia llegar a esta instancia :D

    i += 1 



#*-----------------------------------------------------------------   
#* DIFERENCIAMOS SI TIENEN EL MISMO NOMBRE POR UN INDICE
#*-----------------------------------------------------------------    


if nombre1 == nombre2 == nombre3:
    nombre1 = nombre1 + '(1)'
    nombre2 = nombre2 + '(2)'
    nombre3 = nombre3 + '(3)'
    
elif nombre1 == nombre2 and nombre1 !=nombre3:
    nombre1 = nombre1 + '(1)'
    nombre2 = nombre2 + '(2)'

elif nombre1 == nombre3 and nombre1 != nombre2:
    nombre1 = nombre1 + '(1)'
    nombre3 = nombre3 + '(2)'
    
elif nombre2 == nombre3 and nombre2 != nombre1:
    nombre2 = nombre2 + '(1)'
    nombre3 = nombre3 + '(2)'

#*-----------------------------------------------------------------   
#* MOSTRAMOS LOS DATOS CARGADOS POR EL USER  
#*-----------------------------------------------------------------

print('\n'*5)
print('-'*100)

print(f'''
JUGADORES REGISTRADOS:
------JUGADOR N°1 --------     
Nombre: {nombre1}
Edad: {edad1} 
Votos: {votos1}
      
------JUGADOR N°2 --------  
Nombre: {nombre2}
Edad: {edad2}
Votos: {votos2}
      
------JUGADOR N°3 --------  
Nombre: {nombre3}
Edad: {edad3}
Votos: {votos3}  
      ''')


#*-----------------------------------------------------------------
#* NOMBRE DEL CANDIDATO CON MAS VOTOS
#*-----------------------------------------------------------------
print('-'*100)

if votos1 > votos2 and votos1 > votos3:
    print(f'El candidato con mas votos es {nombre1}: {votos1} votos ')
elif votos2 > votos1 and votos2 > votos3:
    print(f'El candidato con mas votos es {nombre2}: {votos2} votos')
elif votos3 > votos1 and votos3 > votos2:
    print(f'El candidato con mas votos es {nombre3}: {votos3} votos') 
    
elif votos1 == votos2 == votos3:  
    print(f'MAYOR CANTIDAD DE VOTOS:\nTodos los candidatos tienen la misma cantidad de votos: {votos1} votos') 
elif votos1 == votos2:
    print(f'Los candidatos {nombre1} y {nombre2} empatados con la mayor cantida de votos: {votos1} votos')
elif votos1 == votos3:
    print(f'Los candidatos {nombre1} y {nombre3} empatados con la mayor cantida de votos:  {votos1} votos')
elif votos2 == votos3:
    print(f'Los candidatos {nombre2} y {nombre3} empatados con la mayor cantida de votos:  {votos2} votos')

    
   

#*-----------------------------------------------------------------
#* NOMBRE Y EDAD DEL CANDIDATO CON MENOS VOTOS
#*-----------------------------------------------------------------
print('-'*100)

if votos1 < votos2 and votos1 < votos3:
    print(f'El candidato con menos votos es {nombre1} de {edad1} años con: {votos1} votos')  
elif votos2 < votos1 and votos2 < votos3:
    print(f'El candidato con menos votos es {nombre2} de {edad2} años con: {votos2} votos')  
elif votos3 < votos1 and votos3 < votos2:
    print(f'El candidato con menos votos es {nombre3} de {edad3} años con: {votos3} votos')
    
elif votos1 == votos2 == votos3:  
    print(f'MENOR CANTIDAD DE VOTOS:\nTodos los candidatos tienen la misma cantidad de votos: {votos1} votos') 
elif votos1 == votos2 and votos1 != votos3:
    print(f'Los candidatos {nombre1} de {edad1} años y {nombre2} de {edad2} años empatados con la menor cantidad de votos: {votos1} votos')
elif votos1 == votos3 and votos1 != votos2:
    print(f'Los candidatos {nombre1} de {edad1} años y {nombre3} de {edad3} años empatados con la menor cantidad de votos: {votos1} votos')    
elif votos2 == votos3 and votos2 != votos1:
    print(f'Los candidatos {nombre2} de {edad2} años y {nombre3} de {edad3} años empatados con la menor cantidad de votos: {votos2} votos')

#*-----------------------------------------------------------------
#* PROMEDIO EDAD DE LOS CANDIDATOS
#*-----------------------------------------------------------------
print('-'*100)
print(f'El promedio de edad de los candidatos es: {(edad1 + edad2 + edad3) / 3}')


#*-----------------------------------------------------------------
#* EL TOTAL DE VOTOS EMITIDOS
#*-----------------------------------------------------------------
print('-'*100)
print(f'El total de votos emitidos es: {votos1 + votos2 + votos3} votos')
print('-'*100)
