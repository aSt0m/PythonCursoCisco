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

my_list = [1, 3, 78, 2, "hola", 8.2]
my_tupla = (3, 8, 2.3, 'text', 1)
my_dictionary = {"perro":"John", "cat":"minino", "edad": 2, }

print(type(my_list))
print(type(my_tupla))
print(type(my_dictionary))


my_dictionary["perro"] = "bobby"
print(my_dictionary)

for key in sorted(my_dictionary.keys()):
    print(key)
for key in my_dictionary.values():
    print(key)
    
my_dictionary.update({"hurón":"Ramón"})

print(my_dictionary) 

