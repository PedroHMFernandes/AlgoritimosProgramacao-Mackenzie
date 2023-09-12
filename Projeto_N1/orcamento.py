import os


limites_cadastrados = False
tudo_cadastrado = False
a_cadastrado = False
t_cadastrado = False
m_cadastrado = False
s_cadastrado = False
e_cadastrado = False
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'


def excedeu(limite, despesa):
    if limite < despesa:
        return f'{vermelho}EXCEDIDO em R${(despesa - limite):,.2f}){branco}'
    else:
        return f'{verde}NÃO EXCEDIDO{branco}'


while True:
    # MENU
    print('SISTEMA DE CONTROLE DE ORÇAMENTO - ESCOLHA UMA OPÇÃO\n')
    print('\t(1) CADASTRAR CATEGORIAS E LIMITES')
    print('\t(2) CADASTRAR DESPESA DIÁRIA')
    print('\t(3) EXIBIR RESUMO E ESTATÍSTICAS')
    print('\t(4) FINALIZAR PROGRAMA\n')

    opcao_menu = int(input('SUA OPÇÃO: '))
    print()
    while opcao_menu not in (1, 2, 3, 4):
        print(f'{vermelho}ERRO! Opção inválida, tente novamente:{branco}')
        opcao_menu = int(input('SUA OPÇÃO: '))
    os.system('cls')

    # CADASTRAR CATEGORIAS E LIMITES
    if opcao_menu == 1:
        if limites_cadastrados == False:
            while True:
                print('SISTEMA DE CONTROLE DE ORÇAMENTO - CATEGORIAS E LIMITES\n')
                print('INFORME O LIMITE DE GASTOS PARA AS CATEGORIAS:')
                limite_alimentos = float(input('ALIMENTOS - R$ '))
                limite_transporte = float(input('TRANSPORTE - R$ '))
                limite_moradia = float(input('MORADIA - R$ '))
                limite_saude = float(input('SAÚDE - R$ '))
                limite_entretenimento = float(input('ENTRETENIMENTO - R$ '))
                print()
                confirmacao = input('CONFIRMAR?\n[S]im/[R]efazer: ')[0].upper()
                while confirmacao not in 'SR':
                    print(
                        f'{vermelho}ERRO! Opção inválida, tente novamente:{branco}')
                    confirmacao = input('[S]im/[R]efazer: ')[0].upper()
                if confirmacao == 'S':
                    limites_cadastrados = True
                    os.system('cls')
                    break
                else:
                    pass
                print()
        else:
            print(f'{vermelho}OS LIMITES JÁ FORAM CADASTRADOS!{branco}\n')

    # CADASTRAR DESPESA DIÁRIA
    elif opcao_menu == 2:
        while True:
            if limites_cadastrados == True:
                print(
                    'SISTEMA DE CONTROLE DE ORÇAMENTO - DESPESA DIÁRIA\n')
                print(
                    f'\t{verde}(A) ALIMENTO - R${despesa_alimentos:,.2f}{branco}' if a_cadastrado else '\t(A) ALIMENTO')
                print(
                    f'{verde}\t(T) TRANSPORTE - R${despesa_transporte:,.2f}{branco}' if t_cadastrado else '\t(T) TRANSPORTE')
                print(
                    f'{verde}\t(M) MORADIA - R${despesa_moradia:,.2f}{branco}' if m_cadastrado else '\t(M) MORADIA')
                print(
                    f'{verde}\t(S) SAÚDE - R${despesa_saude:,.2f}{branco}' if s_cadastrado else '\t(S) SAÚDE')
                print(
                    f'{verde}\t(E) ENTRETENIMENTO - R${despesa_entretenimento:,.2f}{branco}\n' if e_cadastrado else '\t(E) ENTRETENIMENTO\n')
                categoria = input('INFORME A CATEGORIA: ')[0].upper()

                while categoria not in 'ATMSE':
                    print(
                        f'{vermelho}Categoria INVÁLIDA tente novamente.{branco}\n')
                    categoria = input('INFORME A CATEGORIA: ')[0].upper()
                print()

                if categoria == 'A':
                    print(f'CATEGORIA: {verde}A - ALIMENTO{branco}')
                    despesa_alimentos = float(input('INFORME O VALOR: R$'))
                    status_alimentos = excedeu(
                        limite_alimentos, despesa_alimentos)
                    a_cadastrado = True
                elif categoria == 'T':
                    print(f'CATEGORIA: {verde}T - TRANSPORTE{branco}')
                    despesa_transporte = float(input('INFORME O VALOR: R$'))
                    status_transporte = excedeu(
                        limite_transporte, despesa_transporte)
                    t_cadastrado = True
                elif categoria == 'M':
                    print(f'CATEGORIA: {verde}M - MORADIA{branco}')
                    despesa_moradia = float(input('INFORME O VALOR: R$'))
                    status_moradia = excedeu(limite_moradia, despesa_moradia)
                    m_cadastrado = True
                elif categoria == 'S':
                    print(f'CATEGORIA: {verde}S - SAÚDE{branco}')
                    despesa_saude = float(input('INFORME O VALOR: R$'))
                    status_saude = excedeu(limite_saude, despesa_saude)
                    s_cadastrado = True
                elif categoria == 'E':
                    print(f'CATEGORIA: {verde}E - ENTRETENIMENTO{branco}')
                    despesa_entretenimento = float(
                        input('INFORME O VALOR: R$'))
                    status_entretenimento = excedeu(
                        limite_entretenimento, despesa_entretenimento)
                    e_cadastrado = True

                if a_cadastrado and t_cadastrado and m_cadastrado and s_cadastrado and e_cadastrado:
                    tudo_cadastrado = True

                    gasto_total = despesa_alimentos + despesa_transporte + \
                        despesa_moradia + despesa_saude + despesa_entretenimento

                    limite_total = limite_alimentos + limite_transporte + \
                        limite_moradia + limite_saude + limite_entretenimento

                    porcentagem_de_despesa = (gasto_total / limite_total) * 100

                print('\nDIGITE:')
                print('<N> PARA NOVA CATEGORIA')
                print('<M> PARA VOLTAR PARA O MENU')
                print('<V> PARA VIZUALIZAR DESPESAS')
                opcao_despesa = input('SUA OPÇÃO: ').upper()
                while opcao_despesa not in 'NMV':
                    print(
                        f'{vermelho}ERRO! Opção inválida, tente novamente:{branco}')
                    opcao_despesa = input('SUA OPÇÃO: ').upper()
                os.system('cls')
                if opcao_despesa == 'V':
                    os.system('cls')
                    print(
                        f'\t{verde}(A) ALIMENTO - R${despesa_alimentos:,.2f}{branco}' if a_cadastrado else '\t(A) ALIMENTO - R$0,00')
                    print(
                        f'{verde}\t(T) TRANSPORTE - R${despesa_transporte:,.2f}{branco}' if t_cadastrado else '\t(T) TRANSPORTE - R$0,00')
                    print(
                        f'{verde}\t(M) MORADIA - R${despesa_moradia:,.2f}{branco}' if m_cadastrado else '\t(M) MORADIA - R$0,00')
                    print(
                        f'{verde}\t(S) SAÚDE - R${despesa_saude:,.2f}{branco}' if s_cadastrado else '\t(S) SAÚDE - R$0,00')
                    print(
                        f'{verde}\t(E) ENTRETENIMENTO - R${despesa_entretenimento:,.2f}{branco}\n' if e_cadastrado else '\t(E) ENTRETENIMENTO - R$0,00\n')
                    print('DIGITE:')
                    print('<N> PARA NOVA CATEGORIA')
                    print('<M> PARA VOLTAR PARA O MENU')
                    opcao_despesa = input('SUA OPÇÃO: ').upper()
                    while opcao_despesa not in 'NM':
                        print(
                            f'{vermelho}ERRO! Opção inválida, tente novamente:{branco}')
                        opcao_despesa = input('SUA OPÇÃO: ').upper()
                    os.system('cls')
                if opcao_despesa == 'M':
                    break
            else:
                print(
                    f'{vermelho}POR FAVOR, FAÇA O CADASTRO DOS LIMITES PRIMEIRO{branco}\n')
                break

    # EXIBIR RESUMO E ESTATÍSTICAS
    elif opcao_menu == 3:
        if tudo_cadastrado:
            print('SISTEMA DE CONTROLE DE ORÇAMENTO - RESUMO E ESTATÍSTICAS\n')
            print(
                f'TOTAL GASTO EM ALIMENTOS - R$ {despesa_alimentos:,.2f} - LIMITE DE R$ {limite_alimentos:,.2f} {status_alimentos}')
            print(
                f'TOTAL GASTO EM TRANSPORTE - R$ {despesa_transporte:,.2f} - LIMITE DE R$ {limite_transporte:,.2f} {status_transporte}')
            print(
                f'TOTAL GASTO EM MORADIA - R$ {despesa_moradia:,.2f} - LIMITE DE R$ {limite_moradia:,.2f} {status_moradia}')
            print(
                f'TOTAL GASTO EM SAÚDE - R$ {despesa_saude:,.2f} - LIMITE DE R$ {limite_saude:,.2f} {status_saude}')
            print(
                f'TOTAL GASTO EM ENTRETENIMENTO - R$ {despesa_entretenimento:,.2f} - LIMITE DE R$ {limite_entretenimento:,.2f} {status_entretenimento}')
            print(
                f'GASTO TOTAL: R${vermelho}{gasto_total:,.2f}{branco}')
            print(
                f'LIMITE TOTAL DETERMINADO: R${amarelo}{limite_total:,.2f}{branco}')
            print(
                f'RELAÇÃO DESPESA: {ciano}{porcentagem_de_despesa:,.2f}%{branco} DO LIMITE ESTABELECIDO')
        else:
            print(f'{vermelho}ATENÇÃO:{branco}')
            if not a_cadastrado:
                print('Falta cadastrar: (A) ALIMENTO')
            if not t_cadastrado:
                print('Falta cadastrar: (T) TRANSPORTE')
            if not m_cadastrado:
                print('Falta cadastrar: (M) MORADIA')
            if not s_cadastrado:
                print('Falta cadastrar: (S) SAÚDE')
            if not e_cadastrado:
                print('Falta cadastrar: (E) ENTRETENIMENTO')
        print()
    # FINALIZAR PROGRAMA
    elif opcao_menu == 4:
        print('Este programa foi desenvolvido por:')
        print('Pedro Henrique Mansano Fernandes - 42303885')
        print()
        break
