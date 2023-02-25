#Jogo de adivinhação
#Regras: O usuário digitará um número e o programa retornará se ele acertou ou não este número
#Definir um número qualquer
numero_secreto = 42

# função que permite que o usuário digite um valor no console
chute_do_usuario = input ('Digite seu número:')
print("Você digitou: ", chute_do_usuario )
#Conversão da entrada do usuário de str(String) para int, assim consigo fazer a comparação
chute_convertido_utilizando_cast = int(chute_do_usuario)

acertou_numero_secreto = numero_secreto == chute_convertido_utilizando_cast
chute_maior_que_numero_secreto = chute_convertido_utilizando_cast > numero_secreto
chute_mmenor_que_numero_secreto = chute_convertido_utilizando_cast < numero_secreto

if(acertou_numero_secreto):
     print('Parabéns!!! Você acertou o número secreto')
else:
    if(chute_maior_que_numero_secreto):
        print("Você errou!!! Dica: O número digitado é maior que o número secreto")
    elif(chute_mmenor_que_numero_secreto):
        print("Você errou!!! Dica: O número digitado é menor que o número secreto")

print('## Fim do jogo ##')




