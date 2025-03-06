""" Funciones """

# def message():
#     print("Ingresa un valor")
    
# message()
# a = int(input())
# message()
# b = int(input())
# message()
# c = int(input())

# print("Los valores ingresados son: ", a, b, c)



# def function_one(param_one, param_two):
#     print("Me gusta la ", param_one, "y el ", param_two, " tambien")
    
    
# function_one("Fresa","Platano")


# def introduction(name, last_name):
#     print("Mi nombre es: ", name, last_name)

# introduction("Tom", last_name="Trejo")



""" Return """
print('-----return without an expression-----')

# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two")
#     print("One")
#     if not wishes:
#         return
    
#     print("Happy New Year!")
    
# happy_new_year()
# print("\n\n")


print("-------return with an expression--------")

# def boring_function():
#     return 123

# x = boring_function()

# print("The boring _function has returned its result. It's:", x)

# print("\n\n")



print("--------list and functions----------")


# def list_sum(lst):
#     s = 0

#     for elem in lst:
#         s += elem

#     return s

# print(list_sum([5, 4, 3]))


print("-------- LAB Año bisiesto ---------")

# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# test_data = [1536, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"-> ",end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")



print("-------- LAB How many days -------\n")


# def is_year_leap(year):           # funcion para el año bisiesto
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year,month):  # funcion para los dias del mes
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res  = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res

# test_years = [1900, 2000, 2016, 1987]
# test_months = [ 2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr,mo,"-> ",end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")
        
        
        
print("------ Day of the year -------")

# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year, month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res  = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res

# def day_of_year(year, month, day):
#     days = 0
#     for m in range(1, month):
#         md = days_in_month(year, m)
#         if md == None:
#             return None
#         days += md
#     md = days_in_month(year, month)
#     if day >= 1 and day <= md:
#         return days + day
#     else:
#         return None

# print(day_of_year(2000, 12, 30))



print("------- Prime numbers ------")

# def is_prime(num):
#     for i in range(2, int(1 + num ** 0.5)):
#         if num % i == 0:
#             return False
#     return True

# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()



print("------ Indice de masa corporal ------")

# funcion que me da el indice de masa corporal

# def imc(weight, height):
#     imc = weight / height ** 2
#     print("El indice de masa corporal es: ", imc )
# print(imc(3, 2))

# funcion que realiza la conversion de libras a kilogramo
# sabemos que que 1 lb =  0.45359237kg

# def ft_and_inch_to_m(ft, inch = 0.0):
#     return ft * 0.3048 + inch * 0.0254


# def lb_to_kg(lb):
#     return lb * 0.4535923


# def bmi(weight, height):
#     if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
#         return None

#     return weight / height ** 2


# print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

print("------ Ejemplos de funciones: Triangulos ------")



# def is_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b

# a = int(input("Dame el valor de a: "))
# b = int(input("Dame el valor de b: "))
# c = int(input("Dame el valor de c:  "))

# print(is_triangle(a,b,c))

# if is_triangle(a, b, c):
#     print("Si, si puede ser un triangulo")
# else:
#     print("No, no puede ser un triangulo")
    
    
    
 
print("------ Triangulos y el Teorema de Pitagoras ------ ") 
     
# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# def is_a_right_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return False
#     if c > a and c > b:
#         return c ** 2 == a ** 2 + b ** 2
#     # if a > b and a > c:
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2
# print(is_a_right_triangle(5, 3, 4))
# print(is_a_right_triangle(1, 3, 4))

print("------ Funciones factoriales ------")


# def factorial(n):
    
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     print(n)
#     return n * factorial(n - 1)
# print(factorial(5))

# def factorial(n):
#     if n == 1:
#         print("n es igual a 1")
#         return print(n * factorial(n - 1))


# print(factorial(4))


print("------- Listas, tuplas y diccionarios -------")

# my_list = [1, 3, 78, 2, "hola", 8.2]
# my_tupla = (3, 8, 2.3, 'text', 1)
# my_dictionary = {"perro":"John", "cat":"minino", "edad": 2, }

