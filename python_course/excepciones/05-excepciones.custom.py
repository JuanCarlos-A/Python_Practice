class MiError(Exception):
    """ Clase para maneja un error de Division por 0"""
    def __init__(self, msg  :str, codigo :float) -> None:
        self.msg = msg
        self.codigo = codigo

    def __str__(self) -> str:
        return f'El error es: "{self.msg}".\nEl codigo de error es {self.codigo}.'
    

def dividir(n=0):
    if n == 0:
        raise MiError("No se puede dividir entre cero", 405)
    return 5 / n

try:
    dividir()
except MiError as e:
    print(e)