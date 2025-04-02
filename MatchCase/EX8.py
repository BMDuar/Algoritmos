#Calculo valor de viagens

destino = input("Digite o o destino da viagem: ")

match destino:
    case "sao paulo":
        print(f"O valor da passagem para {destino} é de:R$500 ")

    case "rio de janeiro":
        print(f"O valor da passagem para {destino} é de:R$1000 ")

    case "curitiba":
        print(f"O valor da passagem para {destino} é de:R$2000 ")

    case "salvador":
        print(f"O valor da passagem para {destino} é de:R$3000 ")
