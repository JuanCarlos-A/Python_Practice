"""Practice of Sets Collections in Python"""

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 

my_set.add(10)  # Agregar un elemento al set

print(my_set)

# Remover un elemento del set
my_set.remove(10) #error if element does not exist

print(my_set)

# Descartar un elemento del set
my_set.discard(10) #No Error if element does not exist

print(my_set)

# Pop an element from the set
my_set.pop() #random element removed

print(my_set)

# Union of two sets
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

set3 = set1.union(set2) 

print(set3)


# Intersection of two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = set1.intersection(set2)

print(set2.isdisjoint(set1)) #False

print(set3, "+")

# Difference of two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = set1.difference(set2)


print(set3)


# Clear the set
my_set.clear()


set4 = {c for c in 'abracadabra' if c not in 'abc'} # comprehension
print(set4) # {'r', 'd'}


#Tarea: Crear un set vacio

set5 = set()
print(type(set5))


set6 = frozenset()
print(type(set6))


print(10 in set1)


