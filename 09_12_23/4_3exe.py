# 3) Elabore um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?" 
# O programa deve, no final, emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
# responder Sim a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
# "Assassino". Caso contrário, ela será classificada como "Inocente".



print('Responda as seguintes perguntas:')

contador = 0

telefonou = input('Telefonou para a vítima?\n[Sim/Não]: ')[0].upper()
if telefonou == 'S':
    contador += 1
esteve_local = input('Esteve no local do crime?\n[Sim/Não]: ')[0].upper()
if esteve_local == 'S':
    contador += 1
mora_perto = input('Mora perto da vítima?\n[Sim/Não]: ')[0].upper()
if mora_perto == 'S':
    contador += 1
devia = input('Devia para a vítima?\n[Sim/Não]: ')[0].upper()
if devia == 'S':
    contador += 1
trabalhou = input('Já trabalhou com a vítima?\n[Sim/Não]: ')[0].upper()
if trabalhou == 'S':
    contador += 1
print(f'{contador=}')

if contador == 5:
    pessoa = 'Assassina'
elif contador >= 3:
    pessoa = 'Cúmplice'
elif contador == 2:
    pessoa = 'Suspeita'
else:
    pessoa = 'Inocente'

print(f'A pessoa é cosiderada: {pessoa}')