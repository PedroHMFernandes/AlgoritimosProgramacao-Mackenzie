# 1. Faça um programa, utilizando funções, que receba três números inteiros e positivos, e que forneça a
# soma desses três números.
# Para este exercício crie três funções:
# • entrada() - retorna um número digitado (fazer a verificação se é positivo);
# • calculaSoma(a, b, c) - recebe 3 números inteiros e positivos e retorna a soma deles;
# • main() - chamada das funções criadas (chama 3 vezes a entrada, sendo uma para cada número e a
# função para somar) e depois mostre o resultado.

# def entrada():
#     n1 = int(input('Digite um número inteiro e positivo n1: '))
#     n2 = int(input('Digite um número inteiro e positivo n2: ')) 
#     n3 = int(input('Digite um número inteiro e positivo n3: '))
#     while n1 or n2 or n3 < 0:
#         if n1 < 0:
#             n1 = int(input('n1 deve ser positivo: '))
#         if n2 < 0:
#             n2 = int(input('n2 deve ser positivo: '))
#         if n3 < 0:
#             n3 = int(input('n3 deve ser positivo: '))
#     return n1, n2, n3

def entrada():
    num = int(input('Digite um número inteiro e positivo: '))
    while num <0 :
        num = int(input('num deve ser positivo: '))
    return num

def calculaSoma(a, b, c):
    return a + b + c

# n1, n2, n3 = entrada()
# soma = calculaSoma(n1, n2, n3)

def main():
    a = entrada()
    print()
    b = entrada()
    print()
    c = entrada()
    print()
    print(f'Soma = {calculaSoma(a, b, c)}')

main()
