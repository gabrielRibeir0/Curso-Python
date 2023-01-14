corretas = 0

print("""Quiz sobre a História de Portugal, desde o passado à ataulidade
Este quiz contém 8 perguntas para responderes. Pronto?""")

resposta = input(("""Pergunta 1 - Quem foi o 1º Rei de Portugal?
1 - D.João I
2 - D.Afonso I
3 - D.Afonso Henriques"""))
if resposta == "3":
  print("Parabéns, acertaste!")
  corretas += 1
else:
    print("Erraste. A resposta correta era D.Afonso Henriques.")

resposta = input(("""Pergunta 2 - Quem é o atual presidente de Portugal?
1 - Marcelo Rebelo de Sousa
2 - António Costa
3 - Manuel Luís Goucha"""))
if resposta == "1":
  print("Parabéns, acertaste!")
  corretas += 1
else:
    print("Erraste. A resposta correta era Marcelo Rebelo de Sousa.")

resposta = input(("""Pergunta 3 - Quando é que o Euro foi introduzido em Portugal?
1 - 1 de Janeiro de 2004
2 - 1 de Janeiro de 2002
3 - 1 de Janeiro de 1999"""))
if resposta == "2":
  print("Parabéns, acertaste!")
  corretas += 1
else:
    print("Erraste. A resposta correta era 1 de Janeiro de 2002.")

resposta = input(("""Pergunta 4 - A 10 de Julho de 2016 Portugal venceu o Campeonato Europeu de Futebol. Quem marcou o golo decisivo?
1 - Éder
2 - Cristiano Ronaldo
3 - Quaresma"""))
if resposta == "1":
  print("Parabéns, acertaste!")
  corretas += 1
else:
    print("Erraste. A resposta correta era Éder.")

resposta = input(("""Pergunta 5 - Quem foi o último rei de Portugal?
1 -D.João VI
2 -D.Luís
3 -D.Manuel II"""))
if resposta == "3":
  print("Parabéns, acertaste!")
  corretas += 1
else:
    print("Erraste. A resposta correta era D.Manuel II.")

resposta = input(("""Pergunta 6 - Quem escreveu "Os Lusíadas"?
1 - Luís de Camões
2 - Fernando Pessoa
3 - José Saramago"""))
if resposta == "1":
  print("Parabéns, acertaste!")
  corretas += 1
else:
    print("Erraste. A resposta correta era Luís de Camões.")

resposta = input(("""Pergunta 7 - Que rei português desapareceu numa batalha e, diz-se, voltará numa manhã de nevoeiro?
1 - D.Dinis
2 - D.Afonso Henriques
3 - D.Sebastião"""))
if resposta == "3":
  print("Parabéns, acertaste!")
  corretas += 1
else:
    print("Erraste. A resposta correta era D.Sebastião.")

resposta = input(("""Pergunta 8 - Qual o nome do regime que acabou a 25 de Abril de 1974?
1 - Estado Novo
2 - Monarquia Portuguesa
3 - Antigo Regime"""))
if resposta == "1":
  print("Parabéns, acertaste!")
  corretas += 1
else:
    print("Erraste. A resposta correta era Estado Novo.")

print("Muito bem, chegaste ao fim do quiz! Vamos ver como te saíste.")

if corretas <= 3:
  print(f"Não te saíste muito bem, apenas acertaste {corretas} perguntas")
elif corretas <= 5:
  print(f"Não está ótimo, mas não está mau. Conseguiste acertar {corretas} perguntas")
else:
  print(f"Muito bem! Conseguiste acertar {corretas} questões. És um craque!")