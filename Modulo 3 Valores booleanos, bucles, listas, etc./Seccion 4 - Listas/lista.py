"""Asignacion de un nuevo valor (111) al primer elemento de la lista
"""
    
# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista:", numbers)

# numbers[0] = 111
# print("Nuevo contenido de la lista:", numbers)

# numbers[1] = numbers[4]
# print("Cambio de posición de 2 a 5", numbers)

""" Ejemplo: copiar el valor del quinto elemento al segundo elemento"""

# master_list = ["caballo", "perro", 1, 'sopa', 100, 28]
# print(master_list)
# for list in master_list:
#     print(list)
        
        
        
"""Ejemplo con len (sirve para saber la logitud de la lista)"""

# master_list = ["caballo", "perro", 1, 'sopa', 100, 28]
# print(len(master_list))


"""Ejemplo con del (sirve para borrar algún elemento de la lista)"""

# master_list = ["caballo", "perro", 1, 'sopa', 100, 28]
# print(master_list)
# print(len(master_list))
# del master_list[1]
# print(master_list)
# print(len(master_list))

"""Ejemplo con indices negativos sirven para identificar el ultimo indice"""

# number = [111, 7, 2, 1]
# last_index = number[-1]
# print(last_index," Es el ultimo indice de la lista")


# number = [111, 7, 2, 1]
# second_last = number[-4]
# print(second_last)


"""Lab Los fundamentos de las listas"""

"""
- Escribir una linea de código que solicite al usuario que reemplace el número  central en la lista con un número entero ingresado por el usuario
- Escribir una línea de código que elimine el último elemento de la lista
- Escribir una línea de código que imprima la longitud de la lista existente
"""
 


"""Funciones VS Metodos"""

numbers = [111, 7, 2, 1]
print(len(numbers))     # Imprimimos la loongitud de numbers = 4
print(numbers)          # imprime [111, 7, 2, 1]

###

numbers.append(4)       # Agrega el valor 4 al final de la lista

print(len(numbers))     # Imprime la longitud de numbers = 5 despues de agregar 4
print(numbers)          # Inmprime [111,7, 2, 1, 4]

###

numbers.insert(0, 222)  # Agrega en el indice 0 el valor de 222
print(len(numbers))     # Imprime la longitud de numbers ahora 6 
print(numbers)          # Imprime [222, 111, 7, 2, 1, 4]