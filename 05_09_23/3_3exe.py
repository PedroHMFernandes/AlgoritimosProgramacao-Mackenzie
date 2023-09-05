# 3) Faça um programa que coloque dois nomes em ordem alfabética.
nome1 = str(input('Digite um nome: ')).title()
nome2 = str(input('Digite um nome: ')).title()

print('Ordem alfabética.')
if nome1 < nome2:
    print(nome1)
    print(nome2)
else:
    print(nome2)
    print(nome1)
    