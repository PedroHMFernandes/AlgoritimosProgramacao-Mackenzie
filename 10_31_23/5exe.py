def leiaNotas():
    lista_notas = []
    for n in range(4):
        nota = float(input(f'{n+1}ª Nota [0.0 - 10.0]:   '))
        while nota < 0 or nota > 10:
            print('Nota inválida! Digite novamente: ')
            nota = float(input(f'{n+1}ª Nota [0.0 - 10.0]:   '))
        lista_notas.append(nota)
    media = sum(lista_notas) / len(lista_notas)
    return media

def contaAprovados(lista_notas):
    contador = 0
    for nota in lista_notas:
        if nota >= 7:
            contador += 1
    return contador
        
def imprimeTudo(medias, quantidade_aprovados):
    print(f'{quantidade_aprovados} alunos foram aprovados')
    print('As médias foram:')
    for key, notas in enumerate(medias):
        print(f'Aluno {key + 1}: {notas:.1f}')
    print()
    

# quantidade_alunos = int(input('Quantos alunos você quer cadastrar: '))
lista_medias = []

# for n in range(quantidade_alunos):
for n in range(4):
    print(f'{n + 1}º Aluno:')
    cadastro_notas = leiaNotas()
    print()
    lista_medias.append(cadastro_notas)


aprovados = contaAprovados(lista_medias)
imprimeTudo(lista_medias, aprovados)
