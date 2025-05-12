print("SUPERMERCADO EDNALDO PEREIRA 2")
saldo = int(input("Digite o valor do seu saldo:"))
while True:
    valorProduto = input("Digite o valor do produto que deseja comprar,digite 'sair' para sair: ")
    if valorProduto.lower() == 'sair':
        print("Saindo do sistema")
        break

    try:
        valor = int(valorProduto)
        saldo -= valor
        print(f"Seu saldo atual é: {saldo}")

        if saldo < valor:
            print(f"Saldo insuficiente!\n Desposite mais para continuar as operações! \n Seu saldo atual é de: {saldo}")

    except ValueError:
        print("Por favor, digite um número válido ou 'fim' para terminar.")
