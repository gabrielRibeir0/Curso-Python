from random import randint, random

dias = ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira']
carne = ['Strogonoff', 'Massa a Bolonhesa', 'Massa Almondegas','Bifes de Frango','Hamburger','Pizza','Coisas do Lidl','Massa Broculos','Assado Carne','']
peixe = ['Douradinhos','Massa Atum','Assado Peixe',]
ementa_atual = ['']
ementa_passada = ['']
ementa_passada2 = ['']

def verificar(lista, prato):
    for i in range(len(lista)):
        if prato.lower() == lista[i].lower():
            return True
    return False
    
def adicionar():
    novo = input('Novo prato: ')
    opc = input('''1 - Prato de Carne
    2 - Prato de Peixe''')
    if opc == '1':
        if verificar(carne, novo):
            print('Prato já existente')
        else:
            carne.append(novo)
            print('Adicionado!')
    elif opc == '2':
        if verificar(carne, novo):
            print('Prato já existente')
        else:
            peixe.append(novo)
            print('Adicionado!')
    else:
        adicionar()

def remover():
    alvo = input('Prato a remover: ')
    opc = input('''1 - Prato de Carne
    2 - Prato de Peixe''')
    if opc == '1':
        if verificar(carne, alvo):
            for i in range(len(carne)):
                if alvo.lower() == carne[i].lower():
                    carne.pop(i)
                    print('Removido!')
                    break
        else:
            print('Prato não existente')
    elif opc == '2':
        if verificar(peixe, alvo):
            for i in range(len(peixe)):
                if alvo.lower() == peixe[i].lower():
                    peixe.pop(i)
                    print('Removido!')
                    break
        else:
            print('Prato não existente')
    else:
        remover()

def gerir():
    opc = input('''1 - Adicionar pratos
    2 - Remover pratos''')
    if opc == '1':
        adicionar()
    elif opc == '2':
        remover()
    else:
        gerir()

def mostrar_pratos():
    print('Pratos de Carne')
    for i in range(len(carne)):
        print(carne[i])
    print('''
    Pratos de Peixe''')
    for i in range(len(peixe)):
        print(peixe[i])
    input('')

def pratos():
    opc = input('''1 - Mostrar pratos por carne/peixe
    2 - Gerir pratos''')
    if opc == '1':
        mostrar_pratos()
    elif opc == '2':
        gerir()
    else:
        pratos()

def gerador():
    ementa_passada2 = ementa_passada
    ementa_passada = ementa_atual
    ementa_atual.clear()
    ind = random()       ## 0 - carne           1 - peixe
    for i in range(5):
        j = True
        if ind == 0:
            ind = 1
            while j:
                prato = carne[randint(0,len(carne) - 1)]
                if  prato not in ementa_passada and prato not in ementa_passada2:
                    ementa_atual[i] = prato
                    j = False
                else:
                    print('''Prato presente nas 2 últimas semanas!
                    ''')
        else:
            ind = 0
            while j:
                prato = peixe[randint(0,len(peixe) - 1)]
                if  prato not in ementa_passada and prato not in ementa_passada2:
                    ementa_atual[i] = prato
                    j = False
                else:
                    print('''Prato presente nas 2 últimas semanas!
                    ''')
    for i in range(len(ementa_atual)):
        print(f'{dias[i]} - {ementa_atual[i]}')

def ver():
    for i in range(len(ementa_atual)):
        print(f'{dias[i]} - {ementa_atual[i]}')
    input('')

def menu():
    opc = input('''
    1 - Gerar ementa para a semana
    2 - Ver pratos guardados
    3 - Ver ementa atual
    4 - Sair
    ''')
    if opc == '1':
        gerador()
    elif opc == '2':
        pratos()
    elif opc == '3':
        ver()
    elif opc == '4':
        pass
    else:
        menu()

menu()  