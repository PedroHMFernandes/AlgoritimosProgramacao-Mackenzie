# 1. Registro de Despesas: o programa deve permitir que o usuário insira despesas diárias
# referentes à um período específico, até que ele decida parar de registrar.
# 2. Categorias de Despesas: Cada despesa deve estar associada a uma categoria. As
# categorias são <A> para alimentos, <T> para transporte, <M>< para moradia, <S> para
# saúde e <E> para entretenimento.
# 3. Valor: Para cada despesa, o usuário deve fornecer o seu valor da despesa e a sua
# categoria.
# 4. Limite de Orçamento: O programa deve permitir que o usuário defina um limite de
# orçamento para cada categoria de despesa.
# 5. Resumo das Despesas: Após o registro das despesas, o programa deve fornecer um
# resumo que inclua:
# a. O total gasto em cada categoria - o programa deve indicar se o limite foi
# ultrapassado ou não.
# b. Estatísticas Adicionais – Além do resumo, o programa deve calcular e exibir
# alguma estatística adicional (a critério do grupo)
# 6. Opções do Usuário: O programa deve oferecer opções ao usuário, como cadastrar
# categorias e limites, registrar uma nova despesa, visualizar o resumo das despesas ou
# encerrar o programa (menu principal)
# 7. Validação de Dados: Certifique-se de que o programa valide os dados inseridos pelo
# usuário, como valores numéricos positivos e validação da categoria.

while True:
    print('SISTEMA DE CONTROLE DE ORÇAMENTO - ESCOLHA UMA OPÇÃO\n')
    print('\t(1) CADASTRAR CATEGORIAS E LIMITES')
    print('\t(2) CADASTRAR DESPESA DIÁRIA')
    print('\t(3) EXIBIR RESUMO E ESTATÍSTICAS')
    print('\t(4) FINALIZAR PROGRAMA\n')
    opcao = int(input('SUA OPÇÃO: '))

    if opcao == 1:
        print('SISTEMA DE CONTROLE DE ORÇAMENTO - CATEGORIAS E LIMITES')
        print('INFORME O LIMITE DE GASTOS PARA AS CATEGORIAS:')
        limite_alimentos = float(input('ALIMENTOS - R$ '))
        limite_transporte = float(input('TRANSPORTE - R$ '))
        limite_moradia = float(input('MORADIA - R$ '))
        limite_saude = float(input('SAÚDE - R$ '))
        limite_entretenimento = float(input('ENTRETENIMENTO - R$ '))
    elif opcao == 2:
        print('SISTEMA DE CONTROLE DE ORÇAMENTO - DESPESA DIÁRIA')
        categoria = input('INFORME A CATEGORIA: ')
        if categoria == 'A':
            despesa_alimentos = float(input('INFORME O VALOR: R$')) 
        elif categoria == 'T':
            despesa_transporte = float(input('INFORME O VALOR: R$'))
        elif categoria == 'M':
            despesa_moradia = float(input('INFORME O VALOR: R$'))
        elif categoria == 'S':
            despesa_saude = float(input('INFORME O VALOR: R$'))
        elif categoria == 'E':
            despesa_entretenimento = float(input('INFORME O VALOR: R$'))
        else:
            print('Categoria INVÁLIDA tente novamente.')
    elif opcao == 3:
        ...
    elif opcao == 4:
        break
    else:
        print('Opção INVÁLIDA tente novamente.')