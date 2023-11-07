# 3. Escreva um programa em Python com a seguinte lista de inteiros:
# lista = [13, 41, 13, 8, 21, 7, 79] Calcule
# e mostre:
# • o valor do maior elemento desta lista (NÃO UTILIZE o max);
# • o valor do menor elemento desta lista (NÃO UTILIZE o min);
# • o número de vezes que um determinado número, digitado pelo usuário, aparece nesta lista (NÃO UTILIZE o
# count)


def calcula_maior(lista):
    maior = 0
    for key, numero in enumerate(lista):
        if key == 0:
            maior = numero
        if numero > maior:
            maior = numero
    return maior


def calcula_menor(lista):
    menor = 0
    for key, numero in enumerate(lista):
        if key == 0:
            menor = numero
        if numero < menor:
            menor = numero
    return menor


def calcule_repeticao(num, lista):
    contador = 0
    for numero in lista:
        if num == numero:
            contador += 1
    return f'Número de ocorrências do número {num} na lista: {contador}'


lista = [13, 41, 13, 8, 21, 7, 79]
numero_pesquisado = int(input('Digite o número a ser pesquisado: '))
maior = calcula_maior(lista)
menor = calcula_menor(lista)
print(f'Maior elemento:{maior}')
print(f'Menor elemento: {menor}')
print(calcule_repeticao(numero_pesquisado, lista))
