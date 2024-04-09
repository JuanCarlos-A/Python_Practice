class JsonMixin:
    import json

    def to_json(self):
        return self.json.dumps(self.__dict__)

class XmlMixin:
    def to_xml(self):
        # Implementación simplificada para el ejemplo
        attributes = "".join([f'<{k}>{v}</{k}>' for k, v in self.__dict__.items()])
        return f'<{self.__class__.__name__}>{attributes}</{self.__class__.__name__}>'

class Persona(JsonMixin, XmlMixin):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Ejemplo de uso
persona = Persona("Alice", 30)
print(persona.to_json())  # Utilizando el mixin JsonMixin
print(persona.to_xml())   # Utilizando el mixin XmlMixin