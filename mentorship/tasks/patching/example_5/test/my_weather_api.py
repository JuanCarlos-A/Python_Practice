import requests

def obtener_clima_actual(ciudad):
    url = f'http://api.weatherapi.com/v1/current.json?key=minha_api_key&q={ciudad}'
    response = requests.get(url)
    return response.json()