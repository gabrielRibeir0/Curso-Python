def novo_supermercado():
    pass

def novo_produto():
    pass

def alterar_qtd():
    pass

def mostrar_qtd():
    pass

def mostrar_supermercado():
    pass

def menu():
    opc = input('''
    Programa de Gestão Supermercados Adelino
    Bem-vindo Senhor Adelino! O que deseja fazer?
    1 - Adicionar um novo supermercado
    2 - Adicionar um novo produto
    3 - Alterar a quantidade de algum produto
    4 - Imprimir a quantidade dos produtos dispníveis em um supermercado
    5 - Imprimir a lista de supermercados nos quais um produto está disponível
    6 - Sair
    ''')
    if opc == '1':
        pass
    elif opc == '2':
        pass
    elif opc == '3':
        pass
    elif opc == '4':
        pass
    elif opc == '5':
        pass
    elif opc == '6':
        print('De certeza que pretende sair do programa!')
    else:
        print('Opção inválida, senhor Adelino!')
        menu()

def continuar():
    opc = input('''
    Gostaria de fazer mais alguma coisa?
    1 - Sim
    2 - Não''')
    if opc == '1':
        return 0
    elif opc == '2':
        print('Até à próxima!')
        return -1
    else:
        print('Opção inválida!')
        continuar()

menu()
continuar =  0
while continuar != -1:
    menu()
    continuar = continuar()