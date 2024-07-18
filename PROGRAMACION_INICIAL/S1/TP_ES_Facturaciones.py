#+--------------------+          
#|TP: ES_Facturaciones|
#+--------------------+
#@FacuGuidobono
#
#      -------- ENUNCIADO ----------
#Para el departamento de facturación:
# A. Ingresar tres precios de productos y mostrar la suma de los mismos.
# B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
# C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).

import time
import os

#+----------------------------------------------------------------------------+          
#| FUNCION PARA ESPERAR CONFIRMACION DE USUARIO PARA CONTINUAR CON EL PROGRAMA|
#+----------------------------------------------------------------------------+
def msg_continuar() -> None:
    input("\nPresione enter para continuar...") 
    clear_console() 

#+--------------------------------+          
#|FUNCION QUE LIMPIA LA CONSOLA   |
#+--------------------------------+  
def clear_console(tiempo: float = 1.2) -> None:
    time.sleep(tiempo)
    os.system("cls") & os.system("clear")

#+----------------------------------+          
#|CREA UN MSG DE ERROR PERSONALIZADO|
#+----------------------------------+
def msg_error(text: str = 'Opción inválida!!!') -> None:
    print(f"{text}\n")
    msg_continuar()
    clear_console()

#+-----------------------------------+          
#|IMPRIME UN TEXTO DENTRO DE UNA CAJA|
#+-----------------------------------+
def print_box(text: str = 'Ingrese su texto') -> None:
    text_length = len(text)
    print("+" + "-" * (text_length + 2) + "+")
    print("|" + f" {text} ".center(text_length + 2) + "|")
    print("+" + "-" * (text_length + 2) + "+")

# +----------------------------------------------+
# |     CREA MENU DE OPCIONES PERSONALIZADO      |  
# +----------------------------------------------+
def menu_principal(opciones: list, title: str = "MENU PRINCIPAL", salir: str = 'Salir') -> int:
    while True:
        clear_console()
        print_box(f"    {title}   ")  # imprimo el nombre del menú
        
        for i, option in enumerate(opciones, start=1):
            print(f"{i}. {option}")
        
        print(f"0. {salir}\n")
        
        try:
            opcion = int(input("Ingrese una opción: "))
            if 0 <= opcion <= len(opciones):
                clear_console()
                return opcion
            else:
                msg_error()
        except ValueError:
            msg_error()

# +----------------------------------------------+
# |        REALIZA LA SUMA DE 3 NUMEROS          |
# +----------------------------------------------+
def sum_nums(a: float, b: float, c: float) -> float:
    return a + b + c

# +--------------------------------------------------+
# |       REALIZA EL PROMEDIO DE 3 NUMEROS           |
# +--------------------------------------------------+
def avg_nums(a: float, b: float, c: float) -> float:
    return sum_nums(a, b, c) / 3

# +--------------------------------------------------+
# |       REALIZA LA SUMA Y LE AGREGA EL IVA         |
# +--------------------------------------------------+
def sum_with_iva(a: float, b: float, c: float) -> float:
    return sum_nums(a, b, c) * 1.21

#  + ---------------------------------------------+
#  | CARGA DE DATOS POR EL USUARIO CON VALIDACION |
#  +----------------------------------------------+
def carga_nums() -> tuple:
    while True:
        try:
            a = float(input("Ingrese el primer número (positivo): "))
            b = float(input("Ingrese el segundo número (positivo): "))
            c = float(input("Ingrese el tercer número (positivo): "))
            
            if a > 0 and b > 0 and c > 0:    # Por simplicidad solo se permiten N° positivos
                return a, b, c
            else:
                msg_error("Error: Ingrese solo números positivos.")
        except ValueError:
            msg_error("Error: Ingrese un número válido.")


def main():
    while True:
        # lista de opciones para el menú
        opciones = [
            'Ingrese tres precios de productos para mostrar la suma de los mismos.',
            'Ingrese tres precios de productos para mostrar el promedio de los mismos.',
            'Ingrese tres precios de productos para sumarlos y mostrar el precio final (más IVA 21%).'
        ]
        
        print_box('BIENVENIDO A TP: ES_Facturaciones') # Mensaje de bienvenida
        time.sleep(0.5)
        
        opcion = menu_principal(opciones) # crea un menú con las opciones anteriores
        
        if opcion == 0:
            break
        elif opcion == 1:
            a, b, c = carga_nums()
            print(f"Precio Total: {sum_nums(a, b, c)}")
        elif opcion == 2:
            a, b, c = carga_nums()
            print(f"Promedio de precios: {avg_nums(a, b, c)}")
        elif opcion == 3:
            a, b, c = carga_nums()
            print(f"Precio final mas IVA : {sum_with_iva(a, b, c)}")
        else:
            msg_error("Opción inválida") # no se debería ejecutar nunca

        msg_continuar()

if __name__ == '__main__':
    main()
