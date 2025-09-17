"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

genero = input('Digite o seu gênero: ').lower()

if genero == 'f':
    print('Feminino.')
elif genero == 'm':
    print('Masculino.')
else:
    print('Sexo inválido.')