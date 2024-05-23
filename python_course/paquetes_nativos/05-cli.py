import sys
from pathlib import Path
import os

# print(sys.argv)

def cli(args):
    if len(args) == 1:
        print("No se pasaron Argumentos")
        return
    if len(args) != 3:
        print("Se necesitan 2 Argumentos")
        return
    
    origen = Path(args[1])

    if not origen.exists():
        print("Origen no existe.")
        return
    
    destino = Path(args[2])

    if destino.exists():
        print("El destino no puede existir.")
        return
    
    destiny = Path(args[2])

    os.rename(args[1], destiny)

    print("Archivo renombrado con exito")
    
    
    
cli(sys.argv)
