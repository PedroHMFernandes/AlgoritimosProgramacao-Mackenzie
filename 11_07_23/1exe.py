# Faça um programa em Python que leia duas listas – uma com peso e a outra com a altura de 5 pessoas.
# Construir uma lista de mesmo tamanho com o índice de massa corporal de cada pessoa (IMC).
# IMC = peso/(altura)2
# UTILIZAR FUNÇÕES PARA A ENTRADA DE DADOS, PROCESSAMENTO E SAÍDA


def entrada():
    lista_peso = []
    lista_altura = []
    for i in range(5):
        print(f'Digite o peso(Kg) da pessoa {i + 1}: ')
        peso = int(input())
        lista_peso.append(peso)
        print(f'Digite a altura(m) da pessoa {i + 1}: ')
        altura = float(input())
        lista_altura.append(altura)
        print()
    return lista_peso, lista_altura


def calcula_IMC(peso, altura):
    lista_imc = []
    for i in range(len(peso)):
        imc = peso[i] / (altura[i]**2)
        lista_imc.append(imc)
    return lista_imc


def saida_IMC(peso, altura, imc):
    for i in range(len(imc)):
        print(
            f'{i + 1}ª pessoa: peso = {peso[i]}, altura = {altura[i]:.2f}, imc= {imc[i]:.2f}\n')


pesos, alturas = entrada()
lista_imc = calcula_IMC(pesos, alturas)
saida_IMC(pesos, alturas, lista_imc)
