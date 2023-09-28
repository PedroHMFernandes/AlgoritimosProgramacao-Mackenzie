# 5) Faça um programa que leia um número n (positivo) que indique quantos valores inteiros e
# positivos devem ser lidos a seguir. Para cada número lido, mostre o valor lido e o fatorial desse
# valor.

numero_entradas = int(input('Quantos fatoriais calcular: '))

for entradas in range(numero_entradas):
    numero_fatorial = int(input('Calcular fatorial de: '))
    resultado_fatorial = 1
    if numero_fatorial == 0:
        print(f'{numero_fatorial}! = 1')
    else:
        print(f'{numero_fatorial}!: ', end='')
        for num in range(numero_fatorial, 0, -1):
            print(f'{num}', end=' x ' if num >
                  1 else f' = {resultado_fatorial}\n')
            resultado_fatorial *= num
