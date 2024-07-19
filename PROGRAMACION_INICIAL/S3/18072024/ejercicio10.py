'''
nombre: Facundo
apellido: Guidobono
---
TP: Condicionales 10
---
Enunciado:

Ingresar el sueldo, estado civil (casado o soltero) y cantidad de hijos de un empleado. 
Determinar si el empleado debe o no pagar el impuesto a las ganancias. 
El mismo no se pagará si el empleado es casado con hijos y sus ingresos son menores a $2200000.



'''


sueldo = float(input("Ingrese su sueldo: "))
estado_civil = input("Ingrese su estado civil (casado/soltero): ")
cantidad_hijos = int(input("Ingrese la cantidad de hijos: "))

msg = "Debe pagar el impuesto a las ganancias."

if estado_civil == "casado" and cantidad_hijos > 0 and sueldo < 2200000:
    msg = "No debe pagar el impuesto a las ganancias."
    
print(msg)