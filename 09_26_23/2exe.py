# 2) Escreva um programa que apresente os n (1 <= n <= 20) primeiros termos da seguinte sequência:
# 1, 4, 9, 16, 25, ...

numeros_sequencia = 0
while numeros_sequencia < 1 or numeros_sequencia > 20:
    numeros_sequencia = int(input('De 1 - 20, quantos números na sequência: '))

for numero in range(1, numeros_sequencia + 1):
    print(numero**2, end=' ')
