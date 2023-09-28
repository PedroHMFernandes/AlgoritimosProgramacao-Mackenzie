# A conversão de graus Fahrenheit para Celsius é obtida pela fórmula:
# 𝐶 = (5/9) * (𝐹 − 32)
# Escreva um programa que calcule e apresente uma tabela de graus Celsius em função de graus
# Fahrenheit que variem de 50 a 150, de 1 em 1.

for f in range(50, 151):
    c = (5/9) * (f - 32)
    print(f'{f}F° = {c:.2f}°C')
