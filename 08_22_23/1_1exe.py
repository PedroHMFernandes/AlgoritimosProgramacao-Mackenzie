# 1. Faça um programa que leia 4 notas bimestrais de uma disciplina, calcule e mostre a média aritmética do
# bimestre.
soma_notas = 0
cont = 0

for n in range(4):
    nota = float(input(f'Nota da Prova {n+1}: '))
    soma_notas += nota
    cont += 1

media = soma_notas / cont
print(f'A média aritimética do bimestre é {media}')
