class Vehiculo():
    def __init__(self, marca, modelo, color, precio, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.arrancado = False
        self.tipo_motor = tipo_motor

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nPrecio: {self.precio}\nArrancado: {self.arrancado}"
    
    def arrancar(self):
        self.arrancado = True
        return "El vehículo ha arrancado"
    
    def apagar(self):
        self.arrancado = False
        return "El vehículo ha apagado"
    
    def tipo(self):
        return f"Tipo de energía: {self.tipo_motor}"
    
    def pico_placa(self):
        return "Si tiene pico y placa, no puede circular hoy" if self.tipo_motor.lower().strip() == "gasolina" else "No tiene pico y placa, puede circular hoy"
    
    
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


#Tarea:

#Averiguar _atributo __metodo, static method, getters y setters inheritances, circular importation