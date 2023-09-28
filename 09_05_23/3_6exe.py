# 6) Dado o preço de um produto (valor inteiro), elabore um programa que calcule e apresente a menor
# quantidade de notas, de cada valor, necessárias para efetuar o pagamento da compra desse produto.
# Considere como valores das notas: 1, 2, 5, 10, 20, 50 e 100. 

preco = int(input('Entre com preço truncado do produto: R$'))
novo_preco = preco

notas_100 = preco // 100
if notas_100:
    novo_preco = preco - notas_100 * 100
    print(f'Notas de 100: {notas_100}')

notas_50 = novo_preco // 50
if notas_50:
    novo_preco -= notas_50 * 50
    print(f'Notas de 50: {notas_50}')

notas_20 = novo_preco // 20
if notas_20:
    novo_preco -= notas_20 * 20
    print(f'Notas de 20: {notas_20}')

notas_10 = novo_preco // 10
if notas_10:
    novo_preco -= notas_10 * 10
    print(f'Notas de 10: {notas_10}')

notas_5 = novo_preco // 5
if notas_5:
    novo_preco -= notas_5 * 5
    print(f'Notas de 5: {notas_5}')

notas_2 = novo_preco // 2
if notas_2:
    novo_preco -= notas_2 * 2
    print(f'Notas de 2: {notas_2}')

if novo_preco:
    notas_1 = novo_preco
    print(f'Notas de 1: {notas_1}')
