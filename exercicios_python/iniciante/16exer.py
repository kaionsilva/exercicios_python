"""
Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

preco_um = float(input('Digite o valor do primeiro produto: '))
preco_dois = float(input('Digite o valor do segundo produto: '))
preco_tres = float(input('Digite o valor do terceiro produto: '))

if preco_um < preco_dois and preco_um < preco_tres:
    print('Compre o produto um, é o mais barato.')
elif preco_dois < preco_um and preco_dois < preco_tres:
    print('Compre o produto dois, é o mais barato.')
else:
    print('Compre o produto três, é o mais barato.')