"""Practices with dictionaries in Python"""

dic = { "Uno" : 1, "Dos" : 2, "Tres" : 3, "Cuatro" : 4, "Cinco" : 5}

print(dic)

print(dic["Uno"]) #Devuelve el valor de la clave

dic["Seis"] = 6

dic["Uno"] = 10 #Modifica el valor de la clave


del dic["Dos"] #Elimina la clave y su valor

print(dic)

print(dic.keys())  #Devuelve una lista de claves

print(dic.values()) #Devuelve una lista de valores

print(dic.items()) #Devuelve una lista de tuplas

for clave, values in dic.items():
    print(f'La clave es {clave} y su valor es {values}') 

print("Uno" in dic) #True

print("Diez" in dic) #False
