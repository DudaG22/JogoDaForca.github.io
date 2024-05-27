import random
from os import system, name

def limpa_tela():

    if name == 'nt':
        _ = system ('cls')
    else:
        _ = system ('clear')

def game():

    limpa_tela()

    print("\nJogo Da Forca")
    print("\nAdivinhe a palavra abaixo:\n")

    palavras = ['abacaxi', 'abacate', 'banana', 'coco', 'caju', 'damasco', 'figo', 'goiaba', 'jabuticaba', 'laranja', 'morango', 'mamao', 'pera', 'tangerina', 'uva']
    palavra = random.choice(palavras)

    espacos = ['_' for letra in palavra]
    chances = 6
    erros = []

    while chances > 0:
        print(" ".join(espacos))
        print("\nChances restantes: ", chances)
        print("Erros:", " ".join(erros))

        tentativa = input("\n\n\n\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    espacos[index] = letra
                index += 1
            
        else:
            chances -= 1
            erros.append(tentativa)

        if "_" not in espacos:
            print("\nVoce venceu! A palavra era: ", palavra)
            break

    if "_" in espacos:
        print("\nVoce perdeu! A palavra era: ", palavra)
    
if __name__ == "__main__":
    game()
    print("\nFim")




