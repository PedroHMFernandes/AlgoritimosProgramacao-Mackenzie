# 2) Elabore um programa que mostre o preço de etiqueta de um produto e calcule e mostre o quanto
# deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de
# pagamento.
# Utilize os códigos da tabela seguinte para ler qual a condição de pagamento escolhida e efetuar o cálculo
# adequado
# Código Condições de pagamento
# 1 À vista em dinheiro ou cheque, recebe 10% de desconto
# 2 À vista no cartão de crédito, recebe 5% de desconto
# 3 Em 2 vezes, preço normal de etiqueta sem juros
# 4 Em 3 vezes, preço normal de etiqueta mais juros de 10%

preco = float(input('Preço da etiqueta: '))
print('(1) À vista em dinheiro ou cheque, recebe 10% de desconto')
print('(2) À vista no cartão de crédito, recebe 5% de desconto')
print('(3) Em 2 vezes, preço normal de etiqueta sem juros')
print('(4) Em 3 vezes, preço normal de etiqueta mais juros de 10%')

opcao = int(input('Sua opção: '))
while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
    print('Opção inválida, tente novamente.')
    opcao = int(input('Sua opção: '))

if opcao == 1:
   total = preco * 0.9 
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco 
else:
    total = preco * 1.10

print(f'O preço total da etique é R${total:,.2f}')