# 3. Faça um programa, utilizando funções, que retorne o valor de um produto já com o imposto. Deverão ser
# utilizado dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
# porcentagem e custo, que é o custo de um item antes do imposto.
# Para este exercício crie três funções:
# • entrada() - serve para retornar tanto o custo do produto quanto a porcentagem do imposto;
# • somaImposto(porc, custo) - recebe o valor da porcentagem do imposto e o custo do produto.
# Retorna o novo custo do produto já com o imposto.


def entrada():
    custo = float(input('Custo: R$'))
    taxaImposto = float(input('Taxa de imposto [0.00 até 1.00]: '))
    return custo, taxaImposto

def somaImposto(porc, custo):
    novo_preco = custo + (custo * porc)
    return novo_preco 

custo, porc = entrada()
print(f'R${somaImposto(porc, custo):.2f}')