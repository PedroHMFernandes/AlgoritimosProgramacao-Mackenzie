# 5) Programa que lê um inteiro positivo n e imprime o valor da soma destes números: 1 + 2 + 3 + ... +
# n. 

soma = 0
num = int(input('Digite um número: '))
for n in range(num + 1):
    soma += n
    if n != 0:
        print(f'{n}', end=' + ' if n < num else ' = ')
print(f'{soma}')