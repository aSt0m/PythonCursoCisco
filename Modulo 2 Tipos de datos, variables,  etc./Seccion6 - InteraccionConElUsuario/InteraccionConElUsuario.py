"""

INTERACCION CON EL USUARIO

"""

#numero = int(input("Dame un digito: "))
#resultado = numero ** 3 * 33
#print("El resultado es: ", resultado)2

#a = int(input("Dame un numero"))
#b = int(input("Dame otro numero"))
#c = (a**2 + b**2) ** .5  # En esta parte se eleva a la potencia .5 por que es lo mismo que una raiz
#print("El resultado es: ", c)



""" OPERADORES CADENA Y CONVERSIONES"""


# nombre = input("Dame tu nombre: ")
# num = int(input("Cuantas veces quieres que aparezca tu nombre?"))

# print("Ok ",nombre, "El numero de veces que aparecera tu nombre es: ", num * nombre ,sep="_\n", end="=>\n")

'''CONVERSIONES DE TIPOS UNA VEZ MAS'''

# ingresa un valor flotante para la variable a aquí
#val_a = float(input("Ingresa un valor flotante para la variable 'a': "))
#ingresa un valor flotante para la variable b aquí
#val_b = float(input("Ingresa un valor flotante para la variable 'b': "))

# mostrar el resultado de la suma aquí
#print("El resultado de la suma es: ", val_a + val_b)
# mostrar el resultado de la resta aquí
#print("El resultado de la resta es: ", val_a - val_b)
# mostrar el resultado de la multiplicación aquí
#print("El resultado de la multiplicacion es: ", val_a * val_b)
# mostrar el resultado de la división aquí
#print("El resultado de la division es: ", val_a / val_b)

# print("\n¡Eso es todo, amigos!")





"""LAB OPERADORES Y EXPRESIONES"""


# # hour = int(input("Hora de inicio (horas): "))
# # mins = int(input("Minuto de inicio (minutos): "))
# dura = int(input("Duración del evento (minutos): "))
# mins = mins + dura # encuentra el número total de minutos
# hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
# mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
# hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
# print(hour, ":", mins, sep='')



# anything = input("Dime lo que sea...")
# print("Hmm...", anything, "...en serio?")

"""Replicacion"""

# print("+" + "-" * 10 + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + "-" * 10 + "+")

# Salida
# +----------+
# |          |
# |          |
# |          |
# |          |
# |          |
# +----------+

"""Conversiones de tipos"""

# leg_a = float(input("Dame el primer cateto"))
# leg_b = float(input("Dame el segundo cateto"))
# print("La longitud de la hipotenusa es:" + str((leg_a ** 2 + leg_b ** 2) ** .5))


"""LAB Entradas y salidas simples"""

# value_one = float(input("Dame el valor de la variable 1 "))
# value_two = float(input("Dame el valor de la variable 2 "))

# print("suma:",  value_one + value_two)
# print("resta: ", value_one - value_two)
# print("multiplicacion", value_one * value_two)
# print("division", value_one / value_two)

# print("\nEso es todo, amigos!")


"""Operadores y expresiones"""

# x = float(input("Dame un valor: "))
# y = (1/ (x + 1 / (x + 1 / (x + (1 / x)))))
# print("Valor de y: ", y)


"""Lab Operadores y expresiones -2"""


"""La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59). El resultado debe ser mostrado en la consola.

Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16."""

hour = int(input("Hora de inicio (horas)"))
mins = int(input("Minuto de inicio (minutos)"))
dura = int(input("Duración del evento (minutos)"))

mins = mins + dura # encuentra el numero total de minutos
print(mins)
hour = hour + mins // 60# Encuentra el numero total de horas ocultas en los minutos y actualiza la hora
print(hour)
mins = mins % 60# Corrigue los minutes para que esten en un rango de  (0...59)
hour = hour % 24# Corrige las horas para que esten en un rango de (0...23)
print(hour, ":", mins, sep="")
