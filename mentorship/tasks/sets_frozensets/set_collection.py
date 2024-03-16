"""Practice of Sets Collections in Python"""

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 

# Add an element to the set
my_set.add(10) 

print(my_set)

# Remove an element from the set
my_set.remove(10) #error if element does not exist

print(my_set)

# Discard an element from the set
my_set.discard(10) #No Error if element does not exist

print(my_set)

# Pop an element from the set
my_set.pop() #random element removed

print(my_set)

# Union of two sets
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

set3 = set1.union(set2)


# Intersection of two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = set1.intersection(set2)

print(set3)

# Difference of two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = set1.difference(set2)

print(set3)

# Symmetric difference of two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = set1.symmetric_difference(set2)

print(set3)


# Clear the set
my_set.clear()


