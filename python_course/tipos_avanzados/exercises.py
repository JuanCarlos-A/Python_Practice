class Solutions:
    def solution_1(word: str) -> list[str]:
        return list(x for x in word if x != " ")
    
    def solution_2(word: str) -> dict[str, int]:
        return dict({x: word.count(x) for x in word})
    
    def solution_3(dicc: dict[str, int]) -> list[tuple]:
        return list(tuple(x for x in dicc.items()))
        

    pass

print(Solutions.solution_3({"a" : 1, "b" : 2}))