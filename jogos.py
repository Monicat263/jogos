# Classe principal responsavel por disponibilizar as opções de jogos para o o usuário selecionar#
import adivinhacaoFor
import adivinhacaoWhile
import forca
def jogar_forca():
    print('########################################################################################')
    print('Bem vindo(a) ao mundo python, escolha o seu jogo')
    print('                                     Boa sorte!!!')
    print('########################################################################################')

#opções de jogos
print('(1) Forca (2) Adivinhação While (3) Adivinhação For')

#conversão resposta do usuário de String para int
resp_usuario = int(input("Selecione a opção do jogo: "))

if (resp_usuario ==1):
    print('você selecionou a opção Forca')
    # chamando a função da classes
    forca.jogar()
elif(resp_usuario ==2):
    print('você selecionou a opção adivinhação While')
    adivinhacaoWhile.jogar_adivinhacao_while()
elif (resp_usuario==3):
    print('você selecionou a opção adivinhação adivinhação For')
    adivinhacaoFor.jogar_adivinhacao_for()
else:
     print('opção inválida')

print("## Fim do jogo ##")
