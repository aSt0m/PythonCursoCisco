""" Funciones """

def message():
    print("Ingresa un valor")
    
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

print("Los valores ingresados son: ", a, b, c)



def function_one(param_one, param_two):
    print("Me gusta la ", param_one, "y el ", param_two, " tambien")
    
    
function_one("Fresa","Platano")


def introduction(name, last_name):
    print("Mi nombre es: ", name, last_name)

introduction("Tom", last_name="Trejo")