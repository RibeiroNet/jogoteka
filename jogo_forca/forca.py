from .funcoes_da_forca import *

def forca():
    palavra_secreta = escolhe_tema()

    mascara = cria_mascara(palavra_secreta)
    print(*mascara)

    chances = 5 
    while "_" in mascara:   
        letra_escolhida = input ("escolha uma letra:  ").upper()

        mascara = preenche_mascara(palavra_secreta,letra_escolhida,mascara)

        if letra_escolhida == palavra_secreta:
            print("você ganhou!")
            print(f"a palavra era {palavra_secreta}.")
            break 
        if letra_escolhida not in mascara:
            chances -= 1 

        if chances == 0:
            print("você perdeu!")
            print(f"a palavra era {palavra_secreta}")
            break 

        if len(letra_escolhida) > 2 and "_" in mascara:
            print("você chutou e errou!")
            print(f"a palavra era {palavra_secreta}")
            break
        
        print(f"suas chances:{chances}")
        print(*mascara)
   