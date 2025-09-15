#Tendo como dados de entrada a altura de uma pessoa,
#construa um algoritmo que calcule seu peso ideal minimo e maximo
#usando a seguinte fórmula: 
#imc ideal = 24.9
#formula: imc ideal * (altura elevado a 2)

altura_usuario = input("Qual a sua altura? ")
altura_usuario = (float(altura_usuario))

imc_min = 18.5
imc_ideal = 24.9
peso_ideal_max = imc_ideal * (altura_usuario ** 2)
peso_ideal_min = imc_min * (altura_usuario ** 2)

print(f'Seu peso ideal mínimo é: {peso_ideal_min:.1f}')
print(f'Seu peso ideal máximo é: {peso_ideal_max:.1f}')

