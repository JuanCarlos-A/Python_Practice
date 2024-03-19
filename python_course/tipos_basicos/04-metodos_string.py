animal = "chanCHito feliz  "

print(animal.upper()) #CHANCHITO FELIZ

print(animal.lower()) #chanchito feliz | se necesita tomar en cuenta que el método lower() convierte toda la cadena en minúsculas.

print(animal.capitalize()) #Chanchito feliz | se necesita tomar en cuenta que el método capitalize() convierte la primera letra de la cadena en mayúscula y el resto en minúsculas.

print(animal.title()) #Chanchito Feliz | se necesita tomar en cuenta que el método title() convierte la primera letra de cada palabra en mayúscula y el resto en minúsculas.

print(animal.strip()) #chanCHito feliz | se necesita tomar en cuenta que el método strip() elimina los espacios en blanco al principio y al final de la cadena.

print(animal.rstrip()) #   chanCHito feliz | se necesita tomar en cuenta que el método rstrip() elimina los espacios en blanco al final de la cadena.

print(animal.lstrip()) #chanCHito feliz  | se necesita tomar en cuenta que el método lstrip() elimina los espacios en blanco al principio de la cadena.

print(animal.find("CH")) #5 | se necesita tomar en cuenta que el método find() busca la subcadena en la cadena y devuelve la posición de la primera ocurrencia de la subcadena.
    #si no lo encuentra devuelve -1 que es un valor especial que se utiliza para indicar que no se encontró la subcadena.

print(animal.replace("feliz", "contento")) #chanCHito contento | se necesita tomar en cuenta que el método replace() busca la subcadena en la cadena y la reemplaza por otra subcadena.

print("chan" in animal) #True | se necesita tomar en cuenta que el operador in verifica si la subcadena se encuentra en la cadena.

print("chu" not in animal) #True | se necesita tomar en cuenta que el operador not in verifica si la subcadena no se encuentra en la cadena.