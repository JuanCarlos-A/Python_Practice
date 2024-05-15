import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"

response = requests.get(url=url).text

print(response)

soup = BeautifulSoup(response, "html.parser")

preguntas = soup.select(".s-post-summary") # Este metodo retorna una lista

print(preguntas[0]["data-post-id"]) # Obtenemos el valor que se almacena dentro del atributo data-post-id

# for pregunta in preguntas:
#     titulo = pregunta.select_one(".s-link").get_text()
#     usuario = pregunta.select_one(".s-user-card--link").get_text()
#     print(f'{usuario.strip()} - Titulo: \n{titulo.strip()}')