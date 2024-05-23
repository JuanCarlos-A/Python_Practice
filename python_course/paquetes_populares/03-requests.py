import requests

## GET 


## Impresion de la lista de diccionarios obtenidos en una API

# url = "https://jsonplaceholder.typicode.com/users/"

# response = requests.get(url=url, timeout=10)

# print(
#     response.status_code,
#     response.text
#     )

# response = response.json()

# for user in response:
#     print(user["name"])




## Impresion de solo la imformacion de un diccionario del primer usuario especificado en el endpoint

# url = "https://jsonplaceholder.typicode.com/users/1"

# response = requests.get(url=url, timeout=10).json()


# for key, value in response.items():
#     print(f'Llave : {key}, Value: {value}')



## POST


## Creacion de un nuevo estado de un dato dentro de la api rest enviando un diccionario

# user = {
#     "id" : 11,
#     "name" : "Juan Carlos",
#     "username" : "JuanCar"
# }

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.post(url=url, timeout=10, data=user)

# print(response.status_code) # Obtenemos la respuesta del estado de la peticion




## PUT / PATCH


## Actualizamos un registro dentro de la api enviando los datos y especificando en el endpoint el stado que vamos a actualizar

# user = {
#     "id" : 11,
#     "name" : "Juan Carlos",
#     "username" : "JuanCar"
# }

# url = "https://jsonplaceholder.typicode.com/users/2"

# response = requests.put(url=url, timeout=10, data=user)

# print(response.status_code) # Obtenemos la respuesta del estado de la peticion




## DELETE


# Eliminamos un registro del recurso que conecta con la api rest especificando en el endpoint

# url = "https://jsonplaceholder.typicode.com/users/2"

# response = requests.delete(url=url, timeout=10)

# print(response.status_code) # Obtenemos la respuesta del estado de la peticion




##  CABEZERAS 

## Usamos un diccionario con una llave que es estandar para especificar la api key que vamos a utilizar.

url = "https://jsonplaceholder.typicode.com/users/2"
apikey = "12345156"
headers = {
    "Authorization" : f"Bearer {apikey}"
}

response = requests.delete(url=url, timeout=10, headers=headers)

print(response.status_code) # Obtenemos la respuesta del estado de la peticion
