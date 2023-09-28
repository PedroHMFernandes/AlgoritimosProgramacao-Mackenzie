# 6) Dado o preço de um produto (valor inteiro), elabore um programa que calcule e apresente a menor
# quantidade de notas, de cada valor, necessárias para efetuar o pagamento da compra desse produto.
# Considere como valores das notas: 1, 2, 5, 10, 20, 50 e 100. 

preco = int(input('Entre com preço truncado do produto: R$'))

notas_100 = preco // 100
novo_preco = preco - notas_100 * 100

notas_50 = novo_preco // 50
novo_preco -= notas_50 * 50

notas_20 = novo_preco // 20
novo_preco -= notas_20 * 20

notas_10 = novo_preco // 10
novo_preco -= notas_10 * 10

notas_5 = novo_preco // 5
novo_preco -= notas_5 * 5

notas_2 = novo_preco // 2
novo_preco -= notas_5 * 2

notas_1 = novo_preco

print(f'100: {notas_100}')
print(f'50: {notas_50}')
print(f'20: {notas_20}')
print(f'10: {notas_10}')
print(f'5: {notas_5}')
print(f'2: {notas_2}')
print(f'1: {notas_1}')