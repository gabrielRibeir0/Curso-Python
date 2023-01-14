from random import randint
jogo = [' ',' ',' ',
' ',' ',' ',
' ',' ',' ']

def mostrarjogo(jogo):
    print(f'''{jogo[0]}|{jogo[1]}|{jogo[2]}
{jogo[3]}|{jogo[4]}|{jogo[5]}
{jogo[6]}|{jogo[7]}|{jogo[8]}
    ''')

def jogada_user(jogo,user):
    jogada = 0
    jog_valida = False
    while (jogada<1 or jogada>9) or not jog_valida:
        jogada = int(input("Indique a casa onde quer jogar (1 - 9):"))
        if (jogada<1 or jogada>9):
            print('Opção inválida!')
        elif jogo[jogada-1] != ' ':
            print("Não podes jogar numa casa já preenchida!")
            jog_valida = False
        else:
            jog_valida = True
    jogo[jogada-1] = user
    return jogo

def verificar_vertical(jogo):
    for casa in range(0,3):
        if jogo[casa] != ' ':
            if jogo[casa+3] == jogo[casa] and jogo[casa+6] == jogo[casa]:
                return True
    return False

def verificar_horizontal(jogo):
    for casa in range(0,7,3):
        if jogo[casa] != ' ':
            if jogo[casa+1] == jogo[casa] and jogo[casa+2] == jogo[casa]:
                return True
    return False

def verificar_diagonal(jogo):
    for casa in range(0,3,2):
        if jogo[casa] != ' ':
            if casa == 0:
                if jogo[casa+4] == jogo[casa] and jogo[casa+8] == jogo[casa]:
                    return True
            else:
                if jogo[casa+2] == jogo[casa] and jogo[casa+4] == jogo[casa]:
                    return True
    return False

def possvit_v(jogo):
    for casa in range(0,3):
        for casa2 in range(casa,casa+4,3):
            if jogo[casa2] != ' ':
                if jogo[casa] == jogo[casa2] or jogo[casa+6] == jogo[casa2]:
                    for x in range(casa,casa+7,3):
                        if jogo[x] == ' ':
                            return x
                        else:
                            return -1
    return -1

def possvit_h(jogo):
    for casa in range(0,7,3):
        for casa2 in range(casa,casa+2):
            if jogo[casa2] != ' ':
                if jogo[casa] == jogo[casa2] or jogo[casa+2] == jogo[casa2]:
                    for x in range(casa,casa+3):
                        if jogo[x] == ' ':
                            return x
                        else:
                            return -1
    return -1

def possvit_d(jogo):
    for casa in range(0,3,2):
        for casa2 in range(casa,5,4-casa):
            if jogo[casa2] != ' ':
                if jogo[casa] == jogo[casa2] or jogo[casa+(2*(4-casa))] == jogo[casa2]:
                    for x in range(casa,2*(4-casa)+1,4-casa):
                        if jogo[x] == ' ':
                            return x
                        else:
                            return -1                  
    return -1

