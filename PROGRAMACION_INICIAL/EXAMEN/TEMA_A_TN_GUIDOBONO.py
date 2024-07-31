'''
Nombre: Facundo
Apellido: Guidobono


Usuarios vendedores de MercadoLibre
Cargar 10 usuarios/vendedores de MercadoLibre con sus respectivas
publicaciones.
- Los datos que se cargarán son:
- Nombre de usuario
- Edad (validar)
- Cantidad de productos (validar-número entero positivo).
- Número de publicaciones (validar-número entero positivo, hasta 1000).
- Tipo ("producto", "servicio", "subasta")
- Cuenta activa ("si", "no")
Se necesita saber
Tema A:
1. Cantidad de usuarios con la cuenta activa cuyo producto sea del tipo
“producto”, cuya edad esté entre 25 y 35 años inclusive.
2. Nombre y tipo del usuario de menor edad con más de 500 publicaciones.
3. Porcentaje de publicaciones de tipo subasta.
4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron
del tipo “producto”.
5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre
“activa”.


'''

#_ SCRIPT USUARIOS/VENDEDORES MERCADOLIBRE

MAX_USERS = 10

cant_users = 0
cant_user_activos_producto = 0

cant_subasta = 0
cant_producto = 0
cant_servicio = 0

sum_edades_tipo_producto = 0

menor_edad = None   
nombre_menor_edad = 'None'
tipo_menor_edad = 'None'

max_publicaciones = None
tipo_max_publicaciones = 'None'



while cant_users < MAX_USERS:
    
    #!______________________ INGRESO Y VALIDACION DE DATOS __________________________
    
    nombre_user = input('Ingrese el nombre de usuario: ')
    
    #valido por mayor de 18 anios y menor de 99
    edad = int(input(f'Ingrese la edad de {nombre_user} (mayor de 18): '))
    while edad < 18 or edad > 99: 
        edad = int(input('ERROR: ingrese nuevamente la edad (mayor de 18): '))
    
    
    num_productos = int(input('Ingrese la cantidad de productos: '))
    while num_productos < 0:
        num_productos = int(input('ERROR: Ingrese nuevamnte la cantidad de productos (número entero positivo): '))
        
        
    num_publicaciones = int(input(f'Ingrese el numero de publiacciones de {nombre_user}: '))
    while num_publicaciones < 0 or num_publicaciones > 1000:
        num_publicaciones = int(input(f'ERROR: Ingrese nuevamente el numero de publiacciones: '))
    
    tipo = input('Ingrese el tipo ("producto", "servicio", "subasta"): ')
    while tipo != 'producto' and tipo != 'servicio' and tipo != 'subasta':
        tipo = input('ERROR: Ingrese nuevamente el tipo ("producto", "servicio", "subasata"): ')
        
    status_cuenta = input('La Cuenta se encuentra activa (si/no):')
    while status_cuenta != 'si' and status_cuenta != 'no':
        status_cuenta = input('ERROR: La Cuenta se encuentra activa (si/no): ')
        
    
    
    #1. Cantidad de usuarios con la cuenta activa cuyo producto sea del tipo “producto”, cuya edad esté entre 25 y 35 años inclusive. 
    if status_cuenta == 'si':
        
            if tipo == 'producto' and (edad >= 25 and edad <= 35):
                cant_user_activos_producto += 1
        
    #5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre “activa”.
            if max_publicaciones == None or num_publicaciones > max_publicaciones:
                max_publicaciones = num_publicaciones
                tipo_max_publicaciones = tipo
                
        

    
    #2. Nombre y tipo de publicación del usuario de menor edad con más de 500 publicaciones.
    if num_publicaciones > 500:
        
        if menor_edad == None or edad < menor_edad:
            nombre_menor_edad = nombre_user
            tipo_menor_edad = tipo
            menor_edad = edad
            
    
    if tipo == 'subasta':
        cant_subasta += 1
    else:
        if tipo == 'producto':
            cant_producto += 1
            sum_edades_tipo_producto += edad
            
        else:
            cant_servicio += 1  
        
    cant_users +=1
    print('\n')




if MAX_USERS > 0:  
    porcentaje_subasta = (cant_subasta / MAX_USERS) * 100  #3. Porcentaje de publicaciones de tipo subasta.   
    prom_edad_producto = sum_edades_tipo_producto / MAX_USERS #4.Promedio de edad de los usuarios cuyas publicaciones fueron del tipo “producto”
else:
    porcentaje_subasta = 'None'
    prom_edad_producto = 'None'

print('='*100)
print(f'''
1. Cantidad de usuarios con la cuenta activa cuyo producto sea del tipo “producto”, cuya edad esté entre 25 y 35 años inclusive: {cant_user_activos_producto}

2. Nombre y tipo de publicación del usuario de menor edad con más de 500 publicaciones: 

    - Nombre:   {nombre_menor_edad}
    - Tipo:     {tipo_menor_edad}
      
3. Porcentaje de publicaciones de tipo subasta: {porcentaje_subasta}%

4. Promedio de edad de los usuarios cuyas publicaciones fueron del tipo “producto”: {prom_edad_producto}
      
5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre “activa”: 

    - tipo:     {tipo_max_publicaciones}
    - cantidad: {max_publicaciones} 

''')
    
print('='*100)
    
