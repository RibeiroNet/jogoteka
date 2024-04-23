import random 
def adivinhacao():
   
    print('''
    ___    ____  _____    _______   ____  ________   ____  __  __   __  _______  ____  ____  ___    __
   /   |  / __ \/  _/ |  / /  _/ | / / / / / ____/  / __ \/ / / /  /  |/  / __ \/ __ \/ __ \/   |  / /
  / /| | / / / // / | | / // //  |/ / /_/ / __/    / / / / / / /  / /|_/ / / / / /_/ / /_/ / /| | / / 
 / ___ |/ /_/ // /  | |/ // // /|  / __  / /___   / /_/ / /_/ /  / /  / / /_/ / _, _/ _, _/ ___ |/_/  
/_/  |_/_____/___/  |___/___/_/ |_/_/ /_/_____/   \____/\____/  /_/  /_/\____/_/ |_/_/ |_/_/  |_(_)   


    | 1 - Fácil (1-10)  |
    | 2 - Médio (1-20)  |
    | 3 - Dificil (1-50)|
    | 4 - SENAI (1-100) |
    ---------------------                                                                                              
    ''')
   

    nível = int(input("Escolha um nível de difilcudade: "))

    chances = 0
    aleatorio = random.randint (1,10)
    aleatorio2 = random.randint (1,20)
    aleatorio3 = random.randint (1,50)
    aleatorio4 = random.randint (1,100)

    while True:

        if nível == 1:
            numero = int(input("Escolha um número de 1 a 10: "))
            chances = 10
            chances -= 1 
            if numero > aleatorio: 
                print("Você errou, o número é menor.")
                print(f"restam {chances} chances.")
            if numero < aleatorio:
                print("Você errou, o número é maior.")  
                print(f"restam {chances} chances.")
            if numero > 10 or numero < 1:
                print("Você perdeu duas chances por escolher um número fora do jogo!")
                print(f"restam {chances} chances.")
                chances -= 2 
            if chances == 0:
                print("VOCÊ PERDEU!")

        if nível == 2:
            chances = 10
            numero = int(input("Escolha um número de 1 a 20: "))
            chances -= 1 
            if numero > aleatorio2: 
                print("Você errou, o número é menor.")
                print(f"restam {chances} chances.")
            if numero < aleatorio2:
                print("Você errou, o número é maior.")
                print(f"restam {chances} chances.")  
            if numero > 20 or numero < 1:
                print("Você perdeu duas chances por digitar um número fora do jogo!")
                print(f"restam {chances} chances.")
                chances -= 2 
            if chances == 0:
                print("VOCÊ PERDEU!")

        if nível == 3:
            chances = 5
            numero = int(input("Escolha um número de 1 a 50: "))
            chances -= 1 
            if numero > aleatorio3: 
                print("Você errou, o número é menor.")
                print(f"restam {chances} chances.")
            if numero < aleatorio3:
                print("Você errou, o número é maior.") 
                print(f"restam {chances} chances.") 
            if numero > 50 or numero < 1:
                print("Você perdeu duas vida por digitar um número fora do jogo!")
                print(f"restam {chances} chances.")
                vezes -= 2


        if nível == 4:
            numero = int(input("escolha um número de 1 a 100: "))
            vezes = vezes + 1  
            if numero > aleatorio4: 
                print("Você errou, o número é menor. ")
            if numero < aleatorio4:
                print("Você errou, o número é maior.")  
            if numero > 100 or numero < 1:
                print("Você perdeu duas vida por digitar um número fora do jogo!")
                vezes = vezes + 1

        if vezes > 5:
            print('''
   ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████       ▄██████▄   ▄█    █▄     ▄████████    ▄████████ 
  ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███ 
  ███    █▀    ███    ███ ███   ███   ███   ███    █▀       ███    ███ ███    ███   ███    █▀    ███    ███ 
 ▄███          ███    ███ ███   ███   ███  ▄███▄▄▄          ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███ ████▄  ▀███████████ ███   ███   ███ ▀▀███▀▀▀          ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    ███   ███    ███ ███   ███   ███   ███    █▄       ███    ███ ███    ███   ███    █▄  ▀███████████ 
  ███    ███   ███    ███ ███   ███   ███   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███ 
  ████████▀    ███    █▀   ▀█   ███   █▀    ██████████       ▀██████▀   ▀██████▀    ██████████   ███    ███ 
                                                                                                 ███    ███ 
''')
            break
        if numero == aleatorio and vezes <= 5:
            print("Você acertou, parabéns!")
            break

