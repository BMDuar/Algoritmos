print("Calculador de médias, digite as notas(0 a 10)")
contador = 0
valorTotal = 0

while True:
    nota = input("Digite a nota, digite 'calcular' para calcular e 'sair' para sair':")

    if nota.lower() == 'sair':
        print("Saindo do sistema")
        break

    if nota.lower() == 'calcular':
        try:
            valor = int(nota)
            contador += 1
            valorTotal += valor
            print(valorTotal/contador)

        except ValueError:
            print("Por favor, digite um número válido ou 'fim' para terminar.")


