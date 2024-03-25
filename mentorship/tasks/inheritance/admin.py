from user import User

class Admin(User):
    def __init__(self, id: int, name: str, active: bool, position: str) -> None:
        super().__init__(id, name, active) #Super nos permite acceder a los metodos de la clase padre
        self.position = position

    def __str__(self) -> str:
        return f'{super().__str__()}\nPosicion: {self.position}'
    

admin = Admin(2, 'Pedro', True, 'Admin')

print(admin.get_name())

admin.set_name('Pedro Perez')

print(admin.get_name())