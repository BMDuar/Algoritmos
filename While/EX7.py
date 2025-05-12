print("Digite o calor em dólares que deseja converter, digite 'sair' para sair do sistema:")
while True:
    dolares = input("Valor em dólares:")
    if dolares.lower() == 'sair':
        print("Saindo do sistema")
        break

    try:
        valor = float(dolares)
        newValor = valor * 0.9
        print(f"Convertendo USD{dolares} obtemos EUR{newValor}")

    except ValueError:
        print("Por favor, digite um número válido ou 'fim' para terminar.")
