"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita).

O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.

Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

valor_horas = float(input('Digite o valor que você ganha por hora: '))
horas_mes = int(input('Digite suas horas trabalhadas no mês: '))

salario_bruto = valor_horas * horas_mes

if salario_bruto < 900:
    salario_total = salario_bruto
    imposto_inss = salario_bruto * (10 / 100)
    salario_bruto = salario_bruto - imposto_inss
    desconto_fgts = salario_bruto * (11 / 100)
    salario_bruto = desconto_fgts - salario_bruto
    total_desconto = imposto_inss + desconto_fgts
    print(f'Salário Bruto: {salario_total:.2f}')
    print('(-) IR (5%) -INSENTO-')
    print(f'(-) INSS (10%) {imposto_inss:.2f}')
    print(f'FGTS (11%) {desconto_fgts:.2f}')
    print(f'Total de descontos: {total_desconto:.2f}')
    print(f'Salário Liquido : {salario_bruto:.2f}')
    
#não acabei a solução