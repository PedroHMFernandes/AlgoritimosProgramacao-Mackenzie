# 2. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O
# resultado do atleta será determinado pela média dos cinco valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
# atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
# O programa deve ser encerrado quando for informado “sair” no nome do atleta.


lista_salto = []
while True:
    nome_atleta = input('Atleta: ').title()
    if nome_atleta == 'Sair':
        break
    for s in range(5):
        salto = float(input(f'{s + 1}º Salto: '))
        lista_salto.append(salto)
    somatorio_saltos = sum(lista_salto)
    media = somatorio_saltos / len(lista_salto)
    print('\nResultado final:')
    print(f'Atleta: {nome_atleta}')
    print('Saltos:', end=' ')
    for salto in lista_salto:
        print(salto, end=' - ' if salto != lista_salto[-1] else '\n')
    print(f'Média dos saltos: {media:.1f}m')
    print()
