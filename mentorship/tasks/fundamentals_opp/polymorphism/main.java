// Clase Padre
class Animal{ 
    public Animal() {} 
}
// CLases hijas
class Perro extends Animal {
    public Perro() {}
}

class Gato extends Animal {
    public Gato() {}
}

Animal a = new Perro();

Animal[] animales = new Animal[10];
animales[0] = new Perro();
animales[1] = new Gato();

class OtraClase { 
    public OtraClase() {} 
}
Animal a = new OtraClase();
animales[0] = new OtraClase();