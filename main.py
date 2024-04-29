#desenvolvido por Neto Ribeiro#
import os 
from jogo_adivinhacao.adivinhacao import *
from jogo_forca.forca import * 
from jogo_da_velha.velha import *
from jogo_calculadora.calculadora import *
from jogo_jokenpo.jogo_jokenpo import *




while True:
   os.system("cls")
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
      print('''escolha um jogo para se divertir.  
      1.Forca e Enforca 
      2.Jogo de Adivinhação makumbado
      3.Calculadora Mortal
      4.Jogo da Velha Maldito
      5.Jokenpo assasino
      0.sair
            
   ''')
   if idade < 18:
      print("você não pode acessar a jogoteka. não volte nunca mais!")
      exit()

   jogo_escolhido = int(input("Em qual jogo você gostaria de se aventurar?  "))

   if jogo_escolhido == 2:
      adivinhacao()
   if jogo_escolhido == 1:
      forca()
   if jogo_escolhido == 4:
      velhinha()
   if jogo_escolhido == 3:
      calcular()
   if jogo_escolhido == 5:
      jokenpo()
   if jogo_escolhido == 0:
      print('tudo bem, viajante. te vejo numa próxima noite sangrenta...')
      break