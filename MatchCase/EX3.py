#Sistema simples de login
opcao = input("Digite o seu acesso: ")

match opcao:
    case "admin":
        print("Acesso total ao sistema")

    case "professor":
        print("Acesso ao ambiente de acadêmico")

    case "aluno":
        print("Acesso ao ambiente de estudo")