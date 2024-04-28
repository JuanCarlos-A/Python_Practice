#Funciones de primera clase

# Ejemplo 1

# def funcion(txt :str) -> None: #Objetos de primera clase o Funciones de primera clase
#     print(txt.upper())


# variable = funcion

# variable("hola")

#Ejemplo 2

# def funcion_2(txt: str, funcion) -> None: # Funcion de Orden Suepior
#     funcion(txt)


# funcion_2("hola", variable)

# Ejemplo 3
# def create_adder(x): 
#     def adder(y): 
#         return x-y 
 
#     return adder
 
 
# add_15 = create_adder(15) 
 
# print(add_15(10)) 



#Decoradores

# Ejemplo 1

# @decorator_example  # Sintaxis de un decorador
# def hola_decorator():
#     print("Gfg")


# def decorator(func):
#     def interna():
#         print("Decorador")
#         func()
#     return interna

# @decorator
# def hola_decorator():
#     print("Gfg")

# hola_decorator()

# Ejemplo 2

# def decorator(func : None): 
#     print("Esto es al momento de usar el decorador")
#     def interna():
#         print("Esto es al momento antes de usar la funcion")
#         func()
#         print("Esto es al momento despues de usar la funcion")

#     return interna

# @decorator
# def hello():
#     print("Hola")

# hello()

# objeto = decorator(hello)

# print(objeto())


# Ejemplo 3
# import time

# def calculate_time(func):
	
# 	def inner1(*args, **kwargs):

# 		begin = time.time()
		
# 		func(*args, **kwargs)

# 		end = time.time()
# 		print("Total time taken in : ", func.__name__, end - begin)

# 	return inner1



# @calculate_time
# def factorial(num):

# 	time.sleep(2)
# 	print(pow(num, 2))

# factorial(10)

# Ejemplo 4

# def decorator(func):
#     print("Dentro del decorador")
#     def inner(*args, **kwargs):
#         print("Antes de la ejecucion")

#         returned_value = func(*args, **kwargs)

#         print("Despues de la ejecucion")

#         return returned_value

#     return inner

# @decorator
# def funcion(num):
#     print("Dentro de la ejecucion")
#     return num ** 2


# print(funcion(10))


# Ejemplo 5

# def decor1(func): 
# 	def inner(): 
# 		x = func() 
# 		return x * x 
# 	return inner 

# def decor(func): 
# 	def inner(): 
# 		x = func() 
# 		return 2 * x 
# 	return inner 

# @decor1
# @decor
# def num(): 
# 	return 10

# @decor
# @decor1
# def num2():
# 	return 10

# print(num()) 
# print(num2())


#Ejemplo 6
# DUNDER ATTRIBUTES
# from functools import wraps

# def decorator(func):
#     @wraps(func)
#     def inner(*args, **kwargs):

#         variable =  func(*args, **kwargs)

#         return variable
#     return inner
    

# @decorator
# def funcion(*args, **kwargs):
#     """ Funcion con un decoradors"""
#     print(f'Args = {args} \n Kwargs : {kwargs}')



# print(funcion.__name__)
# print(funcion.__doc__)


#Ejemplo 7

# import decoradores 

# @decoradores.decorator_func
# def example_function(cantidad):
#     for _ in range(cantidad):
#         sum([number**2 for number in range(10000)])

#     return



# print(example_function(100))

# Ejemplo 8

# class ExampleDecorator:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         print(f'Llamando {self.func.__name__}')
#         return self.func(*args, **kwargs)


## Example 9

import functools

def repetir(funcion = None, *, veces = 2):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(veces):
                func(*args, **kwargs)

        return wrapper

    if funcion is None:
        return decorador
    else:
        return decorador(funcion)
    

@repetir(veces=3)

def hola():
    print("Hola")

hola()
