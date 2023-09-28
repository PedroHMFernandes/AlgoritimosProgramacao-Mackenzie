# 1) Faça um programa que leia um número inteiro (e diferente de zero) e mostre
# uma mensagem indicando se este número é positivo ou negativo.

num = int(input('Digite um número inteiro diferente de zero: '))

if num < 0:
    print(f'{num} é negativo')
elif num == 0:
    print('Zero é zero')
else:
    print(f'{num} é positivo')
