"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante :
        aumento de 5% Após o aumento ser realizado,
    informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
"""

salario_colaborador = float(input('Digite o seu salário: '))

if salario_colaborador < 280:
    print(f'Salário antes do reajuste: {salario_colaborador:.2f}')
    print('Você teve um aumento de 20% em seu salário.')
    valor_aumentado = salario_colaborador * (20 / 100)
    print(f'Valor do aumento: {valor_aumentado:.2f}')
    salario_colaborador = salario_colaborador + valor_aumentado
    print(f'Novo salário após aumento: {salario_colaborador:.2f}')

elif salario_colaborador >= 280 and salario_colaborador < 700:
    print(f'Salário antes do reajuste: {salario_colaborador:.2f}')
    print('Você teve um aumento de 15% em seu salário.')
    valor_aumentado = salario_colaborador * (15 / 100)
    print(f'Valor do aumento: {valor_aumentado:.2f}')
    salario_colaborador = salario_colaborador + valor_aumentado
    print(f'Novo salário após aumento: {salario_colaborador:.2f}')

elif salario_colaborador > 700 and salario_colaborador <= 1500:
    print(f'Salário antes do reajuste: {salario_colaborador:.2f}')
    print('Você teve um aumento de 10% em seu salário.')
    valor_aumentado = salario_colaborador * (10 / 100)
    print(f'Valor do aumento: {valor_aumentado:.2f}')
    salario_colaborador = salario_colaborador + valor_aumentado
    print(f'Novo salário após aumento: {salario_colaborador:.2f}')

elif salario_colaborador > 1500:
    print(f'Salário antes do reajuste: {salario_colaborador:.2f}')
    print('Você teve um aumento de 5% em seu salário.')
    valor_aumentado = salario_colaborador * (5 / 100)
    print(f'Valor do aumento: {valor_aumentado:.2f}')
    salario_colaborador = salario_colaborador + valor_aumentado
    print(f'Novo salário após aumento: {salario_colaborador:.2f}')

