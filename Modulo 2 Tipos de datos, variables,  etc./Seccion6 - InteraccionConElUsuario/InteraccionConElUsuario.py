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


nombre = input("Dame tu nombre: ")
num = int(input("Cuantas veces quieres que aparezca tu nombre?"))

print("Ok ",nombre, "El numero de veces que aparecera tu nombre es: ", num * nombre ,sep="T\n", end="T\n")

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

print("\n¡Eso es todo, amigos!")





"""LAB OPERADORES Y EXPRESIONES"""


hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hour, ":", mins, sep='')
