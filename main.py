'''
Constroi um programa que escreve permite ao utlizador fazer o seguinte:
* Adicionar coisas à lista de compras guardada em compras.txt
* Verificar se um certo elemento está na lista de compras, e se sim, dizer que quantidade.

Repara que no ficheiro os produtos devem ser guardados como:
[produto] [quantidade]
'''
def adicionar():
  with open('compras.txt','a') as compras:
    prod = input('Introduza o produto: ')
    with open('compras.txt','r') as lista:
      l_compras = lista.readlines()
      for i in l_compras:
        produto = i.split(' ')
        if produto[0] == prod:
          print(f'Já tens este produto na lista.')
          return None
    qtd = input('Introduza a quantidade desse produto: ')
    compras.write(f'{prod} {qtd}\n')

def verificar():
  encontrado = False
  with open('compras.txt','r') as compras:
    prod = input('Introduza o produto que gostaria de verificar: ')
    l_compras = compras.readlines()
    for i in l_compras:
      produto = i.split(' ')
      if produto[0] == prod:
        print(f'Precisas de {produto[1]} {produto[0]}')
        encontrado = True
    if not encontrado:
      print('Esse produto não está na tua lista de compras.')

def main():
  opc = input('''Escolha a operação que pretende realizar:
              1 - Adicionar novo produto à lista
              2 - Verificar se um produto está na lista
              3 - Sair
              ''')
  if opc == '1':
    adicionar()
  elif opc == '2':
    verificar()
  elif opc == '3':
    print('Adeus!')
    return -1
  else:
    print('Opção inválida!')
    main()

continuar = 0 
while continuar != -1:
  continuar = main()