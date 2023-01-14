import math


def calcular():
    opcao = input('''Gostaria de calcular uma área de uma figura ou o volume de um sólido?
F para Figura
S para Sólido
-> ''')

    if opcao == 'S':
        calc_volume()

    elif opcao == 'F':
        calc_area()

    else:
        print("Não foi introduzida uma opção válida. Tente novamente.")
        calcular()


def calc_volume():
    solido = input('''De qual sólido gostaria de calcular o volume?
C para Cubo
P para Paralelepípedo
PR para Prisma
PIR para Pirâmide
CO para Cone
CI para Cilindro
E para Esfera
-> ''')

    if solido == 'C':
        l = int(input("Introduza a medida do lado do cubo:"))
        print(l**2)

    elif solido == 'P':
        l1 = int(input("Introduza a medida do comprimento do paralelepípedo:"))
        l2 = int(input("Introduza a medida da largura do paralelepípedo:"))
        l3 = int(input("Introduza a medida da altura do paralelepípedo:"))
        print(l1 * l2 * l3)

    elif solido == 'PR':
        ab = int(input("Introduza a medida da área da base do prisma:"))
        h = int(input("Introduza a medida da altura do prisma:"))
        print(ab * h)

    elif solido == 'PIR':
        ab = int(input("Introduza a medida da área da base da pirâmide:"))
        h = int(input("Introduza a medida da altura da pirâmide:"))
        print((ab * h) / 3)

    elif solido == 'CO':
        ab = int(input("Introduza a medida da área da base do cone:"))
        h = int(input("Introduza a medida da altura do cone:"))
        print((ab * h) / 3)

    elif solido == 'CI':
        ab = int(input("Introduza a medida da área da base do cilindro:"))
        h = int(input("Introduza a medida da altura do cilindro"))
        print(ab * h)

    elif solido == 'E':
        r = int(input("Introduza a medida do raio da esfera:"))
        print((4 * (math.pi * (r**3))) / 3)
    else:
        print("Não foi introduzida uma opção válida. Tente novamente.")
        calc_volume()

    again()


def calc_area():
    figura = input('''De qual figura gostaria de calcular a área?
T para Triângulo 
C para Circunferência
Q para Quadrado
R para retângulo
TP para trapézio
-> ''')

    if figura == 'T':
        b = int(input("Introduza a medida da base do triângulo:"))
        h = int(input("Introduza a medida da altura do triângulo:"))
        print((b * h) / 2)

    elif figura == 'C':
        r = int(input("Introduza a medida do raio da circunferência:"))
        print(math.pi * (r**2))

    elif figura == 'Q':
        l = int(input("Introduza a medida do lado do quadrado:"))
        print(l**2)

    elif figura == 'R':
        l = int(input("Introduza a medida da largura do retângulo:"))
        c = int(input("Introduza a medida do comprimento do retângulo"))
        print(c * l)

    elif figura == 'TP':
        b1 = int(input("Introduza a medida da base menor do trapésio:"))
        b2 = int(input("Introduza a medida da base maior do trapésio:"))
        h = int(input("Introduza a medida da altura do trapésio:"))
        print(((b1 + b2) / 2) * h)

    else:
        print("Não foi introduzida uma opção válida. Tente novamente.")
        calc_area()

    again()


def again():
    calc_again = input('''
Gostaria de calcular de novo?
Introduz S para Sim ou N para Não.
-> ''')

    if calc_again == 'S':
        calcular()
    elif calc_again == 'N':
        print('Adeus!')
        quit()
    else:
        again()