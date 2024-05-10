from unittest.mock import Mock

# Configuracion desde la instancia

# mock = Mock(return_value=True)

# print(mock())



# mock = Mock(name="Juan Carlos Aguilar")

# mock.name = "Juan Carlos Aguilar"

# print(mock)



# Configuracion usando la configuracion de configure_mock()

# mock = Mock()

# mock.configure_mock(return_value = True)

# print(mock())



holidays = {'12/25': 'Christmas', '7/4': 'Independence Day'}
response_mock = Mock(**{'json.return_value': holidays, "get.return_value" : True})

print(response_mock.json())
print(response_mock.get())





