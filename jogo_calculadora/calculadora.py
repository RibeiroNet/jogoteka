import random
def calcular():
    while True:
        numero1 = random.randrange(100)
        numero2 = random.randrange(100)
        operacao = random.randrange(5)
        

        if operacao == 1:
            resul = numero1 + numero2
            rep = int(input(f"qual a resposta de {numero1} + {numero2}?: "))
            if rep == resul:
                print("PARABENS VOCE ACERTOU")
                break
            if rep != resul:
                print("NAOOO VOCE ERROU, tente de novo")
        
        
        if operacao == 2:
            resul = numero1 - numero2
            rep = int(input(f"qual a resposta de {numero1} - {numero2}?: "))
            if rep == resul:
                print("PARABENS VOCE ACERTOU")
                break
            if rep != resul:
                print("NAOOO VOCE ERROU, tente de novo")
        
        
        if operacao == 3:
            resul = numero1 * numero2
            rep = int(input(f"qual a resposta de {numero1} X {numero2}?: "))
            if rep == resul:
                print("PARABENS VOCE ACERTOU")
                break
            if rep != resul:
                print("NAOOO VOCE ERROU, tente de novo")
        
        
        if operacao == 4:
            resul = numero1 / numero2
            rep = float(input(f"qual a resposta de {numero1} / {numero2}?: "))
            if rep == resul:
                print("PARABENS VOCE ACERTOU")
                break
            if rep != resul:
                print("NAOOO VOCE ERROU, tente de novo")