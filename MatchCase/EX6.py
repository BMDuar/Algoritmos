#Simulação de atendimento telefonico

print("Bem vindo! O que deseja realizar?"
      "1- Suporte Técnico\n"
      "2- Financeito\n"
      "3- Cancelamento\n"
      "4- Falar com um atendente")

opcao = int(input("Digite o valor da operação: "))

match opcao:
    case "1":
        print(f"Bem vindo ao canal {opcao} qual o seu problema...")

    case "2":
        print(f"Bem vindo ao canal {opcao}, dúvidas em relação a pagamentos?...")

    case "3":
        print(f" Bem vindo ao canal {opcao}, para realizarmos o cancelamento é preciso que envie alguns documentos...")

    case "4":
        print(f"Bem vindo ao canal {opcao},encontrando um atendente disponível...")
