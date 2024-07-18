'''
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

#_Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces #_(DC y AB) del mismo material para mantener la forma del cometa.

#_El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.

#_Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.
@FacuGuidobono
'''

print('-'*100)
print('JUGUETERIA EL MUNDO DE CHARLY'.center(80))
print('-'*100)

print('''
      
Programa para confeccionar un cometa
      
         B
         ^
       / | \
     /   |   \
    D---------C
     \   |   /
      \  |  /
       \ | /
        \|/
         v
         A
         
Medidas Requeridas:
AB = Diagonal mayor
DC = Diagonal menor
BD y BC = Lados menores
AD y AC = Lados mayores

      ''')

print('='*100)

#_ ingreso de datos

ab = float(input('Ingrese el tamaño de la diagonal mayor(AB): '))
dc = float(input('Ingrese el tamaño de la diagonal menor(DC): '))
bd_bc = float(input('Ingrese el tamaño del lado menor(BD/BC): '))
ad_ac = float(input('Ingrese el tamaño del lado mayor(AD/AC): '))




