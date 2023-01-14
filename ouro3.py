def main():
  def converter(moeda1, moeda2, valor):
   if moeda1 == "1":
    if moeda2 == "1":
      return round(valor, 1)
    elif moeda2 == "2":
      return round(valor * 1.13, 1)
    else:
      return round(valor * 6.11, 1)
   elif moeda1 == "2":
    if moeda2 == "1":
      return round(valor * 0.89, 1)
    elif moeda2 == "2":
      return round(valor, 1)
    else:
      return round(valor * 5.42, 1)
   else:
    if moeda2 == "1":
      return round(valor * 0.16, 1)
    elif moeda2 == "2":
      return round(valor * 0.18, 1)
    else:
      return round(valor, 1)

  def comparar(moeda1, moeda2, valor1, valor2):
    convertido = converter(moeda2, moeda1, valor2)
    if moeda1 == "1":
      if moeda2 == "1":
        print(f"{valor1} EUR = {valor2} EUR")
      elif moeda2 == "2": 
        if valor1 > convertido:
          print(f"{valor1} EUR > {convertido} USD ")
        else:
          print(f"{valor1} EUR < {convertido} USD ")
      elif moeda2 == "3":    
        if valor1 > convertido:
          print(f"{valor1} EUR > {convertido} BRL ")
        else:
          print(f"{valor1} EUR < {convertido} BRL ")
      else:
        print("Opção inválida!")
    elif moeda1 == "2":
      if moeda2 == "1":
        if valor1 > convertido:
          print(f"{valor1} USD > {convertido} EUR ")
        else:
          print(f"{valor1} USD < {convertido} EUR ")
      elif moeda2 == "2":
        print(f"{valor1} USD = {valor2} USD")
      elif moeda2 == "3":   
        if valor1 > convertido:
          print(f"{valor1} USD > {convertido} BRL ")
        else:
          print(f"{valor1} USD < {convertido} BRL ")
      else:
        print("Opção inválida!")
    elif moeda1 == "3":
      if moeda2 == "1":     
        if valor1 > convertido:
          print(f"{valor1} BRL > {convertido} EUR ")
        else:
          print(f"{valor1} BRL < {convertido} EUR ")
      elif moeda2 == "2":   
        if valor1 > convertido:
          print(f"{valor1} BRL > {convertido} USD ")
        else:
          print(f"{valor1} BRL < {convertido} USD ")
      elif moeda2 == "3":
        print(f"{valor1} BRL = {valor2} BRL")
      else:
        print("Opção inválida!")
    else:
      print("Opção inválida")

  opc = input(('''Bem-vindo! Escolha a opção que pretende realizar
  1 - Conversor de Moeda
  2 - Comparação de valor de moedas
  3 - O que pode comprar com o seu dinheiro?
  4 - Progresso de poupança '''))

  if opc == "1":
    moeda1 = input('''Converter de:
    1 - EUR
    2 - USD
    3 - BRL ''')

    moeda2 = input('''Converter para:
    1 - EUR
    2 - USD
    3 - BRL ''')
    
    valor = round(int(input("Quantia a converter: ")),1)
    convertido = converter(moeda1, moeda2, valor)
    if moeda1 == "1":
      if moeda2 == "1":
        print(f"{valor} EUR = {convertido} EUR")
      elif moeda2 == "2":
        print(f"{valor} EUR = {convertido} USD")
      elif moeda2 == "3":
        print(f"{valor} EUR = {convertido} BRL")
      else:
        print("Opção inválida!")
    elif moeda1 == "2":
      if moeda2 == "1":
        print(f"{valor} USD = {convertido} EUR")
      elif moeda2 == "2":
        print(f"{valor} USD = {convertido} USD")
      elif moeda2 == "3":
        print(f"{valor} USD = {convertido} BRL")
      else:
        print("Opção inválida!")
    elif moeda1 == "3":
      if moeda2 == "1":
        print(f"{valor} BRL = {convertido} EUR")
      elif moeda2 == "2":
        print(f"{valor} BRL = {convertido} USD")
      elif moeda2 == "3":
        print(f"{valor} BRL = {convertido} BRL")
      else:
        print("Opção inválida!")
    else:
      print("Opção inválida")
  elif opc == "2":
    moeda1 = input('''Moeda a comparar:
    1 - EUR
    2 - USD
    3 - BRL ''')
    valor1 = int(input("Primeira quantia a comparar: "))
    moeda2 = input('''Comparar a:
    1 - EUR
    2 - USD
    3 - BRL ''')
    valor2 = int(input("Segunda quantia a comparar: "))
    comparar(moeda1, moeda2, valor1, valor2)
  elif opc == "3":
    dinheiro = int(input("Quanto dinheiro tens? "))
    moeda = input('''Que moeda estás a usar?
    1 - EUR
    2 - USD
    3 - BRL ''')
    eur = converter(moeda, "1", dinheiro)
    if eur < 30:
      print("Consegues comprar ingredientes para fazer 'Pasta alla Carbonara' para 10 pessoas!")
    elif eur < 80:
      print("Podes comprar novas peças de vestuário e dar um retoque no visual!")
    elif eur < 450:
      print("Podes comprar um smartphone novo e alugar uma casa de férias em Aveiro!")
    elif eur < 1000:
      print("Já tens o suficiente para comprar uma consola de última geração. Diverte-te!")
    elif eur < 2500:
      print("Já podes comprar um carro bom! (não inclui a carta ;))")
    else:
      print("Uau! És uma das pessoas mais ricas do mundo!")
  elif opc == "4":
    objetivo = int(input("Quantidade que deseja poupar: "))
    poupado = int(input("Quantidade que já juntou: "))
    if poupado >= objetivo:
      print(f"Já atingiu o seu objetivo de {objetivo}!")
    else:
      print(f"Já poupou {round((poupado * 100)/objetivo, 2)}% ({poupado}) do seu objetivo de {objetivo}!")
  else:
    print("Opção inválida!")
  continuar()

def continuar():
  opcao = input("Gostaria de continuar? (S/N) ")
  if opcao == "S" or opcao == "s":
    main()
  elif opcao == "N" or opcao == "n":
    print("Até à próxima!")
  else:
    print("Opção inválida.")
    continuar()
    
main()