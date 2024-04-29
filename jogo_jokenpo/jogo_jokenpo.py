import os 
import random
os.system("cls")
print('olá! seja bem vindo ao jokenpô.')
print('1 ---------> Pedra;')
print('2 ---------> Papel;')
print('3 ---------> Tesoura;')


while True:
   
    escolha = int(input("escolha pedra, papel ou tesoura:"))
    escolhact = random.randint(1,3)

    if escolha == escolhact: 
        print ('empatamos, vamos de novo. JO KEN PO!')

    if escolha == 1 and escolhact == 2:
        print ('papel venceu a pedra, vamos de novo. JO KEN PO!')
    if escolha == 1 and escolhact == 3:
        print ('pedra venceu tesoura, vamos de novo. JO KEN PO!')

    if escolha == 2 and escolhact == 1:
        print ('papel venceu a pedra, vamos de novo. JO KEN PO!')
    if escolha == 2 and escolhact == 3:
        print ('tesoura venceu papel, vamos de novo. JO KEN PO!')

    if escolha == 2 and escolhact == 1:
        print ('pedra venceu a tesoura, vamos de novo. JO KEN PO!')
    if escolha == 2 and escolhact == 2:
        print ('tesoura venceu papel, vamos de novo. JO KEN PO!')