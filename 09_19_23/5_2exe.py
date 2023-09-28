# 2) Faça um programa que solicite números inteiros e determine se eles são ímpares ou pares
# enquanto o usuário não digitar -1. 

while True:
    n = int(input('Digite um número: '))
    if n == -1:
        break
    elif n % 2 == 0:
        print(f'{n} é par')
    else:
        print(f'{n} é ímpar')