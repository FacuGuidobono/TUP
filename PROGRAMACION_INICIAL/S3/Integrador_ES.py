'''
#_ ENUNCIADO:
#_ 🔔Integrador !
#_La juguetería El MUNDO DE CHARLY nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

#*CONFECCIÓN DE UN COMETA: 

#!          B
#!          ^
#!       // | \\
#!      //  |  \\
#*     D---------C
#?     \\   |   //
#?      \\  |  //
#?       \\ | //
#?        \\|//
#?          v
#?          A

#!Medidas:

#* AB = Diágonal mayor
#* DC = Diágonal menor
#! BD y BC = lados menores
#? AD y AC = lados mayores

#! El usuario ingresará las medidas  BC, CD y DA.

#_ Detalles de construcción

#_Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.

#_El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.

#_Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.

@FacuGuidobono
'''

#_ presentacion del programa

print('='*100)
print('JUGUETERIA EL MUNDO DE CHARLY'.center(100))
print('='*100)


# utilizo \\ para que no se interpreten como secuencias de escape
#probe 100 veces para que salga alineado 
print('''  
PROGRAMA PARA CONFECCIONAR UN COMETA
      
        B
        ^
      / | \\
    /   |   \\
   D---------C                
    \\   |   /
     \\  |  /
      \\ | /
       \\|/
        v
        A
         
Medidas Requeridas:
AB = Diagonal mayor
DC = Diagonal menor
BD y BC = Lados menores
AD y AC = Lados mayores

      ''')

print('='*100)

#_ Cantidad de cometas para produccion en masa
CANTIDAD_DE_COMETAS = 10

#_----------------------
#_ ingreso de datos
#_----------------------

ab = float(input('Ingrese el tamaño de la diagonal mayor AB (cm): '))
dc = float(input('Ingrese el tamaño de la diagonal menor DC (cm): '))

#todo los valores de los lados deberian ser acotados respecto a los de las diagonales para poder mantener la forma del cometa confiemos en el buen criterio del user

bd_bc = float(input('Ingrese el tamaño de los lados menores BD/BC (cm): '))
ad_ac = float(input('Ingrese el tamaño de los lados mayores AD/AC (cm): '))


#_----------------------------------
#_ calculo total varillas 
#_----------------------------------

#_perimetro externo del cometa
perimetro_total_exterior = 2 * (bd_bc + ad_ac)

#_entre cruces
entre_cruces = ab + dc


total_varillas_en_metros = (perimetro_total_exterior + entre_cruces) * (10**-2)  #!convercion en metros
total_varillas_en_metros = round(total_varillas_en_metros, 2) 


#_---------------------------------
#_ calculo del papel necesario
#_---------------------------------

#?Calculo en base al perimetro, pero yo calcularia en base al area del cometa

#_ perimetros internos del cometa
perimetro_superior = 2*bd_bc + dc  #triangulo superior  bc//bd//dc
perimetro_inferior = 2*ad_ac + dc  #triangulo inferior  ad//ac//dc

total_sin_cola = (perimetro_inferior + perimetro_inferior)*(10**-2) #!conversion a metros
cola_del_cometa = 0.1 * total_sin_cola  # 10% del total del cuerpo

#_ total del papel
total_metros_de_papel = total_sin_cola + cola_del_cometa
total_metros_de_papel = round(total_metros_de_papel,2)



print('='*100)
print(f'Total de metros (m) de varillas de plastico necesarios para producir {CANTIDAD_DE_COMETAS} cometas: {CANTIDAD_DE_COMETAS * total_varillas_en_metros}m')     
print(f'Total de metros (m) de papel necesarios para producir {CANTIDAD_DE_COMETAS} cometas: {CANTIDAD_DE_COMETAS * total_metros_de_papel}m')     
print('='*100)




























