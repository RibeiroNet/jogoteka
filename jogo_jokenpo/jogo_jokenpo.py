import os 
import random
def jokenpo():
    
    os.system("cls")
    print('olá! seja bem vindo ao jokenpô assasino.')
    print('1 ---------> Pedra;')
    print('2 ---------> Papel;')
    print('3 ---------> Tesoura;')


    while True:
    
        escolha = int(input("escolha pedra, papel ou tesoura:"))
        
        escolhact = random.randint(1,3)

        if escolha == escolhact: 
            print ('empatamos, vamos de novo. JO KEN PO!')

        if escolha == 1 and escolhact == 2:
            print ('joguei papel e venci sua pedra. vamos de novo, JO KEN PO!')
        if escolha == 1 and escolhact == 3:
            print ('escolhi tesoura. você ganhou! vamos de novo, JO KEN PO!')

        if escolha == 2 and escolhact == 1:
            print ('escolhi pedra. você ganhou! vamos de novo, JO KEN PO!')
        if escolha == 2 and escolhact == 3:
            print ('joguei tesoura e venci seu papel. vamos de novo, JO KEN PO!')

        if escolha == 3 and escolhact == 2:
            print ('escolhi papel. você ganhou! vamos de novo, JO KEN PO!')
        if escolha == 3 and escolhact == 1:
            print ('joguei pedra e venci sua tesoura. vamos de novo, JO KEN PO!')