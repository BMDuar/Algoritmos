#Cálculo de Desconto por Categoria

produto = input("Digite o tipo de produto para saber seu desconto: ")
match produto:
    case "eletronico":
        print(f"O tipo {produto} possui 10% de desconto!")

    case "roupas":
        print(f"O tipo {produto} possui 25% de desconto!")

    case "Alimentos":
        print(f"O tipo {produto} possui 15% de desconto")

    case "moveis":
        print(f"O tipo {produto} possui 10% de desconto")

