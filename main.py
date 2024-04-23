import os 
os.system("cls")
#desenvolvido por Neto Ribeiro#

print('''
******************** SEJA BEM VINDO A ****************************** 
      
     ██╗ ██████╗  ██████╗  ██████╗ ████████╗███████╗██╗  ██╗ █████╗ 
     ██║██╔═══██╗██╔════╝ ██╔═══██╗╚══██╔══╝██╔════╝██║ ██╔╝██╔══██╗
     ██║██║   ██║██║  ███╗██║   ██║   ██║   █████╗  █████╔╝ ███████║
██   ██║██║   ██║██║   ██║██║   ██║   ██║   ██╔══╝  ██╔═██╗ ██╔══██║
╚█████╔╝╚██████╔╝╚██████╔╝╚██████╔╝   ██║   ███████╗██║  ██╗██║  ██║
 ╚════╝  ╚═════╝  ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
''')
idade = int(input("qual sua idade?  "))
if idade >= 18:
   input('''escolha um jogo para se divertir:  
    1.Forca e Enforca 
    2.Jogo de Adivinhação makumbado
    3.Calculadora Mortal
    4.Jogo da Velha Maldito
         
''')
if idade < 18:
    print("você não pode acessar a jogoteka. não volte mais!")
    exit()
    

