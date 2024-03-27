from pprint import pprint
class Solutions:
    @staticmethod
    def solution_1(word: str) -> list[str]:
        return list(x for x in word if x != " ")
    
    @staticmethod
    def solution_2(word: str) -> dict[str, int]:
        return dict({x: word.count(x) for x in word})
    
    @staticmethod
    def solution_3(dicc: dict[str, int]) -> list[tuple]:
        return sorted(
            dicc.items(),
            key=lambda x: x[1],
            reverse=True
        )
    
    @staticmethod
    def solution_4(listado: list[tuple]) -> list[tuple]:
        return list(orden for orden in listado if not orden[1] < listado[0][1])
    
    @staticmethod
    def message(lista :list[tuple]) -> str:
        print(f'Los caracteres que mas se repiten con {lista[0][1]} repeticiones son:')
        for items in lista: 
            print(f'- {items[0].upper()}')
        
sin_espacios = Solutions.solution_1("hola mundo este es mi string")
contados = Solutions.solution_2(sin_espacios)
ordenados = Solutions.solution_3(contados)
mayores = Solutions.solution_4(ordenados)
pprint(mayores, width= 10)

Solutions.message(mayores)
