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

# numbers = [111, 7, 2, 1]
# print(len(numbers))     # Imprimimos la loongitud de numbers = 4
# print(numbers)          # imprime [111, 7, 2, 1]

# ###

# numbers.append(4)       # Agrega el valor 4 al final de la lista

# print(len(numbers))     # Imprime la longitud de numbers = 5 despues de agregar 4
# print(numbers)          # Inmprime [111,7, 2, 1, 4]

# ###

# numbers.insert(0, 222)  # Agrega en el indice 0 el valor de 222
# print(len(numbers))     # Imprime la longitud de numbers ahora 6 
# print(numbers)          # Imprime [222, 111, 7, 2, 1, 4]


"""
Agregando elementos a una lista vacia
"""

# my_list = []

# for i in range(5):
#     my_list.append(i + 1)
    
# print(my_list)


# my_list = []

# for i in range(5):
#     my_list.insert(-1, i)
    
# print(my_list)

# new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(new_list)
# new_list.insert(9, 777)
# print(new_list)
# for list in new_list:
#     print(list)
#     if list == 777:
#         print("777, es el valor en este momento del ciclo")
    
# print(new_list)

# new_list.append(999)
# print(new_list)

"""Eliminando elementos de una listas"""

# new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# del new_list[1]
# print(new_list)


"""
Lab LIstas 1
- escribir una linea de codigo que solicite al usuario que reemplace el numero central en la lista con un numero entero ingresado por el usuario (paso 1)
- escribir una linea de codigo que elimine el ultimo elemento de la lista (paso 2)
- escribir una linea de codigo que imprima al longitud de la lista existente (paso 3)
"""


# hat_list = [1,  2, 3, 4, 5]
# print("La lista de numeros que esta en el sombrero es: 1,2,3,4,5")
# num_select = int(input("Dame el numero entero para intercambiar por el numero 3: "))
# print("El numero cambiado fue el", hat_list[2]," fue el numero ", num_select  )
# hat_list[2] = num_select
# del hat_list[-1]
# print("La longitud de la lista es: ", len(hat_list))
# print(hat_list)

# my_list = [1,2,3,4,5]

# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]

 
# print(my_list)

# my_list = [10, 1, 8, 3, 5]
# print(my_list) 
# my_list[0], my_list[4] = my_list[4], my_list[0] # 10, 5 = 5, 10  
# my_list[1], my_list[3] = my_list[3], my_list[1] # 1, 3 = 3, 1
 
# print(my_list)

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,102,103]

# length = len(my_list)
# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
# print(my_list)
# print(length // 2)

'''
LAB fundamentos de las listas: los beatles
* paso 1: crea una lista vacia llamada beatles;
* paso 2: emplea el metodo append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul Mackartney y George Harrison;
* paso 3 emplea el bucle for y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista Stu Sutcliffe y Pete Best;
* paso 4: usa la instruccion del para eliminar a Stu SucCliffe y Pete Best de la lista:
* paso 5: usa el metodo insert() para agregar a Ringo Starr al principio de la lista
;
'''

# beatles = []
# print(beatles.append("John Lennon"),beatles)
# print(beatles.append("Ringo Starr"),beatles)
# print(beatles.append("Paul McCartney"), beatles)
# print(beatles.append("George Harrison"), beatles)
# length = len(beatles)
# for i in range(1):
#     music_man = str(input("Dame el nombre de primer integrante: "))
#     print(beatles.append("John Lennon"),beatles)
#     beatles.append(music_man)
#     music_man2 = str(input("Dame el nombre de otro integrante: "))
#     beatles.append(music_man2)
# print(beatles)
# del beatles[-1]
# print(beatles)
# del beatles[-1]
# print(beatles)

'''
Metodo sort() para ordenar listas

'''

# fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]

# print(fruits)
# fruits.sort()
# print(fruits)


"""_

Metodo reverse() sirve para invertir la lista

"""

# fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
# print(fruits)
# for i in range(len(fruits)):

#     fruits.reverse()
    
# print(fruits)

"""
Ejemplo con sort()    
"""

# my_list = ["R", "M", "J", "Z","K"]
# my_list.sort()
# print(my_list)



# list_1 = [1]
# print("list_1 = [1]:     ", list_1)
# list_2 = list_1
# print("list_2 = list_1:  ", list_2)
# list_1[0] = 2
# print("list_1[0] = 2:     ",list_1[0])
# print("list_2:           ",list_2)



# print("-------------SEPARADOR-----------------------")

# list_1 = [1]
# print("list_1 = [1]  |    ", list_1)

# list_2 = list_1[:]
# print("list_2 = list_1[:] | ", list_2)

# list_1[0] = 2
# print(list_1[0])
# print(list_2)

"""
Operaciones con listas

"""

# nombres = ["Juan", "Carlos", "Abraham", "Ramiro", "Luis", "Fernando"]
# print("Mi lista original es: ", nombres)
# print("Lista con nombres[1:3] es: ", nombres[1:3])
# del nombres[1:2]
# print("Lista con del nombres[1:2] es: ", nombres)



"""
Operadores in y not in
"""

# nombres = ["Juan", "Carlos", "Abraham", "Ramiro", "Luis", "Fernando"]
# print("wences" in nombres) #Nos regresara False
# print("Juan" in nombres)    I#Nos regresara True python distingue entre mayusculas y minusculas



"""
Encontrar el valor mas grande en una lista con python

"""

# my_list = [3, 3, 22, 32, 51, 1, 3, 32]
# largest = my_list[0]
# for elem in my_list[1:]:
#     if elem > largest:
#         print(elem)
#         largest = elem
#     else:
#         print("El ",elem, "Este numero es menor que el elemento de la lista")
# print("El numero mas grande es: ", largest)



"""
Encontrar la ubicacion de un elemento de una lista
"""

# my_list = [3, 3, 22, 32, 51, 1, 3, 32]
# to_find = 51
# found = False

# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#          break
# if found:
#     print("Elemento encontrado en el indice ", i)
# else:
#     print("ausente")



"""
Comparar dos listas 
"""

# list_one = [3, 3, 22, 32, 51, 1, 3, 32]
# list_two = [9, 32, 92, 28, 31, 2, 9, 2]
# match = 0

# for num in range(len(list_two)):
#     if num in list_one:
#         match += 1
# print(match)
        
        
'''
LAB Operaciones con listas

Escenario
Imagina una lista - no muy larga ni muy complicada, solo una lista simple que contiene algunos números enteros. Algunos de estos números pueden estar repetidos, y esta es la clave. No queremos ninguna repetición. Queremos que sean eliminados.

Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.

Nota: Asume que la lista original está ya dentro del código - no tienes que ingresarla desde el teclado. Por supuesto, puedes mejorar el código y agregar una parte que pueda llevar a cabo una conversación con el usuario y obtener todos los datos.

Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo temporal - no necesitas actualizar la lista actual.

No hemos proporcionado datos de prueba, ya que sería demasiado fácil. Puedes usar nuestro esqueleto en su lugar.
'''


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

new_list = my_list[:]


for numbers in my_list:
    if new_list[numbers] in my_list:
        del my_list[numbers]
       
print("La lista con elementos únicos:")
print(my_list)



