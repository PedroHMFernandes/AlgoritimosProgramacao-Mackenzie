# 4) Escreva um programa que receba três números inteiros quaisquer e apresente:
# a) a soma dos quadrados dos três números;
# b) o quadrado da soma dos três números.

n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))
n3 = int(input('Digite n3: '))
soma_quadrados = n1**2 + n2**2 + n3**2
quadrado_da_soma = (n1 + n2 + n3)**2
print(f'Soma dos quadrados: {soma_quadrados}')
print(f'Quadrado da soma: {quadrado_da_soma}')