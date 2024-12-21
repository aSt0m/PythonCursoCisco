#   dev: Tomás Gutiérrez Trejo
#   program: parte  del curso de python de Skill for All sobre condicionales (Ejemplos)

"""Ejemplo 1 Como identificar el mayor de los dos numeros"""

#

number1 = int(input("Dame el primer numero: "))
number2 = int(input("Dame el segundo numero: "))

if number1 > number2:
    largest_number = number1
else:
    largest_number = number2

print("The number largest is",largest_number)