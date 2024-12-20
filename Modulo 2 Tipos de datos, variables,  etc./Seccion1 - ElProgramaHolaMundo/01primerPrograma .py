# Developer: Tom Trejo
# Name: primerPrograma.py
# Programa que analiza a detalle la función print() 



"""
En este ejercicio podemos ver que la invocacion vacia de la función print() genera una linea vacia, 
en el siguiente ejemplo veremos que no es la única forma de producir una nueva linea


print('La Witsi Witsi Araña subío a su telaraña.')
print()
print('Vino la  lluvia y se la llevo')
"""


#En este ejercicio se muestra la otra forma para realizar un salto de lineea
#La barra invertida (\)tiene un significado muy especial cuando se usa dentro de cadenas , 
#se llama caracter de escape
#La palabra escape debe entenderese especifilcamente significa que la seria de caracteres 
# en la cadena se esccapa por un momento(un momento muy breve) para introducir un caracter 
# muy especial. La letra n colacada desplues de la barra invertida previene de la palabra 
# newline

"""print("La Witse Witse Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\ny se llevo.")
print("\\")"""



#En este ejemplo tiene 3 argumentos y los tres son cadenas 

"""print("La Witsi Witsi Araña","subio","a su telarania")"""

#En este ejemplo, la forma en la que se estan pasando los argumentos a la funcion print() es 
# mas comun en Python, y se llama la forma posicional. Este nombre proviene del hecho de que 
# el significado del argumento esta dictado por su posicion (por ejemplo, el segundo argumento se 
# mostrara despues del primero, no al reves)

"""print("Mi nombre es:","Python.")
print("Monty Python")"""


# Argumentos de palabras clave
# Para usar este debe de contar con los siguientes requerimientos como son: agregarse 
# al final del ultimo argumento, debe contener la palabra clave (end) junto con el 
# signo de (=) y entre comillas si es una cadena el valor que estara como argumento 
# final, el argumento end se colocara en el lugar tres de tres argumento o en el ultimo lugar, 
# el argumento sep quiere decir separador y este argumento se colocara entre el primer
# argumento y el segundo

"""print("Mi nombre es:", "Python.", end=" end ")
print("Mi nombre es:", "Python.", sep=" sep ")
print("Monty Python.")"""



#Este ejemplo es para ver como interactuar con los argumentos, el resultado es predecible


print("Mi", "nombre", "es", sep="_",end="*")
print("Monty","Python.",sep="*",end="\n")

print("Mi","Nombre","es:", sep="_", end="Tom")