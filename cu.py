cont_10 = 0
media = 0

quantidade_a_cadastrar = int(input('Quantidade de funcionários a cadastrar: '))
for cadastro in range(quantidade_a_cadastrar):
    nome = input('Nome: ').title()
    salario = float(input('Salário: R$'))
    if salario < 2000:
        salario_acrescido = salario * 1.12
    elif salario < 3000:
        salario_acrescido = salario * 1.10
        cont_10 += 1
    else:
        salario_acrescido = salario * 1.08
    media += salario_acrescido/quantidade_a_cadastrar
    print(f'{nome} - R${salario_acrescido}')
print(f'{media=}')
print(f'{cont_10=}')
