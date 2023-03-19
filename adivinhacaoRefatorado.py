import random

texto1: str = '########################################################################################'
texto: str = 'Boa sorte!!!'
max_tentativas = 0
rodada = 1
pontos = 1000


def jogar_adivinhacao_refatorado():
    print(f'{texto1:^88}')
    print('Bem vindo(a) ao jogo de adivinhação ')
    print('Regras: Selecione o nivel de 1 a 3 para iniciar.')
    print('De acordo com o nível selecionado você terá mais ou menos tentativas para acerta o número secreto ')
    print('Sendo:')
    print('       Nivel (1) = 8 tentativas')
    print('       Nivel (2) = 5 tentativas')
    print('       Nivel (3) = 3 tentativas\n')
    print(f'{texto:^88}')
    print('########################################################################################')
    # utilizar caso queira loop do jogo
    # definir_nivel()


def definir_nivel():
    global max_tentativas

    print('Selecione o nível de dificuldade do jogo:')
    print('(1) Fácil | (2) Normal | (3) Difícil\n')

    while True:
        try:
            nivel = int(input('Defina o nível: '))
            if nivel not in [1, 2, 3]:
                msg_invalido = 'ESSE NÍVEL NÃO EXISTE, INSIRA UM NÍVEL VÁLIDO!'
                raise ValueError(msg_invalido)
            break
        except ValueError:
            print('Insira um valor válido entre 1 e 3\n')

    if nivel == 1:
        max_tentativas = 8
    elif nivel == 2:
        max_tentativas = 5
    else:
        max_tentativas = 3

    iniciar_rodada()


def gerar_numero_secreto():
    numero_secreto = random.randrange(1, 101)
    #  Impressão do número secreto gerado
    print(f'O número secreto é {numero_secreto}')
    return numero_secreto


def iniciar_rodada():
    global rodada, pontos
    numero_secreto = gerar_numero_secreto()
    jogo_finalizou = False

    while rodada <= max_tentativas and not jogo_finalizou:
        print(f'Tentativas {rodada} de {max_tentativas}')

        chute_do_usuario = input('Digite um número entre 1 e 100: ')

        if not chute_do_usuario.isdigit() or int(chute_do_usuario) < 1 \
                or int(chute_do_usuario) > 100:
            print("Entrada inválida. Digite um número entre 1 e 100.")
            rodada += 1
            continue

        chute_convertido_com_casting = int(chute_do_usuario)

        acertou_numero_secreto = chute_convertido_com_casting == numero_secreto
        chute_maior_que_numero_secreto = chute_convertido_com_casting > numero_secreto
        chute_menor_que_numero_secreto = chute_convertido_com_casting < numero_secreto

        if acertou_numero_secreto:
            msg_acertou = 'Parabéns!!! Você acertou o número secreto é'
            print(f'{msg_acertou}: {numero_secreto} e você fez {pontos}',
                  pontos)
            break

        else:
            if chute_maior_que_numero_secreto:
                msg_maior = 'Você errou!!!'
                msg_dica = 'Dica: Número digitado é maior que o número secreto'
                print(f'{msg_maior}, {msg_dica}')
            elif chute_menor_que_numero_secreto:
                msg_menor = 'Você errou!!!'
                msg_dica = 'Dica: Número digitado é menor que o número secreto'
                print(f'{msg_menor}, {msg_dica}')
            calculo_abs = abs(numero_secreto - chute_convertido_com_casting)
            pontos_perdidos = calculo_abs
            pontos = pontos - pontos_perdidos

            if rodada == max_tentativas:
                print(f'O número secreto era {numero_secreto}. '
                      f'Você fez {pontos} pontos')

        rodada += 1

    print('## Fim do jogo ##')


if __name__ == '__main__':
    numero_secreto_salvo = gerar_numero_secreto()
    jogar_adivinhacao_refatorado()
    definir_nivel()
