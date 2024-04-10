from usuarios.impuestos.utilidades import pagar_impuestos
import usuarios

pagar_impuestos()

print(dir(usuarios))

print(usuarios.__file__)
print(usuarios.__package__)
print(usuarios.__path__)
print(usuarios.__name__)

print(usuarios.gestion.crud.guardar.__name__)