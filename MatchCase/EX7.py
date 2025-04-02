#Calculadora

opcao = input("Qual operação você deseja realizar? ")

match opcao:
    case "adicao":
        num1 = float(input("digite o num1"))
        num2 = float(input("digite o num2"))
        operacao = num1 + num2
        print(f"O resultado da adicao é:{operacao}")

    case "subtracao":
        num1 = float(input("digite o num1"))
        num2 = float(input("digite o num2"))
        operacao = num1 - num2
        print(f"O resultado da subtração é:{operacao}")

    case "divisao":
        num1 = float(input("digite o num1"))
        num2 = float(input("digite o num2"))
        operacao = num1 / num2
        print(f"O resultado da divisão é:{operacao}")

    case "multiplicacao":
        num1 = float(input("digite o num1"))
        num2 = float(input("digite o num2"))
        operacao = num1 * num2
        print(f"O resultado da multiplicação é:{operacao}")