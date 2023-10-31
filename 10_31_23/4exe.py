def criaLista():
    lista = []
    for c in range(10):
        caracatere = input(f'Digite a {c + 1}ª letra: ').lower()
        lista.append(caracatere)
    return lista

def contaVogal(lista):
    contador = 0
    for letra in lista:
        if letra in 'aeiou':
            contador += 1
    return contador

def contaConsoante(lista):
    contador = 0
    for letra in lista:
        if letra not in 'aeiou':
            contador += 1
    return contador

def imprimeTudo(lista, vogal, consoante):
    print(f'Lista de letras: {lista}')
    print(f'Quantidade de vogais: {vogal}')
    print(f'Quantidade de consoantes: {consoante}')

caracteres = criaLista()
quantidade_vogais = contaVogal(caracteres)
quantidade_consoantes = contaConsoante(caracteres)
imprimeTudo(caracteres, quantidade_vogais, quantidade_consoantes)