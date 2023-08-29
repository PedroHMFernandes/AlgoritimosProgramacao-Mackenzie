# 1) Escreva um programa que lê dois valores inteiros e exibe os seguintes resultados:
# a) o resultado do primeiro número dividido pelo segundo número
# b) o resultado da divisão truncada do primeiro número pelo segundo número

n1 = int(input('Digite n1:'))
n2 = int(input('Digite n2:'))

divisao_n1_por_n2 = n1 / n2
truncado_n1_por_n2 = n1 // n2

print(f'n1 / n2 = {divisao_n1_por_n2}')
print(f'n1 // n2 = {truncado_n1_por_n2}')