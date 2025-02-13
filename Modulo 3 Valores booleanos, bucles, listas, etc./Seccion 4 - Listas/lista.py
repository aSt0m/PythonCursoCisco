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

master_list = ["caballo", "perro", 1, 'sopa', 100, 28]
print(master_list)
print(len(master_list))
del master_list[1]
print(master_list)
print(len(master_list))