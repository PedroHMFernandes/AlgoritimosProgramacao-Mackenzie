# 5. Faça um programa que calcule e mostre o IMC (índice de massa corporal) de uma pessoa, considerando
# que ela irá dizer qual o seu peso e qual a sua altura ( imc = peso/(altura*altura) )
altura = float(input('Altura(m): '))
peso = int(input('Peso(Kg): '))
imc = peso / altura**2

if imc <= 18.5:
    classificacao = 'abaixo do peso'
elif imc <= 24.9:
    classificacao = 'peso ideal'
elif imc <= 29.9:
    classificacao = 'acima do peso'
elif imc <= 34.9:
    classificacao = 'obesidade grau I'
elif imc <= 39.9:
    classificacao = 'obesidade grau II (severa)'
else:
    classificacao = 'obesidade grau III (mórbida)'

print(f'Seu IMC é: {imc:.2f}')
print(f'Sua classificação é: {classificacao}')