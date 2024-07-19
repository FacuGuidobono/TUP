'''
nombre: Guidobono
apellido: Facundo
---
TP: Ferrete_lamparas
---
Enunciado:

En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la compra de lámparas de bajo consumo. 
Se tiene en cuenta que todas las lámparas cuestan $800.
A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez) se aplicará el siguiente descuento:
Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 
Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.
Mostrar por pantalla: 
Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.




'''
#_precio lamparas
COSTO_LAMPARA = 800



print('='*100)
print('FERRETE LAMPARAS - SISTEMA DE VENTAS'.center(100))
print('='*100)



#_------------------------------
#_      INGRESO DE DATOS
#_------------------------------

marca = input('Ingrese la marca de la lampara: ')
cantidad = int(input('Ingrese la cantidad de lamparas: '))

print('='*100)

#_------------------------------
#_          DESCUENTOS
#_------------------------------

importe = cantidad * COSTO_LAMPARA 

if cantidad > 5:
    descuento = importe * 0.5
    importe_final = importe - descuento

if cantidad == 5:
    descuento = importe * 0.3
    importe_final = importe - descuento
    
    if marca == 'ArgentinaLuz':
        descuento = importe * 0.4
        importe_final = importe - descuento
        
if cantidad == 4:
    descuento = importe * 0.2
    importe_final = importe - descuento
    
    if marca == 'ArgentinaLuz' or marca == 'FelipeLamparas':
        descuento = importe * 0.25
        importe_final = importe - descuento

if cantidad == 3:
    descuento = importe * 0.05
    importe_final = importe - descuento
    
    if marca == 'ArgentinaLuz':
        descuento = importe * 0.15
        importe_final = importe - descuento
        
    if marca == 'FelipeLamparas':
        descuento = importe * 0.1
        importe_final = importe - descuento


descuento_adicional = 0 # sino aplica descuento adicional   
if importe_final > 4000:
    descuento_adicional = importe * 0.05  
    importe_final = importe_final - descuento_adicional
    

#_------------------------------
#_       MUESTRA DE DATOS
#_------------------------------

    
print(f'''|
| * MARCA: {marca}                                                                                 
|                                                                                       
| * CANTIDAD DE LAMPARAS: {cantidad}                                                       
|                                                                                           
| * TOTAL SIN DESCUENTO: ${importe}                                                        
|                                                                                            
| * DESCUENTO APLICADO: ${descuento}                                                      
|                                                                                        
| * DESCUENTO ADICIONAL: ${descuento_adicional}                                                
|                                                                                       
| * PRECION FINAL CON DESCUENTO/S: ${importe_final}                                        
|     ''')
print('='*100)








