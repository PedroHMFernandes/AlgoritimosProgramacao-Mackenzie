def criaLista():
    lista = []
    for n in range(10):
        numero = int(input('Digite numero inteiro: '))
        lista.append(numero)
    return lista

def printReverso(lista):
    for n in range(len(lista), 0, -1):
        print(lista[n - 1], end='; ')
    print()

lista = criaLista()
printReverso(lista)