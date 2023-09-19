# 1) Faça um programa que solicite 5 números inteiros e determine se eles são ímpares ou pares.

for num in range(5):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        print(f'{n} é par')
    else:
        print(f'{n} é ímpar')
