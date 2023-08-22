# 4. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês 
# (modifiquei para dia).
# Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input('Digite o seu salário: R$'))
horas = int(input('Digite as horas trabalhadas por dia: '))
dias = int(input('Quantidade de dias trabalhados: '))

salario = salario_hora*horas*dias

print(f'Seu salário mensal é R${salario}')