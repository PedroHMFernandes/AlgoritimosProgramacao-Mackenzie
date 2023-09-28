# 7)Elabore um programa que calcule e apresente o valor de S, dado por:
# 𝑆 = 1/N + 2/(N − 1) + 3/(N − 2) + ⋯ + (N − 1)/2 + N
# Sendo N fornecido pelo usuário.

tirador = 0
quociente = 1
s = 0

n = int(input('Valor de n: '))
bode_espiatorio = n
while bode_espiatorio > 2:
    s += quociente/(n-tirador)
    quociente += 1
    tirador += 1
    bode_espiatorio -= tirador

s += (n-1)/2 + n
print(f's = {s}')
