"""
Faça um Programa que leia três números e mostre o maior deles.
"""

numero_um = int(input('Primeiro número: '))
numero_dois = int(input('Segundo número: '))
numero_tres = int(input('Terceiro número: '))

if numero_um > numero_dois and numero_um > numero_tres:
    print(f'O primeiro número é o maior: {numero_um}')
elif numero_dois > numero_um and numero_dois > numero_tres:
    print(f'O segundo número é o maior: {numero_dois}')
else:
    print(f'O terceiro número é o maior: {numero_tres}')

    