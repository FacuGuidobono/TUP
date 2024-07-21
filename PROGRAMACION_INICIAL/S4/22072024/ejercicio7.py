'''
nombre: Facundo
apellido: Guidobono
---
TP: Bucles 07
---
Enunciado:

Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.


'''




suma = 0 
producto = 1  

while True:
    
    
    num = int(input(f"Ingrese un numero: "))
    
    if num < 0:
        producto = producto * num
    else:
        suma = suma + num
    
    op = input("¿Desea ingresar otro numero? (s/n): ") 
    
    if op.lower() == 'n': #solo evaluo la condicion de salida 
        break  # Utilizo break como ejemplo
        

if producto == 1:
    producto = 'No se ingresaron numeros negativos'

print('='*40)
print(f'''
La suma de los numeros positivos es: {suma}
El producto de los numeros negativos es: {producto}
''')
print('='*40)