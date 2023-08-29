# 3) Calcule e apresente o volume de uma lata de óleo ( 𝑣 = 𝜋. 𝑟². 𝑎𝑙𝑡𝑢𝑟𝑎)
from math import pi

raio = float(input('Digite o raio(cm): '))
altura = float(input('Digite a altura (cm): '))
volume = pi * raio**2 * altura

print(f'Volume da lata de óleo: {volume:.2f}cm³')