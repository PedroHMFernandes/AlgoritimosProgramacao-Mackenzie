# 4) Faça um programa que tendo como dados de entrada o código de região de localização do cliente,
# o nome do cliente, o número de peças vendidas e o nome do vendedor; calcule e informe o valor do
# frete, a comissão do vendedor e o lucro obtido com a venda, sabendo-se que:
#  - O valor do frete depende da quantidade transportada e da região;
#  - Custo por peça = R$ 7,00;
#  - Custo total = custo por peça * número de peças vendidas;
#  - Valor total da venda = custo total acrescido de 50%;
#  - Comissão do vendedor = 6,5 % do valor total da venda;
#  - Lucro = Valor total venda – custo total – comissão do vendedor;

print('(1) Sul')
print('(2) Norte')
print('(3) Leste')
print('(4) Oeste')

codigo_regiao = int(input('Código da região:'))
while codigo_regiao not in (1, 2, 3, 4):
    print('Código inválido, tente novamente.')
    codigo_regiao = int(input('Código da região: '))
cliente_nome = str(input('Nome do cliente: '))
pecas_vendidas = int(input('Quantidade de peças vendidas: '))
vendedor_nome = str(input('Nome do vendedor: '))

if codigo_regiao == 1:
    regiao = 'Sul'
    frete = 1 if pecas_vendidas <= 1000 else 0.9
elif codigo_regiao == 2:
    regiao = 'Norte'
    frete = 1.10 if pecas_vendidas <= 1000 else 1
elif codigo_regiao == 3:
    regiao = 'Leste'
    frete = 1.15 if pecas_vendidas <= 1000 else 1.10
else:
    regiao = 'Oeste'
    frete = 1.20 if pecas_vendidas <= 1000 else 1.15

CUSTO_PECA = 7

custo_total_peca = CUSTO_PECA * pecas_vendidas
valor_total_venda = custo_total_peca * 1.50
frete_total = frete * pecas_vendidas
comissao_vendedor = valor_total_venda * 0.065
lucro = valor_total_venda - custo_total_peca - comissao_vendedor

print(f'Frete para {regiao}: {frete_total:.2f}')
print(f'Comissão do vendedor {vendedor_nome}: {comissao_vendedor:.2f}')
print(f'Lucro: {lucro:.2f}')
