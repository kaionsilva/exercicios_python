"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

escolha_usuario = input('Escolha sua letra: ').lower()

if escolha_usuario == 'a' or \
    escolha_usuario == 'e' or \
    escolha_usuario == 'i' or \
    escolha_usuario == 'o' or \
    escolha_usuario == 'u':

    print('É uma vogal.')
else:
    print('Não é uma vogal.')