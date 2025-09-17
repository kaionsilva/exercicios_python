"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

salario_hora = float(input('Quanto você ganha por hora? '))
horas_mes = float(input('Quantas horas você trabalha no mês: '))
salario_mes = salario_hora * horas_mes

imposto_de_renda = salario_mes * (0.11 / 100)
imposto_inss = salario_mes * (0.8 / 100)
imposto_sindicato = salario_mes * (0.5 /100)
salario_liquido = salario_mes - imposto_de_renda - imposto_inss - imposto_sindicato

print(f'Salário bruto: R${salario_mes:,.2f}\n' 
      f'Imposto de renda (11%): R${imposto_de_renda:.2f}\n' 
      f'Imposto INSS (8%): R${imposto_inss:.2f}\n'
      f'Imposto sindicato (5%): R${imposto_sindicato:.2f}\n' 
      f'Salário líquido: R${salario_liquido:,.2f}'
      )





