#Simulador de compras on-line

opcao = input("digite o nome de um produto que voce quer comprar\n "
              "OPCOES\n "
              "pc\n "
              "monitor\n "
              "mouse\n "
              "digite aqui: ")

match opcao:
    case "pc":
        print("O preco é : R$1000,00")

    case "mouse":
        print("O preco é : R$150,00")

    case "monitor":
        print("O preco é : R$599,99")

    case _:
        print("opcao invalida")