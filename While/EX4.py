print("Digite o calor em C que deseja converter, digite 'sair' para sair do sistema:")
while True:
    temp = input("Temperatura em C:")
    if temp.lower() == 'sair':
        print("Saindo do sistema")
        break

    try:
        valor = int(temp)
        newValor = (valor * 9/5) + 32
        print(f"Convertendo {valor}°C obtemos {newValor}°F")

    except ValueError:
        print("Por favor, digite um número válido ou 'fim' para terminar.")
