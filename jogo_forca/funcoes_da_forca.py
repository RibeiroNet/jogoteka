import random
#escolhe o tema
def escolhe_tema():
    print("Bem-Vindo ao jogo de Forca.")
    print("Selecione um tema para jogar; Animais, empregos ou Frutas.")
    jogo = input("qual jogo deseja?  ").upper()
    if jogo == "ANIMAIS":
        arquivo = open("jogo_forca/lista_animais.txt","r")
        lista = arquivo.readlines()
        arquivo.close()
        palavra_escolhida = random.choice(lista).strip().upper()
        return palavra_escolhida
    if jogo == "PROFISSÕES":
        arquivo = open("jogo_forca/lista_empregos.txt","r")
        lista = arquivo.readlines()
        arquivo.close()
        palavra_escolhida = random.choice(lista).strip().upper()
        return palavra_escolhida
    if jogo == "FRUTAS":
        arquivo = open("jogo_forca/lista_frutas.txt","r")
        lista = arquivo.readlines()
        arquivo.close()
        palavra_escolhida = random.choice(lista).strip().upper()
        return palavra_escolhida


def cria_mascara(palavra_escolhida: str)->list:
    #lista vazia
    lista_mascara = []
    
    #percorre a lista substituindo underlines por letras e guardando na lista 
    for letra in palavra_escolhida:
        if letra == " ":
         lista_mascara.append(" ")
        else:
         lista_mascara.append("_")
    return lista_mascara

#troca os underlines por letras das palavras 
def  preenche_mascara(palavra_escolhida:str, letra_escolhida: str, mascara:list) -> list:
    contador = 0
    for letra in palavra_escolhida:
        if letra == letra_escolhida:
            mascara[contador] = letra_escolhida
        contador += 1 
    return mascara
