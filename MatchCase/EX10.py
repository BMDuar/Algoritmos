#Sistema de pagamento

opcao = input("Digite a forma de pagamento: ")

match opcao:
    case "dinheiro":
        print("O valor não será alterado")

    case "boleto":
        print("O valor será acrescido em 2%")

    case "cartao":
        print("O valor será acrescido em 5%")

    case "pix":
        print("Desconto de 5%")