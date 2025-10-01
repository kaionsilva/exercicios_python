"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média.

A atribuição de conceitos obedece à tabela abaixo:
    Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0         A
    Entre 7.5 e 9.0          B
    Entre 6.0 e 7.5          C
    Entre 4.0 e 6.0          D
    Entre 4.0 e zero         E

O algoritmo deve mostrar na tela as notas, a média,
o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
ou “REPROVADO” se o conceito for D ou E.
"""

primeira_nota = float(input('Qual sua PRIMEIRA nota? '))
segunda_nota = float(input('Qual sua SEGUNDA nota? '))

nota_media = (primeira_nota + segunda_nota) / 2

if nota_media > 6.0 and nota_media <= 7.5:
    print('Aprovado! (CONCEITO: C)')
elif nota_media > 7.5 and nota_media < 9.0:
    print('Aprovado! (CONCEITO: B)')
elif nota_media > 9.0:
    print('Aprovado! (CONCEITO: A)')
elif nota_media >= 4 and nota_media <= 6.0:
    print('Reprovado! (CONCEITO: D)')
elif nota_media < 4:
    print('Reprovado! (CONCEITO: E)')
