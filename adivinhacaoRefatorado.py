import random

# numero_secreto: int = random.randrange(1, 101)
max_tentativas: int = 0
rodada: int = 1
pontos: int = 1000


def jogar_adivinhacao_refatorado():
    def gerar_linha_hashtags(comprimento):
        # Gera uma linha horizontal com hashtags.#
        return '#' * comprimento

    linha: str = gerar_linha_hashtags(80)
    texto_boas_vindas: str = 'Bem vindo(a) ao jogo de adivinhação'
    texto_regra: str = 'você terá 3 tentativas para acertar o número secreto'
    texto_boa_sorte: str = "Boa sorte!!!"

    print(linha)
    print(texto_boas_vindas)
    print("{:^80}".format(texto_boa_sorte + "" + texto_regra))
    print(linha)


def definir_nivel():
    global max_tentativas

    print('Selecione o nível de dificuldade do jogo:')
    print('(1) Fácil | (2) Normal | (3) Difícil\n')

    while True:
        try:
            nivel = int(input('Defina o nível: '))
            if nivel not in [1, 2, 3]:
                msg_invalido: str = 'ESSE NÍVEL NÃO EXISTE,' \
                                    'INSIRA UM NÍVEL VÁLIDO!'
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
    numero_secreto: int = gerar_numero_secreto()
    jogo_finalizou: bool = False

    while rodada <= max_tentativas and not jogo_finalizou:
        print(f'Tentativas {rodada} de {max_tentativas}')

        chute_do_usuario = input('Digite um número entre 1 e 100: ')

        if not chute_do_usuario.isdigit() or int(chute_do_usuario) < 1 \
                or int(chute_do_usuario) > 100:
            print("Entrada inválida. Digite um número entre 1 e 100.")
            rodada += 1
            continue

        chute_convertido_com_casting = int(chute_do_usuario)

        acertou_numero_secreto = chute_convertido_com_casting == \
                                 numero_secreto
        chute_maior_que_numero_secreto = chute_convertido_com_casting > \
                                         numero_secreto
        chute_menor_que_numero_secreto = chute_convertido_com_casting < \
                                         numero_secreto

        if acertou_numero_secreto:
            msg_acertou = 'Parabéns!!! Você acertou o número secreto é'
            print(f'{msg_acertou}: {numero_secreto} e você fez {pontos}',
                  pontos)
            break

        else:
            if chute_maior_que_numero_secreto:
                msg_maior: str = 'Você errou!!!'
                msg_dica: str = 'Dica: Número digitado é maior' \
                                'que o número secreto'
                print(f'{msg_maior}, {msg_dica}')
            elif chute_menor_que_numero_secreto:
                msg_menor: str = 'Você errou!!!'
                msg_dica: str = 'Dica: Número digitado é menor' \
                                'que o número secreto'
                print(f'{msg_menor}, {msg_dica}')
            calculo_abs: int = abs(
                numero_secreto - chute_convertido_com_casting)
            pontos_perdidos: int = calculo_abs
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
