#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

pi = 3.1415926
raio = float(input('Digite o valor do raio: '))
area = pi * (raio ** 2)
print(f'A área do raio: {raio} é de: {area:.2f}')