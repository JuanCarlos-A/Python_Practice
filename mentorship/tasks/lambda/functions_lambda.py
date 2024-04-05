numeros = [x for x in range(10)] # Lista usando comprehension

new_list = list(map(lambda x : x*2, numeros)) # Funcion usando una funcion lambda, funcion de orden superior

def funcion(n): 
    return lambda a : a * n

otra_funcion = funcion(2)

print(otra_funcion(11))

# x = lambda x : x + 2

# print(x(5))

print((lambda x : x - 1)(2))
