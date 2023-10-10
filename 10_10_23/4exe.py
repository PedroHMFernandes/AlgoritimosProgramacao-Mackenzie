# 4. Considere o problema de conversão de temperatura:
# C = (F - 32) / 1.8
# F = C * 1.8 + 32
# Escreva um programa modularizado que permite ao usuário converter uma faixa de temperatura de
# Fahrenheit para Celsius(para isso o usuário deve digitar F) e de Celsius para Fahrenheit (neste caso o usuário
# deve digitar C).
# Para a construção do programa você deve escrever as seguintes funções:
# • exibeMsg() - apenas exibe uma mensagem para ao usuário dizendo o que o programa faz e
# informando como deve ser a entrada de dados. Não tem parâmetro de entrada e não tem
# retorno;
# • verificaOpcao() - a função não tem parâmetro de entrada e retorna “F” ou “C” (fazer a validação
# para que o usuário só digite F ou C);
# • verificaIntervalo() - a função não tem parâmetro de entrada e retorna os valores inicial e final
# do intervalo (fazer a validação para que o valor inicial seja menor que o valor final);
# • exibeFahrenheitToCelsius(inicio, fim) – essa função recebe como entrada o intervalo de
# temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida
# para Celsius;
# • exibeCelsiusToFahrenheit(inicio, fim) – essa função recebe como entrada o intervalo de
# temperatura a ser exibido, faz a conve

def exibMsg():
    print('Este programa permite ao usuário converter uma faixa de temperatura de Fahrenheit para Celsius (o usuário deve digitar F)')
    print('e de Celsius para Fahrenheit (O usuário deve digitar C).')
    print('F - Fahrenheit para Celsius\nC - Celsius para Fahrenheit')

def verificaOpcao():
    opcao = input('Digite C ou F:')[0].upper()
    while opcao not in 'FC':
        print('Opção inválida!')
        opcao = input('Digite C ou F:')[0].upper()
    return opcao

def verificaIntervalo():
    inicio = int(input('Digite o início do intervalo: '))
    fim = int(input('Digite o fim do intervalo: '))
    while inicio >= fim:
        print('O início deve ser menor que o fim!')
        inicio = int(input('Digite o início do intervalo: '))    
        fim = int(input('Digite o fim do intervalo: '))
    return(inicio, fim)

def exibeFahrenheitToCelsius(inicio, fim):
    for temp in range(inicio, fim + 1):
        Celsius = (temp - 32)/1.8
        print(f'{temp:.1f}°F = {Celsius:.1f}°C')

def exibCelsiusToFahrenheit(inicio, fim):
    for temp in range(inicio, fim + 1):
        Fahrenheit = temp * 1.8 + 32
        print(f'{temp:.1f}°C = {Fahrenheit:.1f}°F')

exibMsg()
opcao = verificaOpcao()
inicio, fim = verificaIntervalo()
if opcao == 'C':
    exibCelsiusToFahrenheit(inicio, fim)
elif opcao =='F':
    exibeFahrenheitToCelsius(inicio, fim)

