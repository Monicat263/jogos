# Jogo de adivinhação
# Regras: O usuário digitará um número e o programa retornará se ele acertou ou não este número
# Pontos: Inicia o jogo com 1000 e a cada jogada
# Pontos perdidos: É a diferença entre os número secreto - o valor digitado subtraido da pontuação inicial

import random
def jogar_adivinhacao_while():
    def gerar_linha_hashtags(comprimento):
        """Gera uma linha horizontal com hashtags."""
        return '#' * comprimento

    linha = gerar_linha_hashtags(80)
    texto_boas_vindas = 'Bem vindo(a) ao jogo de adivinhação'
    texto_regra = 'você terá 3 tentativas para acertar o número secreto'
    texto_boa_sorte = "Boa sorte!!!"

    print(linha)
    print(texto_boas_vindas)
    print("{:^80}".format(texto_boa_sorte,texto_regra))
    print(linha)

    numero_secreto = random.randrange(1,101)
    max_tentativas = 3
    rodada = 1
    pontos = 1000

    #Escolha do usuário para nivel do jogo
    print('Selecione o nivel de dificuldade do jogo: ')
    print('(1) Fácil')
    print('(2) Médio')
    print('(3) Dificil')
    # variavel recebendo a input do usuário(String) e já convertendo para int
    nivel = int(input('Defina o nível: '))
    print(numero_secreto)

    while(nivel < 1 or nivel > 3 ):
        print('ESSE NÍVEL NÃO EXISTE, INSIRA UM NÍVEL VALIDO!\n')
        print('Escolha a dificuldade.')
        print('(1) Fácil | (2) Normal | (3) Difícil\n')
        nivel= int(input("Dificuldade: "))

        nivel_facil = nivel == 1
        nivel_medio = nivel == 2
        nivel_dificil = nivel == 3

        if(nivel_facil):
            max_tentativas = 8
        elif(nivel_medio):
            max_tentativas = 5
        elif(nivel_dificil):
            max_tentativas = 3

    while(rodada <= max_tentativas):
        print('Tentativas {0} de {1}'.format(rodada,max_tentativas))
    # função que permite que o usuário digite um valor no console
        chute_do_usuario = input('Digite um número entre 1 e 100:  ')
    # Conversão da entrada do usuário de str(String) para int, assim consigo fazer a comparação
        chute_convertido_utilizando_casting = int(chute_do_usuario)

    #Verificação se o número digitado está entre 1 ou 100 #
        if(chute_convertido_utilizando_casting < 1 or chute_convertido_utilizando_casting >= 100):
            continue
    # Declaração de variáveis com possiveis tipos de acerto
        acertou_numero_secreto = chute_convertido_utilizando_casting == numero_secreto
        chute_maior_que_numero_secreto = chute_convertido_utilizando_casting > numero_secreto
        chute_menor_que_numero_secreto = chute_convertido_utilizando_casting < numero_secreto

    # Testendo condições
        if acertou_numero_secreto:
            print('Parabéns!!! Você acertou o número secreto é: {} e você fez {} pontos'.format(numero_secreto,pontos))
            break
        else:
            if chute_maior_que_numero_secreto:
                print('Você errou!!! Dica: O número digitado é maior que o número secreto')
                if (rodada == max_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))
            elif chute_menor_que_numero_secreto:
                print('Você errou!!! Dica: O número digitado é menor que o número secreto')
                if (rodada == max_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))

            # Regra referente a pontos perdidos
        pontos_perdidos = abs(numero_secreto - chute_convertido_utilizando_casting)
        pontos = pontos - pontos_perdidos
        print(pontos)
        rodada = rodada +1

    print('## Fim do jogo ##')

# função necessária para rodar a classe atual, sem isso eu não consigo executar o código diretamente, apenas pela classe jogo
if(__name__=='__main__'):
   jogar_adivinhacao_while()

