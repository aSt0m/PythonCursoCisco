
"OPERADORES"



#var = 0
#print(var == 0)
#var = 1
#print( var == 0 )

"DESIGUALDAD"
"El operador != (noes igual a ) tambien compara los valores de dos operandos"


#var = 0 # Asignando 0 a var
#print ( var != 0)
#
#var = 1 # Asignando 1 a var
#print( var != 0 )


#var1 = 10
#var2 = 20
#var3 = 80
#valor = 0
#
#print( var1 > var2 )
#print( var2 < var1 )
#print( var3 < var2 )
#print( var2 > var1 )
#
#
#
#n = int(input("Ingresa un numero: "))
#print( n >= 100 )
#print ( n == True )


"Condicionales y ejecución condicional"

"La primera forma de uan sentencia condicional, que puede ver a continuación"
#", esta escrita de manera muy informal pero figurada:"
#
#if true_or_not 
#    do_this_if_true
#    
#La sentencia condicional consta de los siguientes elementos, estrictamente necesarios en este orden:
#
#-1.- La palabra clave reservada if
#-2.- Uno o más espacios en blanco;
#-3.- Una expresión (una pregunta o uan respuesta) cuyo valor se interpreta unicamente en términos de True
#-    (cuando su valor no sea cero) y false (cuando sea igual a cero)ñ
#-4.- Unos dos puntos seguidos de una nuevalineañ
#-5.- Una instrucción con sangría o un conjunt de instrucciones (se requiere absolutamente al menos uan instrucción)
#    la  sangría se puede lograr de dos manerasÑ insertando un número particular de espacios
#    (la recomendación es usar cuatro espacios de sangría), o usando el tabulador, nota: si hay mas 
#    de una instrucción en la parte con sangria, la sangría deve ser la misma entodas las lineas:
#    aunque puede parecer lo mismo se se mezclan tabuladores con espacio, es importante que todas
#    las sangrías sean exactamente iguales Python 3 no permite mezclar espacios y tabuladores para la sangría
#
#¿Cómo funciona esta sentencia?
#
#Si la expresión true_or_not representa la verdad (es decir, su valor no es igual a cero), las sentencias con sangría se ejecutarán;
#Si la expresión true_or_not no representa la verdad (es decir, su valor es igual a cero), las sentencias con sangría se omitirán (ignorado), 
#y la siguiente instrucción ejecutada será la siguiente al nivel de la sangría original.


#if the_weather_is_good:
#    if nice_restaurant_is_found:
#        have_lunch()
#    else:
#        eat_a_sandwich()
#else:
#    if tickets_are_available:
#        go_to_the_theater()
#    else:
#        go_shopping()
#        
#        
#        
#if the_weather_is_good
#    go_for_a_walk()
#elif tickets_are_available:
#    go_to_the_theater()
#elif table_is_available:
#    go_for_lunch()
#else:
#    play_chess_at_home()
#    
#La forma de ensamblar las siguientes sentencias if-elif-else a veces se denomina cascada.
#
#Observa de nuevo como la sangría mejora la legibilidad del código.
#
#Se debe prestar atención adicional a este caso:
#
#No debes usar else sin un if precedente;
#else siempre es la última rama de la cascada, independientemente de si has usado elif o no;
#else es una parte opcional de la cascada, y puede omitirse;
#Si hay una rama else en la cascada, solo se ejecuta una de todas las ramas;
#Si no hay una rama else, es posible que no se ejecute ninguna de las opciones disponibles.
#Esto puede sonar un poco desconcertante, pero ojalá que algunos ejemplos simples ayuden a comprenderlo mejor.
    
    
    
    
    
"Análisis de muestas de código"


"Ejemplo 1"

#number1 = int(input("Ingresa el numero 1:  "))
#number2 = int(input("Ingresa el numero 2:  "))
#print("El primer numero que ingresaste fue: ", number1)
#print("El segundo numero que ingresaste fue: ", number2)
#
#if number1 > number2:
#    number_length = number1
#else:
#    number_length = number2
#print("El numero mas grande es: ", number_length)



"Ejemplo 2"

# Se leen dos números
#number1 = int(input("Ingresa el primer numero:  "))
#number2 = int(input("Ingresa el segundo numero:  "))

# Elige el número más grande
#if number1 > number2: number_length = number1
#else: number_length = number2