# print(type(my_list))
# print(type(my_tupla))
# print(type(my_dictionary))


# my_dictionary["perro"] = "bobby"
# print(my_dictionary)

# for key in sorted(my_dictionary.keys()):
#     print(key)
# for key in my_dictionary.values():
#     print(key)
    
# my_dictionary.update({"hurón":"Ramón"})

# print(my_dictionary) 

# pol_esp_dictionary = {
#     "zamek": "castillo",
#     "woda": "agua",
#     "gleba": "tierra"
#     }

# for key, value in pol_esp_dictionary.items():
#     print("Pol/Esp ->", key, ":", value)


# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)

# print("duplicados", duplicates)    # salida: 4




print("------ Tuplas y diccionarios trabajando juntos ------")

'''
    - necesitas un programa para calcular promedios de tus alumnos
    - el programa pide el nombre del alumno seguido de su calificacion
    - los nombres son ingresados en cualquier orden;
    - el ingresar un nombre vacio fi aliza el ingreso de los datos( Nota 1: ingresar una untiacion vacia generara la excepction ValueError, pero no  te precocupes por eso ahora, de la serios del crso de fundamento  de python)
    - unal lista con todos los nombres y el promedio de calda alumno debe ser mostrada a final
'''


# school_class = {}

# while True:
#     name = input("Ingresa el nombre del estudiante: ")
#     if name == '':
#         break
    
#     score = int(input("Ingresa la calificación del estudiante (0-10): "))
#     if score not in range(0, 11):
# 	    break
    
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)


print("------ Excepciones -------")


# try:
#     value = int(input('Ingresa un número natural: '))
#     print('El recíproco de', value, 'es', 1/value)        
# except:
#     print('No se que hacer con', value)


# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i], )

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     print(k[0])



# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):
#     print(type(my_list[i]))
#     print( my_list[i] )
#     dictionary[my_list[i]] = (my_list[i], )
#     var = dictionary[my_list[i]]
#     var2 = (my_list[i])
#     print(type(var), type(var2))

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     print(k[0])

print("-----pregunta examen-------")
# def func(a, b):
#     return a ** a


# print(func(2,8))

print("-----pregunta examen-------")


# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return


# print(fun(fun(2)) + 1)

# Resultado -  TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

print("------pregunta examen------")

# def fun(x):
#     global y
#     y = x * x
#     return y


# fun(2)
# print(y)

print("------pregunta examen------")


# def any():
#     print(var + 1, end='')


# var = 1
# any()
# print(var)

# Resultado - 21

print("-----pregunta examen-----")

# my_list =  ['Mary', 'had', 'a', 'little', 'lamb']


# def my_listR(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'


# print(my_listR(my_list))

# Resutado - TypeError: 'function' object does not support item deletion

print("-----pregunta examen-----")

# def fun(x, y, z):
#     return x + 2 * y + 3 * z


# print(fun(0, z=1, y=3))

# Resultado - 9

print("-----pregunta examen------")

# def fun(inp=2, out=3):
#     return inp * out


# print(fun(out=2))


# Resultado - 4

print("-----pregunta examen------")

# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']

# for k in range(len(dictionary)):
#     v = dictionary[v]

# print(v)

# Resultado - 2


print("-----pregunta examen------")


# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)

# Resultado - 2

print("-----pregunta examen------")
# try:
#     value = int(input("Ingresa un valor: "))
#     print(value/value)
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada errónea...")
# except TypeError:
#     print("Entrada muy errónea...")
# except:
#     print("¡Buuu!")

# Resultado - Entrada muy errónea...

print("-----pregunta examen------")

# my_list = [1, 2]

# for v in range(2):
#     print(v)
#     print("sin insertar valor ", my_list[v])
#     my_list.insert(-1, my_list[v])
#     print(my_list[v]) 
#     print(my_list)

# print(my_list)

print("------pregunta examen------")

# def function_1(a):
#     return None


# def function_2(a):
#     return function_1(a) * function_1(a)


# print(function_2(2))

print("------pregunta examen------")

# my_list =  [x * x for x in range(5)]


# def fun(lst):
#     print(my_list)

