a = 2
b = 34.88
c = a + b
print('Valor de a =', a)
print('Valor de b = ', b, 'e tal coisa', a)
print('Valor de a= %d' %a)
print('Valor de b = %.2f' %b)
print(f'f-strings são as melhores; a + b = {a+b}')
print(f'a + b = {a+b:.5f}')

salario_hora = int(input())
hora_mes= int(input())
salario_mes = salario_hora * hora_mes
print(f'{salario_mes}')

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
media = (n1 + n2 + n3 + n4) / 4
print(media)