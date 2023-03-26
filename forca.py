def jogar():
    print('#' * 65)
    print('Bem vindo(a) ao jogo de forca')
    print('                        Boa sorte!!!')
    print('#' * 65)

    palavra_secreta: str = 'BANANA'.lower()
    #para apresentar os espaçamentos de forma dinâmica
    letras_acertadas: list = [' _ '] * len(palavra_secreta)

    enforcou  = False
    acertou: bool = False
    erros: bool = False

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
            erros += 1
            # verificar se já atingiu o limite de tentativas
        enforcou = erros == 6
        # enquanto _ ñ existir dentro das letras acertadas ai pode encerrar
        acertou = ' _ ' not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        print(f'Parabéns, você acertou a palavra secreta é: {palavra_secreta}')
    else:
        print(f'Não foi dessa vez, você perdeu. A palavra secreta era: {palavra_secreta}')
    print("## Fim do jogo ##")

    # função necessária para rodar a classe atual, sem isso eu não consigo
    # executar o código diretamente, apenas pela classe jogo
if (__name__ == '__main__'):
    jogar()
