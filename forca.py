import random
import string
def jogar():
    global palavras
    print('#' * 65)
    print('Bem vindo(a) ao jogo de forca')
    print('                        Boa sorte!!!')
    print('#' * 65)

    # criar e ler arquivo
    arquivo = open('palavras.txt','r')
    palavras = []  # criei uma lista vazia para receber as palavras
    #Laço para ler cada linha do arquivo
    for linha in arquivo:
        linha = linha.strip() # leitura linha a linha tirando espaços
        palavras.append(linha)
    arquivo.close()

    #Gera a lista aleatóriamente, o len é útil p/ saber o tamanho da lista
    numero: int = random.randrange(0,len(palavras))
    palavra_secreta: str = palavras[numero].lower()
    #para apresentar os espaçamentos de forma dinâmica
    letras_acertadas: list = [' _ '] * len(palavra_secreta)
    # também tem uma outra opção que é:
    #letras_acertadas= [' _ ' for letra in palavra_secreta]
    print(palavra_secreta)

    enforcou  = False
    acertou: bool = False
    # analisa se as tentativas são do mesmo tamanho da palavra secteta
    tentativas: int = len(palavra_secreta) -1

    # para iniciar o jogo mostrando a a forca
    print(letras_acertadas)

    while not enforcou and not acertou:
        # lower retorna a string com todas as letras minusculas
        chute = input('Digite uma letra: ').lower()
        chute = chute.strip() # strip remover espaços em branco#

        # verificar se letra  existe na palavra sescreta
        if chute in palavra_secreta:
            posicao: int = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            tentativas -= 1
        # enquanto _ ñ existir dentro das letras acertadas ai pode encerrar
        acertou = ' _ ' not in letras_acertadas
        # usa o número de letras da palavra secreta como limite de tentativas
        enforcou = tentativas == 0
        print(letras_acertadas)

    if acertou:
        print(f'Parabéns, você acertou a palavra secreta é: {palavra_secreta}')
    else:
        print(f'Não foi dessa vez, você perdeu.'
              f' A palavra secreta era:'f'{palavra_secreta}')

    print("## Fim do jogo ##")

    # função necessária para rodar a classe atual, sem isso eu não consigo
    # executar o código diretamente, apenas pela classe jogo
if (__name__ == '__main__'):
    jogar()
