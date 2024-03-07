def hola(nom:str) -> str:
    if type(nom) is not str:
        return 'Me enviaste un tipo errono'
    return f'Hola Programador {nom}'

variable = hola((2,5,3))
print(variable)

# if 'Hola' == 'Chao':
#     print('1')

# n1 = None
# n2 = None

# if n1 is n2:
#     print('2')

# a = True
# b = True

# if a is b:
#     print('3')

# a = 2
# b = 2

# if a is b:
#     print('4')


c = -60000
d = -60000
print(id(c), id(d))

if c is d:
    print('5')
