#Sección 2 del curso de Python de skillforall sobre bucles en Python

"Bucles en Python"



# Almacena el actual número más grande aquí.
#largest_number = -999999999
#
## Ingresa el primer valor.
#number = int(input("Introduce un número o escribe -1 para detener: "))
#
## Si el número no es igual a -1, continuaremos
#while number != -1:
#    # ¿Es el número más grande que el valor de largest_number?
#    if number > largest_number:
#        # Sí si, se actualiza largest_number.
#        largest_number = number
#    # Ingresa el siguiente número.
#    number = int(input("Introduce un número o escribe -1 para detener: "))
#
## Imprime el número más grande.
#print("El número más grande es:", largest_number)


"Más ejemplos con while"

#Un programa que lee una secuencia de números 
#y cuenta cuántos números son pares y cuántos son impares.
#El programa termina cuando se ingresa un cero

#odd_numbers = 0
#even_numbers = 0
#
## Lee el primer número
#number = int(input("Introduce un número o escribe 0 para detener:  "))
#
## 0 termina la ececución
#
#while number != 0:
#    #Verificar si el número es impar
#    if number % 2 == 1:
#        # Incrementar el contador de números impares odd_nummbers.
#        odd_numbers += 1
#    else:
#        # Incrementar el contador de números pares even_numbers.
#        even_numbers += 1
#        # Leer el siguiente número.
#    number = int(input("Introduce un número o escribe 0 para detener:   "))
#    
#    #Imprimir resultados
 
 
"Empleando la variable counter para salir del bucle"


#counter = 5
#while counter != 0:
#    print("Dentro del bucle.",counter)
#    counter -= 1
#print("Fuera del bucle.",counter)

"Otra manera de hacerlo"

#counter = 5
#while counter:
#    print("Valor en bucle", counter)
#    counter -= 1
#print("Valor en bucle fuera: ", counter)



"LAB Adivina el número secreto"

#secret_number = 777
#number = int(input("Ingresa un número entero"))
#while secret_number != number:
#    print("Ja, Ja! ")
#
#    number = int(input("Ingresa un número entero"))
#print("Bien hecho, muggle! Eres libre ahora")
#    
    
"Bucles en tu código con for"

# Estructura del bucle for

#i = 0
#while i < 100:
#    # do something()
#    i += 1
#    print("El ciclo empieza en:  ", i)
#print("Termino el ciclo while")
#
#
#for i in range(100):
#    # do something
#    pass
#

#for i in range(10):
#    print("El valor de i es: ", i)


#number = int(input("Ingresa el numero de la tabla de multiplicar que deseas: "))
#
#
#for a in range(1, 10):
#    #for b in range(10):
#        print(a, "X" , number , "=" , a*number)
 
 
"Funcion range() con tres argumentos"
 
#for i in range(2, 8, 2):
#    print("El valor de i es:  ", i)
 
 
"Programa de potencias de dos"

#power = 1
#
#for expo in range(16):
#    print("2 a la potencia de ", expo, "es ", power)
#    power *= 2
    
    
"Fundamentos del bucle for - contando lentamente (mississippily)"
#import time
#
#
#for i in range(1,6):
#    time.sleep(.5)
#    print(i," Mississippi")
#print("Lista o no, aquí vengo!")


"BREAK Y CONTINUE en el ciclo for"
