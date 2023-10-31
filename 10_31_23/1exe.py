def listaNum():
    lista = []
    for n in range(5):
        numero = int(input(f'Adicione o {n + 1}º numero inteiro: '))
        lista.append(numero)
    return lista

def printLista(lista):
    print('Números da lista:')
    for numero in lista:
        print(numero, end=' ')
        print()

numeros = listaNum()
printLista(numeros)