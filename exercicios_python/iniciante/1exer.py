#Faça um programa na qual mostre o seu nome, mostre os seu nome invertido, se contém ou não espaços 
#informe a primeira e última letra do seu nome e caso o usuário deixar campos vazios informar: 
#'você deixou campos vázios.'


nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')

    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')