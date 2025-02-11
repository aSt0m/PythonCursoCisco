#Sección 2 del curso de Python de skillforall sobre bucles en Python

# "Bucles en Python"



# # Almacena el actual número más grande aquí.
# largest_number = -999999999

# # Ingresa el primer valor.
# number = int(input("Introduce un número o escribe -1 para detener: "))

# # Si el número no es igual a -1, continuaremos
# while number != -1:
#    # ¿Es el número más grande que el valor de largest_number?
#    if number > largest_number:
#        # Sí si, se actualiza largest_number.
#        largest_number = number
#    # Ingresa el siguiente número.
#    number = int(input("Introduce un número o escribe -1 para detener: "))

# # Imprime el número más grande.
# print("El número más grande es:", largest_number)


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
    
    
"Fundamentos del bucle for - contando lentamente (mississippi)"
#import time
#
#
#for i in range(1,6):
#    time.sleep(.5)
#    print(i," Mississippi")
#print("Lista o no, aquí vengo!")


"BREAK Y CONTINUE en el ciclo for"

# Example of Break

# print("Sentencia break")
# for i in range(1,6):
#     print("Ciclo for", i)
#     if i == 3:
#         print("Se ejecutará una sentencia 'break'")
#         break
# print("Fuera del ciclo")


# print("Sentencia continue")
# for i in range(1,6):
#     print("Valor de i es: ", i )
#     if i == 2:
#         print("Se ejecutará una sentencia 'continue'")       
#         continue
#     if i == 4:
#         print("Se ejecutará una sentencia 'continue'")       
#         continue
# print("Fuera del ciclo")
    

    


#----------------------------------------------------------------------

# counter = 1
# while counter != 100:
#     print("Dentro del bucle." , counter)
#     counter += 1
#     if counter == 30:
#         print("Counter llego a ", counter)
#     elif counter == 31:
#         print("counter es igual a:", counter)
# print("Fuera del bucle while porque llego al numero", counter)

# _________________________________________________
# counter = 3
# while counter:
#     print("Dentro del bucle", counter)
#     counter -= 1
# print("fuera del bucle", counter)

# .....................................................
# secret_number = 5
# number = int(input("ingresa un numero"))
# while secret_number != number:
#     print("Ja ja! Estas atrapado en mi bucle")
#     number = int(input("Ingresa un nuevo numero"))
# print("Hecho, muggle! Eres libre ahora")


# """
# ****************************************
# * Estos son ejercicios con for         *
# *                                      *
# *                                      *
# ****************************************

# """

"""Sentencia break - atrapado en un blucle"""


# input_word = str(input("Escribe una palabra para adivinar la palabra oculta: "))
# word_hidden  = "chupacabras"
# while word_hidden:
#     if input_word == word_hidden:
#         break
#     else:
#         print("La palabra ", input_word , " No es la palabra oculta")
#         input_word = str(input("Escribe una palabra para adivinar la palabra oculta"))
        
# print("has dejado el ciclo")


"""Sentencia continue - el Feo Devorador de Vocales"""
# Programa que usa un bucle for con un condicional (if-elif-else) y la sentencia continue
# El programa pide al usuario que ingrese la palabra utiliza el metodo .upper() para convertir la palabra en mayusculas 
# utilizar la instruccion continue para devorar las vocales, despues imprimir las palabras sin las vocales devoradas

# user_word = str(input("Ingresa una palabra: "))
# user_word = user_word.upper()
# user_word_final = ""
# for vowel in user_word:
#     if vowel == "A":
#         continue    
#     elif vowel == "E":
#         continue
#     elif vowel == "I":
#         continue
#     elif vowel == "O":
#         continue
#     elif vowel == "U":
#         continue
#     user_word_final += vowel
#     print("letra dentro del ciclo for: ", vowel)
# print(user_word_final)



# Bloque while y el bloque else

# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("Bloque else:" , i)


"""Bloque for y bloque else"""

# for i in range(5):
#     print(i)
# else:
#     print("else: ", i)


"""Pregunta 1: Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:"""


# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)
#         # Línea de código.

"""
    
Pregunta 3: Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea. Usa el esqueleto de abajo:

"""
    
   
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")


"""Pregunta 2: Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:"""


# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1


"""Pregunta 4: Crea un programa con un bucle for y una sentencia continue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla. Usa el esqueleto de abajo:"""

# for digit in "0165031806510":
#     if digit == "0":
#         print("X", end="")
#         continue
#     print(digit, end="")

 