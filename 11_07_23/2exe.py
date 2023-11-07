# 2. Escreva um programa em Python que leia duas listas de 20 números inteiros cada e armazene em uma lista de mesmo
# tamanho a soma de cada elemento das duas listas. Exibir as três listas.
# Faça uma implementação utilizando função. Na implementação com funções NÃO UTILIZE variáveis GLOBAIS.
# Teste:

def cria_lista(numero_da_lista=1):
    lista = []
    print(f'Digite 5 números inteiros da lista {numero_da_lista}:')
    for n in range(5):
        numero = int(input())
        lista.append(numero)
    return lista


def soma_duas_listas(lista1, lista2):
    lista_soma = []
    for n in range(len(lista1)):
        soma = lista1[n] + lista2[n]
        lista_soma.append(soma)
    return lista_soma


lista_1 = cria_lista(1)
lista_2 = cria_lista(2)
somas = soma_duas_listas(lista_1, lista_2)
print(f'Lista 1: {lista_1}')
print(f'Lista 2: {lista_2}')
print(f'Soma: {somas}')
