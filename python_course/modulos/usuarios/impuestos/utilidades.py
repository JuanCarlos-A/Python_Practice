if __name__ != "__main__":
    # from ..gestion.crud import guardar # Importar modulo de otro paquete de forma relativa
    from usuarios.gestion.crud import guardar # Importar modulo de otro paquete de forma absoluta

    def pagar_impuestos():
        print("Pagar Impuestos")
        guardar()

    print(__name__)

if __name__ == "__main__":
    print("Soy el main de utilidades")
