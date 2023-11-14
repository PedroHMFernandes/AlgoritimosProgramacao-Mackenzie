# 1. Faça um programa em Python que receba e armazene 10 números inteiros em uma
# lista.
# Após a entrada dos 10 números, solicite ao usuário um valor, faça a busca deste número
# na lista e emita a mensagem NÚMERO EXISTE caso o número informado pelo usuário
# esteja na lista de entrada ou NÚMERO NÃO EXISTE se o número informado não for
# localizado na lista.

lista = []
for n in range(10):
    add_num = int(input(f'Digite o {n+1}º número: '))
    lista.append(add_num)

find_num = int(input('Qual número você deseja procurar: '))
if find_num in lista:
    print('NÚMERO EXISTE')
else:
    print('NÚMERO NÃO EXISTE')
