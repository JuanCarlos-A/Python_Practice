"""Example 2: Mixin para convertir a JSON y XML un objeto Python."""
class JsonMixin:
    """Clase Mixin para convertir a JSON un objeto Python."""
    import json

    def to_json(self):
        """ Método que convierte a JSON un objeto Python."""
        return self.json.dumps(self.__dict__)

class XmlMixin:
    """Clase Mixin para convertir a XML un objeto Python."""
    def to_xml(self):
        """ Método que convierte a XML un objeto Python."""
        # Implementación simplificada para el ejemplo
        attributes = "".join([f'<{k}>{v}</{k}>' for k, v in self.__dict__.items()])
        return f'<{self.__class__.__name__}>{attributes}</{self.__class__.__name__}>'

class Persona(JsonMixin, XmlMixin):
    """Clase que representa una persona."""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Ejemplo de uso
persona = Persona("Alice", 30)
print(persona.to_json())  # Utilizando el mixin JsonMixin
print(persona.to_xml())   # Utilizando el mixin XmlMixin
