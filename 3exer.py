#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

primeiro_bimestre = float(input('Digite a nota do PRIMEIRO bimestre: '))
segundo_bimestre = float(input('Digite a nota do SEGUNDO bimestre: '))
terceiro_bimestre = float(input('Digite a nota do TERCEIRO bimestre: '))
quarto_bimestre = float(input('Digite a nota do QUARTO bimestre: '))

media_total = primeiro_bimestre + segundo_bimestre + terceiro_bimestre + quarto_bimestre / 4

print(f'A sua média total: {media_total:.2f}')