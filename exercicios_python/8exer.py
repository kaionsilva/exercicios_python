#Faça um programa que peça ao usuário para digitar um número inteiro,
#informe se este número é par ou impar. Caso o usuário não digitar um número inteiro
#informe, que não é um número inteiro.

numero_usuario = input('Digite um número: ')

if numero_usuario.isdigit():

    entrada = int(numero_usuario)
    resultado = entrada % 2 == 0
    if resultado:
        print('Seu número é par.')
    else:
        print('Seu número é impar.')
else:
    print('Você não digitou um número inteiro.')    