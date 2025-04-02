saldo = 0
while True:
    print("Bem vindo ao Banco!Qual operação deseja fazer?"
          "\n1-Saque"
          "\n2-Depósito"
          "\n3-Verificar Saldo"
          "\n4-Sair")

    escolha = int(input("Número da operação: "))

    if escolha == 1:
        valor_saque = int(input("Digite o valor do saque: "))
        if valor_saque > saldo:
            print(f"Saldo insuficiente! o saque não será efetuado.\n")
        else:
            saldo = saldo - valor_saque
            print(f"Saque efetuado com sucesso! Seu saldo atual é de R${saldo}\n")

    elif escolha == 2:
        valor_deposito = int(input("Digite o valor do deposito: "))
        saldo = saldo + valor_deposito
        print("Deposito realizado com sucesso!")
        print(f"Seu saldo atual é de R${saldo}\n")

    elif escolha == 3:
        print(f"Seu saldo atual é de R${saldo}\n")

    elif escolha == 4:
        print("Obrigado pela preferencia, até logo!")
        break

    else:
        print("Digite um número válido")