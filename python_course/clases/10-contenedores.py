class Producto:
    def __init__(self, nombre :str, precio :float) -> None:
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self) -> None:
        return f'Producto: {self.nombre}\n-Precio: {self.precio}'

class Categoria:
    producto = []
    def __init__(self, nombre :str, productos :list[object]) -> None:
        self.nombre = nombre
        self.productos = productos

    def agragar(self, producto :object) -> None:
        self.productos.append(producto)

    def imprimir(self) -> None:
        for producto in self.productos:
            print(producto)

kayac = Producto("Kayac", 1000)

bicicleta = Producto("Bicicleta", 750)

surfboard = Producto("Surfboard", 500)

deportes = Categoria("Deportes", [kayac, bicicleta])

deportes.agragar(surfboard)

deportes.imprimir()
