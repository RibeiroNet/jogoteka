import os 
def velhinha():

    lista_de_posicoes =[ 0,1,2,3,4,5,6,7,8,9 ]
    jogador = "X"
    contagem = 0 

    while True:
        print(f"        {lista_de_posicoes[1]}  |  {lista_de_posicoes[2]}  |  {lista_de_posicoes[3]}")
        print('      -----|-----|-----')
        print(f"        {lista_de_posicoes[4]}  |  {lista_de_posicoes[5]}  |  {lista_de_posicoes[6]}")
        print('      -----|-----|-----')
        print(f"        {lista_de_posicoes[7]}  |  {lista_de_posicoes[8]}  |  {lista_de_posicoes[9]}")
    


        jogada = int(input(f'Jogador X, escolha sua posição; '))
        lista_de_posicoes[jogada] = ("X")
        os.system("cls")
        contagem += 1 
        if contagem == 9:
            print('empate.')
            break





        if lista_de_posicoes[1] == ("X") and lista_de_posicoes[2] == ("X") and lista_de_posicoes[3] == ("X"):
            print("jogador X ganhou.")
            break
        if lista_de_posicoes[4] == ("X") and lista_de_posicoes[5] == ("X") and lista_de_posicoes[6] == ("X"):
            print("jogador X ganhou.")
            break
        if lista_de_posicoes[7] == ("X") and lista_de_posicoes[8] == ("X") and lista_de_posicoes[9] == ("X"):
            print("jogador X ganhou.")
            break
        if lista_de_posicoes[1] == ("X") and lista_de_posicoes[5] == ("X") and lista_de_posicoes[9] == ("X"):
            print("jogador X ganhou.")
            break
        if lista_de_posicoes[3] == ("X") and lista_de_posicoes[5] == ("X") and lista_de_posicoes[7] == ("X"):
            print("jogador X ganhou.")
            break
        if lista_de_posicoes[1] == ("X") and lista_de_posicoes[4] == ("X") and lista_de_posicoes[7] == ("X"):
            print("jogador X ganhou.")
            break
        if lista_de_posicoes[2] == ("X") and lista_de_posicoes[5] == ("X") and lista_de_posicoes[8] == ("X"):
            print("jogador X ganhou.")
            break
        if lista_de_posicoes[3] == ("X") and lista_de_posicoes[6] == ("X") and lista_de_posicoes[9] == ("X"):
            print("jogador X ganhou.")
            break




        print(f"        {lista_de_posicoes[1]}  |  {lista_de_posicoes[2]}  |  {lista_de_posicoes[3]}")
        print('      -----|-----|-----')
        print(f"        {lista_de_posicoes[4]}  |  {lista_de_posicoes[5]}  |  {lista_de_posicoes[6]}")
        print('      -----|-----|-----')
        print(f"        {lista_de_posicoes[7]}  |  {lista_de_posicoes[8]}  |  {lista_de_posicoes[9]}")





        jogada = int(input(f'Jogador O, escolha sua posição; '))
        lista_de_posicoes[jogada] = ("O")
        os.system("cls")
        contagem += 1 
        if contagem == 9:
            print('empate.')
            break





        if lista_de_posicoes[1] == ("O") and lista_de_posicoes[2] == ("O") and lista_de_posicoes[3] == ("O"):
            print("jogador O ganhou.")
            break
        if lista_de_posicoes[4] == ("O") and lista_de_posicoes[5] == ("O") and lista_de_posicoes[6] == ("O"):
            print("jogador O ganhou.")
            break
        if lista_de_posicoes[7] == ("O") and lista_de_posicoes[8] == ("O") and lista_de_posicoes[9] == ("O"):
            print("jogador O ganhou.")
            break
        if lista_de_posicoes[1] == ("O") and lista_de_posicoes[5] == ("O") and lista_de_posicoes[9] == ("O"):
            print("jogador O ganhou.")
            break
        if lista_de_posicoes[3] == ("O") and lista_de_posicoes[5] == ("O") and lista_de_posicoes[7] == ("O"):
            print("jogador O ganhou.")
            break
        if lista_de_posicoes[1] == ("O") and lista_de_posicoes[4] == ("O") and lista_de_posicoes[7] == ("O"):
            print("jogador O ganhou.")
            break
        if lista_de_posicoes[2] == ("O") and lista_de_posicoes[5] == ("O") and lista_de_posicoes[8] == ("O"):
            print("jogador O ganhou.")
            break
        if lista_de_posicoes[3] == ("O") and lista_de_posicoes[6] == ("O") and lista_de_posicoes[9] == ("O"):
            print("jogador O ganhou.")
            break