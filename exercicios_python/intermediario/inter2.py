#Faça uma calculadora na qual o usuario digite 2 números e escolha o operador que deseja
#Vamos usar apenas os operadores de: adição, multiplicação, subtração e divisão
#não precisa se preocupar na validação do usuario

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
operador_usuario = input('Qual operador deseja? [D]ivisão, [S]ubtração, [A]dição ou [M]ultiplicação: ').lower()


escolha_usuario = True

while escolha_usuario:

    if operador_usuario == 'd':
        print('Você escolheu o operador DIVISÃO: ')
        total = primeiro_numero / segundo_numero
        print(f'Resultado: {total}')

    elif operador_usuario == 's':
        print('Você escolheu o operador DIVISÃO: ')
        total = primeiro_numero - segundo_numero
        print(f'Resultado: {total}')

    elif operador_usuario == 'a':
        print('Você escolheu o operador DIVISÃO: ')
        total = primeiro_numero + segundo_numero
        print(f'Resultado: {total}')

    elif operador_usuario == 'm':
        print('Você escolheu o operador DIVISÃO: ')
        total = primeiro_numero * segundo_numero
        print(f'Resultado: {total}')

    escolha_usuario = input('Deseja continuar a usar calculadora? [Y] ou [N]').lower()
    if escolha_usuario == 'y':
        escolha_usuario = True
        primeiro_numero = int(input('Digite o primeiro número: '))
        segundo_numero = int(input('Digite o segundo número: '))
        operador_usuario = input('Qual operador deseja? [D]ivisão, [S]ubtração, [A]dição ou [M]ultiplicação: ').lower()

    else:
        escolha_usuario = False

print('Você usou a calculadora usando while.')