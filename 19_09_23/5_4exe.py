# 4) Faça um programa que solicite números inteiros e determine a soma e quantidade de números
# digitados enquanto o usuário não digitar -1. Ao final é informado a soma e quantidade de números
# digitados, exceto o -1. 

soma = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == -1:
        break
    elif n % 2 == 0:
        print(f'{n} é par')
    else:
        print(f'{n} é ímpar')
    cont += 1
    soma += n
print(f'Foram digitados {cont} números')
print(f'A soma dos números é {soma}')