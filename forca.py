import random


def jogar():

    imprime_msg_inicial()
    palavra_secreta = selecione_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    print(palavra_secreta)

    while (not enforcou and not acertou):

        chute = chute_usuario()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_msg_ganhador()
    else:
        imprime_msg_perdedor()

    print('Fim do jogo')

def imprime_msg_inicial():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def selecione_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def chute_usuario():
    chute = input('Digite uma letra ')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_msg_ganhador():
    print('Parabéns você ganhou!!!')

def imprime_msg_perdedor():
    print('Não foi desta vez, você perdeu!!!')

if (__name__ == "__main__"):
    jogar()
