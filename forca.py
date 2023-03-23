def jogar():
    print('#' * 65)
    print('Bem vindo(a) ao jogo de forca')
    print('                        Boa sorte!!!')
    print('#' * 65)

    palavra_secreta = 'BANANA'
    letras_acertadas = [' _ '* 6]

    enforcou = False
    acertou = False

    # para iniciar o jogo mostrando a a forca
    print(letras_acertadas)
    while (not enforcou and not acertou):
        #lower retorna a string com todas as letras minusculas
        chute = input('Digite uma letra: ').lower()
        chute = chute.strip() #remover espaços em branco#

        posicao = 0
        for letra in palavra_secreta:
            if (chute.lower() == letra.lower()):
                letras_acertadas[posicao] = letra
            posicao = posicao +1

        print(letras_acertadas)

    print("## Fim do jogo ##")


    # função necessária para rodar a classe atual, sem isso eu não consigo
    # executar o código diretamente, apenas pela classe jogo
if (__name__ == '__main__'):
    jogar()
