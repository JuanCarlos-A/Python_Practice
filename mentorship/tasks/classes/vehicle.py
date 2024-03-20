class Vehiculo():
    def __init__(self, marca, modelo, color, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.arrancado = False

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nPrecio: {self.precio}\nArrancado: {self.arrancado}"
    
    def arrancar(self):
        self.arrancado = True
        return "El vehículo ha arrancado"
    
    def apagar(self):
        self.arrancado = False
        return "El vehículo ha apagado"
    
carro = Vehiculo("Toyota", "Corolla", "Blanco", 20000)
print(carro)
print(carro.arrancar())
print(carro.apagar())
print(carro)

moto = Vehiculo("Honda", "CBR", "Rojo", 10000)
print(moto)
print(moto.arrancar())
print(moto.apagar())
print(moto)