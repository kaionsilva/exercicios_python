#Escreva um programa que permita inserir o nome e o poder de ataque de um personagem, depois o nome, a quantidade de pontos de vida, o poder de defesa de outro personagem 
#e se ele possui um escudo,
#e então calcule a quantidade de dano causado baseado nas seguintes regras:
#Se o poder de ataque for maior do que a defesa e o defensor não possuir um escudo, o dano causado será igual a diferença entre o ataque e a defesa.
#Se o poder de ataque for maior do que a defesa e o defensor possuir um escudo, o dano causado será igual a metade da diferença entre o ataque e a defesa.
#Se o poder de ataque for menor ou igual a defesa, o dano causado será 0.
#Por fim, o programa deve subtrair a quantidade de dano da quantidade de pontos de vida do personagem defensor e exibir na tela a quantidade de dano e 
#as informações atualizadas de ambos os personagens.

#nome_usuario = input('Digite o nome do seu personagem: ')
#nome_usuario_inimigo = input('Digite o nome do seu inimigo: ')


poder_ataque = int(input('Digite o seu poder de ataque: '))
quant_vida = int(input('Digite a quantidade de vida do seu inimigo : '))
quant_def = int(input('Digite a quantidade de defesa do seu inimigo: '))

inimigo_escudo = input('Seu inimigo possui escudo? [Y] ou [N]').lower()

if inimigo_escudo == 'y':
    inimigo_escudo = True
elif inimigo_escudo == 'n':
    inimigo_escudo = False
        
dano_causado = 0
if poder_ataque > quant_def and inimigo_escudo:
    dano_causado = poder_ataque - quant_def
    quant_vida = quant_vida - dano_causado

elif poder_ataque > quant_def and not inimigo_escudo:
     dano_causado = poder_ataque - quant_def
     dano_causado = dano_causado / 2
     quant_vida = quant_vida - dano_causado

elif poder_ataque <= quant_def:
    dano_causado = 0

print(f'O seu personagem nome: {nome_usuario} com poder de ataque: {poder_ataque}.')
print(f'Causou: {dano_causado} de dano no inimigo.')
print(f'O seu inimigo ficou com: {quant_vida} de vida.')