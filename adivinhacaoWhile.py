# Jogo de adivinhação
# Regras: O usuário digitará um número e o programa retornará se ele acertou ou não este número
# Definir um número qualquer


print('########################################################################################')
print('Bem vindo(a) ao jogo de adivinhação, você terá 3 tentativas para acerta o número secreto')
print('                                     Boa sorte!!!')
print('########################################################################################')

numero_secreto = 42
max_tentativas = 3
rodada = 1

while(rodada <= max_tentativas):

    print('Tentativas {0} de {1}'.format(rodada,max_tentativas))
 # função que permite que o usuário digite um valor no console
    chute_do_usuario = input("Digite seu número:")
    chute_do_usuario = input("Digite um número entre 1 e 100: ")

# Conversão da entrada do usuário de str(String) para int, assim consigo fazer a comparação
    chute_convertido_utilizando_cast = int(chute_do_usuario)

 # Verificação se o número digitado está entre 1 ou 100
    if(chute_convertido_utilizando_cast < 1 or chute_convertido_utilizando_cast >= 100):
        continue
# Declaração de variáveis com possiveis tipos de acerto
    acertou_numero_secreto = chute_convertido_utilizando_cast == numero_secreto
    chute_maior_que_numero_secreto = chute_convertido_utilizando_cast > numero_secreto
    chute_menor_que_numero_secreto = chute_convertido_utilizando_cast < numero_secreto

# Testendo condições
    if acertou_numero_secreto:
        print('Parabéns!!! Você acertou o número secreto')
        break
    else:
        if chute_maior_que_numero_secreto:
            print('Você errou!!! Dica: O número digitado é maior que o número secreto')
        elif chute_menor_que_numero_secreto:
            print('Você errou!!! Dica: O número digitado é menor que o número secreto')

    rodada = rodada  + 1


print("## Fim do jogo ##")
