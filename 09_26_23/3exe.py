# 3) Faça um programa que calcule e apresente o fatorial de um número inteiro e natural fornecido
# pelo usuário.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120.
# Por definição 0! = 1.

numero_fatorial = int(input('Calcular fatorial de: '))
resultado_fatorial = 1
if numero_fatorial == 0:
    print(f'{numero_fatorial}! = 1')
else:
    print(f'{numero_fatorial}!: ', end='')
    for num in range(numero_fatorial, 0, -1):
        print(f'{num}', end=' x ' if num > 1 else f' = {resultado_fatorial}')
        resultado_fatorial *= num
