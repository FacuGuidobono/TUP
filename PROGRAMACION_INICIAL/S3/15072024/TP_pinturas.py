'''
nombre: Facundo
apellido: Guidobono
---
TP: ES_Pinturas
---
Enunciado:

2.	Para el departamento de Pinturas:
	A.	Al ingresar una temperatura en Fahrenheit debemos mostrar la temperatura en Centígrados con un mensaje concatenado 
        (0 °F − 32) × 5/9 = -17,78 °C

    B.	Al ingresar una temperatura en Centígrados debemos mostrar la temperatura en Fahrenheit 
        (0 °C × 9/5) + 32 = 32 °F

'''
#Convertir de F a C
print('-'*100)
fahrenheit = float(input('Ingrese una temperatura en grados Fahrenheit para mostrarla en Celsius: '))
celsius = (fahrenheit - 32) * 5/9
print('(' + str(fahrenheit) + '°F − 32 × 5/9) = ' + str(celsius)+ '°C')

print('-'*100)

#Convertir de C a F
celsius = float(input('Ingrese una temperatura en grados Celsius para mostrarla en Faherenheit:'))
fahrenheit = (celsius * 9/5) + 32
print('(' + str(celsius) + '°C × 9/5) + 32 = ' + str(fahrenheit)+ '°F')
print('-'*100)