# Imprime el resultado

#print("El numero más grande es:  ", number_length)


"Ejemplo 3"

#number1 = int(input("Ingresa el primer numero:  "))
#number2 = int(input("Ingresa el segundo numero:  "))
#number3 = int(input("Ingresa el tercer numero:  "))
#
#largest_number = number1
#
#if number2 > number1:
#    largest_number = number2
#if number3 > number2:
#    largest_number = number3
#print("El numero más grande es:  ", largest_number)

"Pseudocódigo e introducción a los bucles"


#number1 = int(input("Ingresa el numero 1:  "))
#number2 = int(input("Ingresa el segundo numero:  "))
#number3 = int(input("Ingresa el tercer numero:  "))
#
#numberLength = max(number1, number2, number3)
#
#print("El numero más grande es:  ", numberLength)

#print()
#largest_number = -9999999
#number = int(input())
#if number == -1:
#    print(largest_number)
#    exit()
#if number > largest_number:
#    largest_number = number


" LAB Fundamentos de la sentencia if-else"
#
#
#print("Calculadora")
#
#ingreso = float(input("Dame el ingreso:  "))
#
#
#if ingreso <= 85528:
#    impuesto = ingreso * 0.18 - 556.2
#else:
#    impuesto = (ingreso - 85528) * 0.32 + 14839.02
#
#if impuesto < 0.0:
#    impuesto = 0.0
#    
#impuesto = round(impuesto, 0)
#print("El impuesto es:  ", impuesto, "pesos")


"LAB Fundamentos de la sentencia if-elif-else"

"Programa que nos dice si el año es bisiesto u ordinario"

#print("Programa que comprueba si el año que ingresas es bisiesto u ordinario")

#anio = int(input("Ingresa el año:  "))
#if anio < 1582:
#    print("No esta dentro del periodo del calendario Gregoriano")
#else:
#    if anio % 4 != 0:
#        print("Año común")
#    elif anio % 100 != 0: 
#        print("año bisiesto")
#    elif anio % 400 != 0:
#        print("Año común")
#    else: 
#        print("Año bisiesto")
 
 
"Programa que detecta una cadena Espatafilio"

#word = str(input("Ingresa la palabra ESPATAFILIO"))
#if word == "ESPATAFILIO":
#    print("Si - ¡El Espatafilio! es la mejor planta de todos los tiempos!")
#elif word == "espatafilio":
#    print(" No, ¡quiero un gran Espatafilio!")
#else:
#    print("¡Espatafilio!, ¡No", word )
#    



#x = 5
#if x > 5:
#    if x == 6:
#         print("anidado: x == 6")
#    elif x == 10:
#        print("anidado: x == 10")
#    else:
#        print("anidado -> else")
#else:
#    print("else")


#for variable in range(0, 9, 2):
#    print(variable)

#for i in range(10):
#    print("soy el valor: ", i)
#

#"Prueba para git"

#for varA in range(1,11):
#    for varB in range(1,11):
#        print(varA, "X", varB, "=", varA * varB )
#        if varB == 10:
#            print("\n")
#print("fuera del for")

"Las Sentencias break y continue"
#
## break - ejemplo
#
#print("la instrucción break:")
#for i in range(1, 6):
#    if i == 3:
#        break
#    print("Dentro del bucle.", i)
#print("Fuera del bucle")


# continue - ejemplo

#print("\nLa instrucción continue: ")
#for i in range(1, 6):
#    if i == 3:
#        continue
#    print("Dentro del bucle. ", i)
#print("Fuera del bucle.")

# Las sentencias break y continue: más  ejemplos

#largest_number = -99999999
#counter = 0
#
#while True:
#    number = int(input("Ingresa un número o escribe -1 para finalizar el programa:"))
#    if number == -1:
#        break
#    counter += 1
#    if number > largest_number:
#        largest_number = number
#        
#if counter != 0:
#    print("El número más grande es: ", largest_number)
#else:
#    print("No has ingresado ningún número.")
#    
    
#largest_number = -9999999
#counter = 0
#
#number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#
#while number != -1:
#    if number == -1:
#        continue
#    counter += 1
#    
#    if number > largest_number:
#        largest_number = number
#    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#if counter:
#    print("El número más grande es", largest_number)
#else:
#    print("No has ingresado ningún número.") 
#