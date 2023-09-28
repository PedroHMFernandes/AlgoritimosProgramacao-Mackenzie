# 6) Faça um programa que solicite 10 números inteiros entre 1 a 10 e apresenta a média aritmética
# entre eles. O programa deverá fazer uma validação de forma que o usuário obrigatoriamente
# somente digite números neste intervalo

soma = 0
for n in range(10):
    numeros = int(input('Digite números inteiros entre 1 e 10: '))
    while numeros < 1 or numeros > 10:
        numeros = int(input('Valor Inválido! Digite números inteiros entre 1 e 10: '))
    soma += numeros
    print(soma)
    if n == 9:
        media = soma/10    
print(media)