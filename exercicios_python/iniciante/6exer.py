
#Faça um Programa que calcule a área de um quadrado,
#em seguida mostre o dobro desta área para o usuário.

lado_esquerdo = float(input('Digite a medida do lado esquerdo: '))
print('Não necessário o valor do lado direito pois ambos tem o mesmo valor.')

area_quadrado = lado_esquerdo * lado_esquerdo
dobro = area_quadrado * 2
print(f'O resultado da área do quadrado é: {area_quadrado:.2f}')
print(f'O dobro da área é: {dobro:.2f}')