while True:
    num1 = int(input("Digite o 1 número: "))
    num2 = int(input("Digite o 2 número: "))

    print("Digite o número da operação que deseja realizar \n"
          "1-Adição \n"
          "2-Subtração \n"
          "3-Divisão \n"
          "4-multiplicação")

    escolha = int(input("Número da operação: "))

    if escolha == 1:
        print("O resultado da operacação é = ", num1 + num2)
        break

    elif escolha == 2:
        print("O resultado da operacação é = ",num1 - num2)
        break

    elif escolha == 3:
        print("O resultado da operacação é = ",num1/num2)
        break

    elif escolha == 4:
        print("O resultado da operacação é = ",num1 * num2)
        break

    else:
        print("Digite um número válido.")