#   dev: Tomás Gutiérrez Trejo
#   program: parte  del curso de python de Skill for All sobre condicionales (Ejemplos)

"""Ejemplo 1 Como identificar el mayor de los dos numeros"""

#

# number1 = int(input("Dame el primer numero: "))
# number2 = int(input("Dame el segundo numero: "))

# if number1 > number2:
#     largest_number = number1
# else:
#     largest_number = number2

# print("The number largest is",largest_number)


""" Ejemplo 2 """
"""Este ejemplo muestra lo mismo que el anterior pero escrito un menos lineas de codigo"""

# print("Script que detecta el numero mas grande")
# number1 = int(input("Dame el primer numero: "))
# number2 = int(input("Dame el segundo numero: "))
# 
# if number1 > number2: number_largest = number1
# else: number_largest = number2
# 
# print("El numero mas grande es ", number_largest)



""" Ejemplo 3 Encontrar el mayor de los 3 numeros  dados"""

# number1 = int(input("Dame el primer numero: "))
# number2 = int(input("Dame el segundo numero: "))
# number3 = int(input("Dame el tercer numero: "))

# largest_number = number1

# if number2 > largest_number:
#     largest_number = number2


# if number3 > largest_number:
#     largest_number = number3

# print("El numero mas grande: ", largest_number)


""" Ejemplo con funcion max()"""

# number1 = int(input("Dame el primer numero: "))
# number2 = int(input("Dame el segundo numero: "))
# number3 = int(input("Dame el tercer numero: "))

# largest_number = max(number1, number2, number3)

# print("El numero mas grande es el: ", largest_number, " con la funcion max()")

# number1 = int(input("Dame el primer numero: "))
# number2 = int(input("Dame el segundo numero: "))
# number3 = int(input("Dame el tercer numero: "))

# minor_number = min(number1,number2,number3)

# print("El numero mas pequenio es: ", minor_number)

"""Ejemplo Espatifilo"""

# name = input("Escribe el nombre de la flor: ")

# if name == "ESPATIFILO":
#     print("Si - !El Espatifilo! es la mejor planta de todos los tiempos!")
# elif name == "espatifilo":
#     print("No, Quiero un gran Espatifilo!")
# else:
#     print("Espatifilo!, No", name)
    
    
"""LAB Fundamentos de sentencia if-else"""

# Uso de la funcion round()

# income = float(input("Introduce el ingreso anual: "))

# if income < 85528:
#     tax = income * 0.18 - 556.02
# else: 
#     tax = (income - 85528) *  0.32 + 14839.02

# if tax < 0:
#     tax = 0

# tax = round(tax, 0)
# print("El impuesto es:", tax, "pesos")

"""LAB Fundamentos de if-elif-else"""

