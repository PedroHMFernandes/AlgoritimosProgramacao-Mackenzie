# 2) Faça um programa que apresenta o maior de dois números inteiros (diferentes)
# lidos do usuário.

n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))

if n1 > n2:
    print(f'{n1=} é maior que {n2=}')
elif n1 == n2:
    print(f'{n1=} é igual a {n2=}')
else:
    print(f'{n2=} é maior que {n1=}')