def jogar(jogo):
    vitoria = False
    simbolo = 0
    while simbolo !=1 and simbolo != 2:
        simbolo = int(input('''Escolha se quer joga com as cruzes ("X") ou as bolas ("O")
        1 - Cruzes ("X")
        2 - Bolas ("O") '''))
        if simbolo == 1:
            user = 'X'
            comp = 'O'
        elif simbolo == 2:
            user = 'O'
            comp = 'X'
        else:
            print("Opção inválida!")

    primeiro = randint(0,1)
    if primeiro == 0:
        print('O utiizador joga primeiro!\nRonda 1') 
        jogo = jogada_user(jogo,user)
        mostrarjogo(jogo)
        if jogo[4] == ' ':
            jogo[4] = comp
        else:
            jogo[0] = comp
        mostrarjogo(jogo)
    else:
        print('O computador joga primeiro!\nRonda 1')
        jogo[4] = comp
        mostrarjogo(jogo)
        jogo = jogada_user(jogo,user)
        mostrarjogo(jogo)
    while not vitoria:
        vencedor = 2
        jogou = False
        for n in range(2,6):
            if primeiro == 0:
                if n == 2:
                    print('Ronda 2')
                    jogo = jogada_user(jogo,user)
                    mostrarjogo(jogo) 
                    if jogo[6] == ' ':
                        jogo[6] = comp
                    else:
                        jogo[0] = comp
                    mostrarjogo(jogo)
                elif n == 3:
                    print('Ronda 3')
                    jogo = jogada_user(jogo,user)
                    mostrarjogo(jogo)
                    vitoria = verificar_vertical(jogo) or verificar_horizontal(jogo) or verificar_diagonal(jogo)
                    if vitoria:
                        vencedor = 0
                        break
                    perigo_v = possvit_v(jogo)
                    perigo_h = possvit_h(jogo)
                    perigo_d = possvit_d(jogo)
                    if perigo_v != -1:
                        jogo[perigo_v] = comp
                    elif perigo_h != -1:
                        jogo[perigo_h] = comp
                    elif perigo_d != -1:
                        jogo[perigo_d] = comp
                    else:
                        while not jogou:
                            x = randint(0,8)
                            if jogo[x] == ' ':
                                jogou = True
                                jogo[x] = comp
                            else:
                                jogou = False
                    mostrarjogo(jogo)
                    vitoria = verificar_vertical(jogo) or verificar_horizontal(jogo) or verificar_diagonal(jogo)
                    if vitoria:
                        vencedor = 1
                        break
                elif n == 4:
                    print('Ronda 4')
                    jogo = jogada_user(jogo,user)
                    mostrarjogo(jogo)
                    vitoria = verificar_vertical(jogo) or verificar_horizontal(jogo) or verificar_diagonal(jogo)
                    if vitoria:
                        vencedor = 0
                        break
                    perigo_v = possvit_v(jogo)
                    perigo_h = possvit_h(jogo)
                    perigo_d = possvit_d(jogo)
                    if perigo_v != -1:
                        jogo[perigo_v] = comp
                    elif perigo_h != -1:
                        jogo[perigo_h] = comp
                    elif perigo_d != -1:
                        jogo[perigo_d] = comp
                    else:
                        while not jogou:
                            x = randint(0,8)
                            if jogo[x] == ' ':
                                jogou = True
                                jogo[x] = comp
                            else:
                                jogou = False
                    mostrarjogo(jogo)
                    vitoria = verificar_vertical(jogo) or verificar_horizontal(jogo) or verificar_diagonal(jogo)
                    if vitoria:
                        vencedor = 1
                        break
                else:
                    print('Ronda 5')
                    jogo = jogada_user(jogo,user)
                    mostrarjogo(jogo)
                    vitoria = verificar_vertical(jogo) or verificar_horizontal(jogo) or verificar_diagonal(jogo)
                    if vitoria:
                        vencedor = 0
            else:
                if n ==2:
                    print('Ronda 2')
                    if jogo[0] == ' ':
                        jogo[0] = comp
                    else:
                        jogo[6] = comp
                    mostrarjogo(jogo)
                    jogo = jogada_user(jogo,user)
                    mostrarjogo(jogo)             
                elif n == 3:
                    print('Ronda 3')
                    perigo_v = possvit_v(jogo)
                    perigo_h = possvit_h(jogo)
                    perigo_d = possvit_d(jogo)
                    if perigo_v != -1:
                        jogo[perigo_v] = comp
                    elif perigo_h != -1:
                        jogo[perigo_h] = comp
                    elif perigo_d != -1:
                        jogo[perigo_d] = comp
                    else:
                        while not jogou:
                            x = randint(0,8)
                            if jogo[x] == ' ':
                                jogo[x] = comp
                                jogou = True
                            else:
                                jogou = False
                    mostrarjogo(jogo)
                    vitoria = verificar_vertical(jogo) or verificar_horizontal(jogo) or verificar_diagonal(jogo)
                    if vitoria:
                        vencedor = 1
                        break  
                    jogo = jogada_user(jogo,user)
                    mostrarjogo(jogo)
                    vitoria = verificar_vertical(jogo) or verificar_horizontal(jogo) or verificar_diagonal(jogo)
                    if vitoria:
                        vencedor = 0
                        break  
                elif n == 4:
                    print('Ronda 4')
                    perigo_v = possvit_v(jogo)
                    perigo_h = possvit_h(jogo)
                    perigo_d = possvit_d(jogo)
                    if perigo_v != -1:
                        jogo[perigo_v] = comp
                    elif perigo_h != -1:
                        jogo[perigo_h] = comp
                    elif perigo_d != -1:
                        jogo[perigo_d] = comp
                    else:
                        while not jogou:
                            x = randint(0,8)
                            if jogo[x] == ' ':
                                jogou = True
                                jogo[x] = comp
                            else:
                                jogou = False
                    mostrarjogo(jogo)
                    vitoria = verificar_vertical(jogo) or verificar_horizontal(jogo) or verificar_diagonal(jogo)
                    if vitoria:
                        vencedor = 1
                        break  
                    jogo = jogada_user(jogo,user)
                    mostrarjogo(jogo)
                    vitoria = verificar_vertical(jogo) or verificar_horizontal(jogo) or verificar_diagonal(jogo)
                    if vitoria:
                        vencedor = 0
                        break 
                else:
                    print('Ronda 5')
                    for casa in jogo:
                        if casa == ' ':
                            casa = comp
                    mostrarjogo(jogo)
                    vitoria = verificar_vertical(jogo) or verificar_horizontal(jogo) or verificar_diagonal(jogo)
                    if vitoria:
                        vencedor = 1

                    if primeiro == 0:
                        print('Ronda final')
                        jogo = jogada_user(jogo,user)
                        mostrarjogo(jogo)
                        vitoria = verificar_vertical(jogo) or verificar_horizontal(jogo) or verificar_diagonal(jogo)
                        if vitoria:
                            vencedor = 0
                    else:
                        print('Ronda final')
                        for casa in jogo:
                            if casa == ' ':
                                casa = comp
                        mostrarjogo(jogo)
                        vitoria = verificar_vertical(jogo) or verificar_horizontal(jogo) or verificar_diagonal(jogo)
                        if vitoria:
                            vencedor = 1
    if vencedor == 0:
        print("Parabéns! Ganhaste o Jogo do Galo!")
    elif vencedor == 1:
        print("Perdeste :( Para a próxima corre melhor!")
    else:
        print("Empate! Quase que conseguias ganhar!")

def menu():
    opc = input('''------Jogo do Galo------
    Menu:
    1 - Jogar
    2 - Sair ''')
    if opc == '1':
        jogo = [' ',' ',' ',
' ',' ',' ',
' ',' ',' ']
        jogar(jogo)
        return 0
    elif opc == '2':
        print('Até à próxima!')
        return -1
    else:
        print("Opção inválida!")
        return 0

continuar =  0
while continuar != -1:
    continuar = menu()