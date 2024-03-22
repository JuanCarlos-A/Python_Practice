class Solucion():
    def __init__(self, texto):
        self.texto = texto

    def no_space(self) -> str:
        # nuevo_text = ""

        # for char in self.texto:
        #     if char != " " : 
        #         nuevo_text += char
                
        return self.texto.replace(" ", "")
    
    def palindrome(self) -> bool:
        return Solucion.no_space(self).lower() == Solucion.no_space(self)[::-1].lower()
    

solu = Solucion("Ama")

print(solu.palindrome())



def no_space(texto :str) -> str:
    return texto.replace(" ", "")

def palindrome(texto :str) -> bool:
    return no_space(texto).lower() == no_space(texto)[::-1].lower()


print(palindrome("osso"))