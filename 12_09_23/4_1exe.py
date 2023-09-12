# 1) Um hospital precisa de um programa para calcular e imprimir os gastos de um paciente.
# A tabela de preços do hospital é a seguinte
#  Quartos:
#  particular – R$ 360,00
#  semi-particular – R$ 210,00
#  coletivo – R$ 185,00
#  WIFI: R$ 3,00
#  TV a cabo: R$ 4,00
#
#  Escreva um programa que leia:
# - o número de dias gastos no hospital;
# - o tipo de quarto;
# - se usou ou não o WIFI (Sim ou Nao);
# - se usou ou não a TV a cabo (Sim ou Nao).
# Ao final, emita um relatório, como o exemplo, a seguir:
# Número de dias no hospital: 5
# Tipo de quarto: ........................... Particular
# Diárias: ................................. 1800,00
# WIFI: ................................... 3,00
# TV a cabo: ............................ 4,00
# Total: ............................ 1807,00

dias = int(input('Número de dias no hospital: '))

print('Tipos de quartos:')
print('  (1) Particular') 
print('  (2) Semi-Particular') 
print('  (3) Coletivo') 
opcao_quarto = int(input('Opção: '))
while opcao_quarto != 1 and opcao_quarto!= 2 and opcao_quarto!=3:
    print('Opção inválida, tente novamente.')
    opcao_quarto = int(input('Opção: '))
if opcao_quarto == 1:
    quarto ='Particular'
    diaria = 360
elif opcao_quarto == 2:
    quarto ='Semi-Particular'
    diaria = 210
else:
    quarto ='Coletivo'
    diaria = 185

diaria *= dias

wifi_uso = input('Usou WIFI[S/N]? ')[0].upper()
wifi_preco = 0
if wifi_uso == 'S':
    wifi_preco = 3

tv_cabo_uso = input('Usou TV a cabo[S/N]? ')[0].upper()
tv_cabo_preco = 0
if tv_cabo_uso == 'S':
    tv_cabo_preco = 4

total = diaria + wifi_preco + tv_cabo_preco

print(f'Número de dias no hospital: {dias}')
print(f'Diárias: {diaria:,.2f}')
print(f'WIFI: {wifi_preco:,.2f}')
print(f'TV a cabo: {tv_cabo_preco:,.2f}')
print(f'Total: {total:,.2f}')