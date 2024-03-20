"""Comprehensions in Python"""

# List Comprehensions

example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

output_list = [var for var in example_list if var % 2 == 0]

print("Resultados usando las comprehensions en lists:", output_list)


# Set Comprehensions

example_set = {11, 12, 13, 14, 15, 16, 17, 18, 19}

output_set = {x for x in example_set if x % 2 == 0}

print("Resultados utilizando las comprehensions en sets:", output_set)


#Dictionary Comprehensions

example_dict = {'a': 21, 'b': 22, 'c': 23, 'd': 24, 'e': 25}

output_dict = {key : value for key, value in example_dict.items() if value % 2 == 0}

print("Resultados utilizando las comprehensions en diccionarios:", output_dict)



#Generator Comprehensions

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_gen = (var for var in input_list if var % 2 == 0)

print("Output values using generator comprehensions:", end = ' ')

for var in output_gen:
	print(var, end = ' ')

print(type(output_gen))