# 5) Faça um programa que receba o custo de um espetáculo teatral e o preço do ingresso desse espetáculo.
# Esse programa deve calcular e mostrar:
# a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.
# b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.
from math import ceil
custo_espetaculo = float(input('Custo do espetáculo: R$'))
preco_ingresso = float(input('Preço do ingresso: R$'))
# a)
minimo_de_ingresso = ceil(custo_espetaculo / preco_ingresso) 
# b)
espetaculo_com_lucro = custo_espetaculo * 1.23
lucro_ingresso = ceil(espetaculo_com_lucro/preco_ingresso)

print(f'O mínimo de ingressos vendidos de ser: {minimo_de_ingresso}')
print(f'Quantidade de ingressos para ter 23% de lucro: {lucro_ingresso}')
print(f'Valor total com 23% de lucro: R${espetaculo_com_lucro:.2f}')