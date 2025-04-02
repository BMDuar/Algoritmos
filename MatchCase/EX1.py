#EX1 conversor de moedas

valor = float(input("Digite o valor que deseja converter: "))
conversao = input("Você deseja converter para Dolar,Euro ou Libra? ")

match conversao:
    case "Dolar":
        valor_final = valor/5.6
        print(f"Você possui R${round(valor_final,3)} dólares")

    case "Euro":
        valor_final = valor/6.13
        print(f"Você possui R${round(valor_final,3)} euros")

    case "Libra":
        valor_final = valor/7.34
        print(f"Você possui R${round(valor_final,3)} libras")