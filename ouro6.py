from random import randint
tentativa = 6
n_desenho = 0
desenho = ['''
 +---+
 |   |
 |   
 |   
 |
 |
=========\n''','''
 +---+
 |   |
 |   O
 |   
 |
 |
=========\n''','''
 +---+
 |   |
 |   O
 |   |
 |
 |
=========\n''','''
 +---+
 |   |
 |   O
 |   |\ 
 |
 |
=========\n''','''
 +---+
 |   |
 |   O
 |  /|\ 
 |
 |
=========\n''','''
 +---+
 |   |
 |   O
 |  /|\ 
 |  /
 |
=========\n''','''
 +---+
 |   |
 |   O
 |  /|\ 
 |  / \ 
 |
========\n''']

def dificuldade():
    palavras_faceis = ['ovo','ontem','ser','terra','cama','fazer','bolo','chuva','rato','dia','dois','assim','com','ajuda','amor','rosa','carro','copo','lama','passe','voz','texto','ouro','creme','linha']
    palavras_dificeis = ['portugal','sociedade','grande','escola','palavra','mulher','orgulho','identidade','inimigo','perfil','esperto','chuveiro','alegria','oposto','garrafa','momento','direito','acesso','bonito','estado','procurar','semana','pessoal','correto','quadro']
    opc = '0'
    while opc != '1' or opc != '2':
        opc = input('''Escolha a dificuldade com que pretende jogar:
        1 - Fácil (5 ou menos letras)
        2 - Difícil (6 ou mais letras)
        ''')
        if opc == '1':
            return palavras_faceis
        elif opc == '2':
            return palavras_dificeis
        else:
            print('Opção inválida!')
        
def forca():
    global tentativa, desenho, n_desenho
    if tentativa == 0:
        print('')
    elif tentativa == 1:
        print('Última tentiva')
    else:
        print(f'\nTens {tentativa} tentativas!')
    print(desenho[n_desenho])    
    tentativa -= 1
    n_desenho += 1

def jogar():
    global tentativa, n_desenho
    vitoria = False
    palavras = dificuldade()
    palavra = palavras[randint(0,24)]
    espacos = '_' * len(palavra)
    letras_usadas = ''
    while vitoria == False and tentativa > 0:
        forca()
        print(f'Palavra: {espacos}')
        print(f'Letras usadas: {letras_usadas}')
        print('Se quiseres podes tentar adivinhar a palavra (Se acertares ganhas, mas se falhares perdes logo!)')
        letra = input('Letra: ').lower()
        if len(letra) > 1:
            if letra == palavra:
                print('O teu palpite está certo!')
                vitoria = True
                break
            else:
                print('Falhaste! Pensa melhor antes de arriscares tudo.')
                break
        elif not letra in letras_usadas:
            if letra in palavra:
                espacos_lista = list(espacos)
                for i in range(len(palavra)):
                    if palavra[i] == letra:
                        espacos_lista[i] = letra
                        espacos = ''.join(espacos_lista)
                n_desenho -= 1
                tentativa += 1
            else:
                print(f'A letra {letra.upper()} não está na palavra.')
            letras_usadas = letras_usadas + f'{letra} , '
        else:
            print(f'Já tentaste a letra {letra.upper()}. Esta jogada não contou como uma tentativa.')
            tentativa += 1   
            n_desenho -= 1
        if espacos == palavra:
            vitoria = True
    if vitoria == True:
        print(f'Parabéns, acertou a palavra - {palavra} !')
    else:
        forca()
        print(f'Não conseguiste adivinhar a palavra. Para a próxima corre melhor!')
    continuar = input('''Gostaria de jogar de novo?
    1 - Sim
    2 - Não
    ''')
    return continuar

def menu():
    global tentativa,n_desenho
    opc =  input('''Bem-vindo/a ao Jogo da Forca!
    1 - Iniciar
    2 - Sair
    ''')
    while opc != '1' and opc != '2':
        print('\nOpção inválida.')
        menu()
    if opc == '1':
        continuar = jogar()
        while continuar == '1':
            tentativa = 6
            n_desenho = 0
            continuar = jogar()
        print('Adeus!')
    else:
        print('Adeus!')
menu()