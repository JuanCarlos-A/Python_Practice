import unittest
from unittest.mock import patch
from test.my_weather_api import obtener_clima_actual


class TestObtenerClima(unittest.TestCase):

    @patch('my_weather_module.requests.get')
    def test_obtener_clima_actual(self, mock_get):
        # Configuramos un objeto mock con una respuesta ficticia cuando se llame
        respuesta_ficticia = {
            "location": {
                "name": "London"
            },
            "current": {
                "temp_c": 20,
                "condition": {
                    "text": "Partly cloudy"
                }
            }
        }

    # Configuramos el mock para retornar un objeto con el método 'json' que retorna nuestra respuesta ficticia
        mock_get.return_value.json.return_value = respuesta_ficticia

        # Llamamos a la función que estamos probando
        resultado = obtener_clima_actual('Londres')

        # Confirmamos que 'requests.get' se llamó con la URL esperada
        mock_get.assert_called_once_with('http://api.weatherapi.com/v1/current.json?key=minha_api_key&q=Londres')

        # Afirmamos que el resultado es el esperado (igual a nuestra respuesta ficticia)
        self.assertEqual(resultado['current']['temp_c'], 20)
        self.assertEqual(resultado['current']['condition']['text'], "Partly cloudy")

# Si este archivo se ejecuta como un script, correr las pruebas
if __name__ == '__main__':
    unittest.main()