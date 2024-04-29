import random
def calcular():
    while True:
        numero1 = random.randrange(100)
        numero2 = random.randrange(100)
        operacao = random.randrange(5)
        

        if operacao == 1:
            resul = numero1 + numero2
            resp = int(input(f"qual a resposta de {numero1} + {numero2}?: "))
            if resp == resul:
                print("está correto. parabéns. ")
                break
            if resp != resul:
                print("Você errou. tente novamente.")
        
        
        if operacao == 2:
            resul = numero1 - numero2
            resp = int(input(f"qual a resposta de {numero1} - {numero2}?: "))
            if resp == resul:
                print("está correto. parabéns.")
                break
            if resp != resul:
                print("Você errou. tente novamente.")
        
        
        if operacao == 3:
            resul = numero1 * numero2
            resp = int(input(f"qual a resposta de {numero1} X {numero2}?: "))
            if resp == resul:
                print("está correto. parabéns.")
                break
            if resp != resul:
                print("Você errou. tente novamente.")
        
        
        if operacao == 4:
            resul = numero1 / numero2
            resp = float(input(f"qual a resposta de {numero1} / {numero2}?: "))
            if resp == resul:
                print("está correto. parabéns.")
                break
            if resp != resul:
                print("Você errou. tente novamente.")