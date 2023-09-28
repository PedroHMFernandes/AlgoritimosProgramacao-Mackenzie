# 6) Uma empresa deseja reajustar o salário de seus empregados conforme a seguinte tabela:
#                        Salário                                                         Acréscimo
#               superior ou igual a 3.000,00                                                 8%
#               inferior a 3.000,00 mas superior ou igual a 2.000,00                        10%
#               inferior a 2.000,00                                                         12%
# Para cada empregado serão digitados o nome do empregado e salário.
# Elabore um programa que leia a quantidade de empregados e em seguida o conjunto de dados
# de cada empregado – nome e salário. Calcule e mostre:
# a) para cada empregado, o salário reajustado (conforme tabela);
# b) a quantidade de empregados que receberam reajuste de 10%;
# c) o salário médio (após o reajuste) entre os empregados;

empregados = []
cont_10 = 0
media = 0
media_reajuste = 0

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
    pessoa_cadastrada = {'nome': nome, 'salario': salario,
                         'salario_acrescido': salario_acrescido}
    empregados.append(pessoa_cadastrada)

print()
for pessoa in empregados:
    print(
        f'{pessoa["nome"]} - Salario: R${pessoa["salario"]:.2f}\nReajustado: R${pessoa["salario_acrescido"]:.2f} ')
    media += pessoa['salario']/len(empregados)
    media_reajuste += pessoa['salario_acrescido']/len(empregados)
print()
print(f'Média antes do reajuste: R${media:.2f}')
print(f'Média após reajuste: R${media_reajuste:.2f}')
print(f'Quantidades de 10% de reajuste: {cont_10}')