#     del lst[lst[2]]
#     print(my_list)
#     return lst


# print(fun(my_list))


# Resultado - [0, 1, 4, 9]

print("------pregunta examen------")

# x = 1
# y = 2
# x, y, z = x, x, y
# print(x, y, z)
# z, y, z = x, y, z

# print(x, y, z)

# Resultado - 1 1 2

print("------pregunta examen------")

# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b

# print(a, b)

# Resultado 01

print("------pregunta examen------")

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2


# print(fun(fun(2)))

# Resultado 2


print("------pregunta examen------")

# nums = [1, 2, 3]
# vals = nums
# del vals[:]

# Resultado - No entrega nada porque no se imprime nada


print("------pregunta examen------")


# x = int(input())
# y = int(input())
# x = x % y
# print(x)
# x = x % y
# print(x)
# y = y % x
# print(y)

# Resultado - 2


print("------pregunta examen------")

# y = input()
# x = input()
# print(x + y)

# Resultado 63

print("------pregunta examen------")

# print("a", "b", "c", sep="sep")

# Resultado - asepbsepc


print("------pregunta examen------")

# x = 1 // 5 + 1 / 5
# print(1 // 5)
# print(1 / 5)
# print(x)

# Resultado - 0.2

print("------pregunta examen------")

# my_tuple = (1, 2, 3, 4)
# my_tuple[1] = my_tuple[1] + my_tuple[0]

# Resultado - error


print("------pregunta examen------")

# x = float(input())
# y = float(input())
# print(y ** (1 / x))

# Resultado - 2.0

print("------pregunta examen------")

# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']

# for k in range(len(dct)):
#     v = dct[v]

# print(v)

# Resultado - one


print("------pregunta examen------")


# lst = [i  for i in range(-2, -1 )]
# print(lst,"0-0" )

print("------pregunta examen------")
# def fun(a, b, c=0):
    # Cuerpo de la función.

print("------pregunta examen------")

# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)


# print(fun(0, 3))

# Resultado - 0

print("------pregunta examen------")

# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")

# Resultado - ciclo infinito

print("------pregunta examen------")

# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)

# Resultado - 4

print("------pregunta examen------")

# dd = {"1": "0", "0": "1"}
# for x in dd.vals():
#     print(x, end="")



print("------pregunta examen------")

# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)

# for x in dct.keys():
#     print(dct[x][1], end="")
#     print("\n")
# print(dct, "\n")


# Resultado - 21

print("------pregunta examen------")

# def fun(inp=2, out=3):
#     return inp * out


# print(fun(out=2))

# Resultado - 4


print("------pregunta examen------")


# lst = [[x for x in range(3)] for y in range(3)]

# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")
# print(lst)

# Resultado - 
#
#
#
print("------pregunta examen------")

# try:
#     value = input("Ingresa un valor: ")
#     print(int(value)/len(value))
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada erronea...")
# except TypeError:
#     print("Entrada muy erronea...")
# except:
#     print("¡Buuu!")

# Resultado - 0.0


print("------pregunta examen------")

# try:
#     print(5/0)
#     break
# except:
#     print("Lo siento, algo salió mal...")
# except (ValueError, ZeroDivisionError):
#     print("Mala suerte...")

# Resultado - SyntaxError: 'break' outside loop

print("------pregunta examen------")


# foo = (1, 2, 3)
# foo.index(0)

print("------pregunta examen------")

# # A:
# except (TypeError, ValueError, ZeroDivisionError):
#     # Algo de código.

# # B:
# except TypeError, ValueError, ZeroDivisionError:
#     # Algo de código.

# # C:
# except: (TypeError, ValueError, ZeroDivisionError)
#     # Algo de código.

# # D:
# except: TypeError, ValueError, ZeroDivisionError
#     # Algo de código.

# # E:
# except (TypeError, ValueError, ZeroDivisionError)
#     # Algo de código.

# # F:
# except TypeError, ValueError, ZeroDivisionError
#     # Algo de código.



print("------pregunta examen------")

# print(¡Hola, Mundo!)

print(1 // 2)
