#Faça um programa que peça o primeiro nome do usuario, se o nome tiver 4 letras ou
#menos escreve ''Seu nome é curto'', se tiver entre 5 e 6 letras, escreva
#''Seu nome é normal'', maior que 6 ''seu nome é muito grande. 

nome_usuario = input("Digite o seu nome: ")
nome = len(nome_usuario)

if nome < 5:
    print("Seu nome é muito curto.")
elif nome >= 5 and nome <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")