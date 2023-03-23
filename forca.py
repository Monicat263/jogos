def jogar():
    print('#' * 65)
    print('Bem vindo(a) ao jogo de forca')
    print('                        Boa sorte!!!')
    print('#' * 65)

    palavra_secreta = 'BANANA'

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input('Digite uma letra: ').lower()


        posicao = 0
        for letra in palavra_secreta:
            if (chute == letra.lower()):
                print('Encontrei a letra {}	na posição	{}'.format(letra, posicao))
            posicao = posicao + 1
        print('Jogando...')

    print("## Fim do jogo ##")


    # função necessária para rodar a classe atual, sem isso eu não consigo
    # executar o código diretamente, apenas pela classe jogo
if (__name__ == '__main__'):
    jogar()
