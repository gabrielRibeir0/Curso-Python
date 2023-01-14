""" 
Este é o código que sobrou depois do problema com o espião...

O código tem 3 listas fundamentais. O propósito de cada uma é auto-explicativo. A lista_pass tem uma password já encriptada.

Começa a implementação do programa dentro da função "programa" e depois do if que já estava escrito. O programa já recolhe a resposta do utilizador. O código que trata da opção 6 não foi eliminado pelo espião, por isso não te preocupes com essa opção.

Podes definir todas as variáveis e funções auxiliares que quiseres abaixo da linha compreendida para esse efeito.

Dá uma vista de olhos no código já escrito antes de começar. Boa sorte!

IMPORTANTE:
Usa tabs em vez de espaços na indentação, caso contrário terás um "IndentationError
- Vai a Settings -> Indent type e muda para tabs
- Usa a tecla "tab" quando queres indentar

"""

lista_users = ["John the spy"]
lista_emails = ["Johnspy@treetree2.school"]
lista_pass = ["drowssap"]
removidos = []

def registar(lista_users, lista_emails, lista_pass):
  nome = input('Nome: ')
  idade = int(input('Idade: '))
  email = input('E-mail: ')
  if idade < 18 or email[-17:] != '@treetree2.school' or ' ' in email:
    print('Não se pode registar!')
  else:
    print('A sua password padrão: treetree')
    lista_users.append(nome)
    lista_emails.append(email)
    lista_pass.append('eerteert')

def password(lista_emails,lista_pass):
  email = input('Primeiro, introduza o seu email: ')
  password = input('Intoduza a sua password atual: ')
  if email in lista_emails and password[::-1] in lista_pass and lista_emails.index(email) == lista_pass.index(password[::-1]):
    novapassword = input((f'''A sua password atual é {password}
    Password nova: '''))
    if ('@' in novapassword or '#' in novapassword or '?' in novapassword or '!' in novapassword) and (8<=len(novapassword)<=20): 
      del lista_pass[lista_pass.index(password[::-1])]
      lista_pass.append(novapassword[::-1])
    else:
      print('Password inválida.')
  else:
    print('Verificação fracassada.')
       
def login(lista_users,lista_emails, lista_pass):
  email = input('E-mail: ')
  password = input('Password: ')
  if email in lista_emails and password[::-1] in lista_pass and lista_emails.index(email) == lista_pass.index(password[::-1]):
    print(f'Bem-vindo/a ao ASOBOOK {lista_users[lista_emails.index(email)]}!')
  else:
    print('E-mail ou password errados.')

def eliminar(lista_users,lista_emails,lista_pass, removidos):
  ver = input('Tem certeza que quer eliminar a sua conta (S/N)? ')
  if ver == 'S' or ver == 's':
    email = input('Introduza os seus dados de acesso.\nE-mail: ')
    password = input('Password: ')
    if email in lista_emails and password[::-1] in lista_pass and lista_emails.index(email) == lista_pass.index(password[::-1]):
      print('Lamentamos vê-lo partir. Até à próxima!')
      removidos.append(lista_users[lista_emails.index(email)])
      del lista_users[lista_emails.index(email)]
      del lista_emails[lista_emails.index(email)]
      del lista_pass[lista_pass.index(password[::-1])]
    else:
      print('Dados de acesso errados!')
  elif ver == 'N' or ver == 'n':
    print('Ainda bem que quer continuar connosco!')
  else:
    print('Opção inválida')

def stats(lista_users,removidos):
  sort_users = sorted(lista_users)
  sort_removidos = sorted(removidos)
  print(f'Número de utilizadores do ASOBOOK: {len(lista_users)}\nUtilizadores: {sort_users}')
  print(f'Número de contas eliminadas: {len(removidos)}\nUtilizadores removidos: {sort_removidos}')

def programa():
  print(""" ---- Gestor de utilizadores ----
  1 - Registar utilizador 
  2 - Definir password 
  3 - Login no ASOBOOK 
  4 - Eliminar conta no ASOBOOK
  5 - Estatística
  6 - Sair 
  """)

  escolha = int(input())
  if escolha == 1:
    registar(lista_users,lista_emails,lista_pass)
  elif escolha == 2:
    password(lista_emails, lista_pass)
  elif escolha == 3:
    login(lista_users,lista_emails,lista_pass)
  elif escolha == 4:
    eliminar(lista_users,lista_emails,lista_pass,removidos)
  elif escolha == 5:
    stats(lista_users,lista_emails,lista_pass,removidos)
  elif escolha == 6:
    return -1
  else:
    print("Opção inválida!")
programa()

while(programa() != -1):
	pass