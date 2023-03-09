

print('########################################################################################')
print('Bem vindo(a) ao mundo python, escolha o seu jogo')
print('                                     Boa sorte!!!')
print('########################################################################################')


print('(1) Adivinhação For (2) Adivinhação While (3) Forca')

resp_usuario = int(input("Selecione a opção do jogo: "))
adivinhacao_for = resp_usuario == 1
adivinhacao_while = resp_usuario == 2
forca = resp_usuario == 3

if (resp_usuario ==1):
    print('você selecionou a opção adivinhação For')
elif(resp_usuario ==2):
    print('você selecionou a opção adivinhação While')
elif (resp_usuario==3):
    print('você selecionou a opção adivinhação forca')
else:
     print('opção inválida')

print("## Fim do jogo ##")
