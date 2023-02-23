#Jogo de adivinhação
#Regras: O usuário digitará um número e o programa retornará se ele acertou ou não este número

#Definir um número qualquer
numero_secreto = 42

# função que permite que o usuário digite um valor no console
chute_do_usuario = input ('Digite seu número:')
print("Você digitou: ", chute_do_usuario )
#Conversão da entrada do usuário de str(String) para int, assim consigo fazer a comparação
chute_convertido_utilizando_casting = int(chute_do_usuario)

if(numero_secreto == chute_convertido_utilizando_casting):
     print('Parabéns!!! Você acertou o número secreto')
else:
    print('Você não acertou o número secreto')
print('## Fim do jogo ##')


