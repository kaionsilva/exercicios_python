
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

diaria = float(input('Digite o valor que você ganha por hora: '))
horas = float(input('Digite a quantidade horas que você trabalhou: '))

total = diaria * horas

print(f'Total do seu salário: {total:.2f}')