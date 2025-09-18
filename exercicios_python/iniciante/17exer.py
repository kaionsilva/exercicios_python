"""
Faça um Programa que leia três números e mostre-os em ordem crescente.
"""

primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))
terceiro_numero = int(input('Terceiro número: '))

if  (primeiro_numero < segundo_numero and 
    segundo_numero < terceiro_numero):

    print(primeiro_numero)
    print(segundo_numero)
    print(terceiro_numero)
elif (segundo_numero < primeiro_numero and
      segundo_numero < terceiro_numero and
      primeiro_numero < terceiro_numero):
    
    print(segundo_numero)
    print(primeiro_numero)
    print(terceiro_numero)
elif (terceiro_numero < primeiro_numero and
      terceiro_numero < segundo_numero and
      segundo_numero < primeiro_numero):
    print(terceiro_numero)
    print(segundo_numero)
    print(primeiro_numero)