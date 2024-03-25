usuarios = [
    ["Juan", 35,],
    ["Ana", 45],
    ["Pedro", 25],
    ["Maria", 30],
    ["Luis", 40]
]

# List Comprehensions

names = [x[0] for x in usuarios]
print(names)

users = [x if x[1] % 2 == 0 else False for x in usuarios]
print(users)


nombres = list(map(lambda x: x[0], usuarios))

usuarios = list(filter(lambda x: x[1] > 2, usuarios))