# 2) Escreva um programa que lê dois valores em ponto flutuante e exiba os seguintes resultados:
# a) divisão do primeiro valor pelo segundo valor, sem formatação;
# b) divisão do primeiro valor pelo segundo valor, com exatamente seis dígitos depois da vírgula (para
# isso utilize a função format)

n1 = float(input('Digite n1:'))
n2 = float(input('Digite n2:'))

n1_por_n2 = n1 / n2

print(f'n1 / n2 = {n1_por_n2}')
print(f'n1 / n2 = {n1_por_n2:.6f}')


