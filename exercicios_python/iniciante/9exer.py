#Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
#descrito, exiba a saudação apropriada. ex:
#bom dia 00-11, boa tarde 11-17, boa noite 18--23

horario_usuario = int(input('Que horas são? '))

if horario_usuario <= 11:
    print('Bom dia!')

elif horario_usuario > 11 and horario_usuario <= 17:
    print('Boa tarde!')

else:
    print('Boa noite! ')