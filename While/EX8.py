estoque = {}


def menu():
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Consultar estoque")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao


def adicionar_produto():
    nome = input("Nome do produto: ").strip()
    try:
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero!")
            return
    except ValueError:
        print("Digite um número válido!")
        return

    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    print(f"{quantidade} unidades de '{nome}' adicionadas ao estoque.")


def remover_produto():
    nome = input("Nome do produto: ").strip()
    if nome not in estoque:
        print("Produto não encontrado no estoque!")
        return

    try:
        quantidade = int(input("Quantidade a remover: "))
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero!")
            return
    except ValueError:
        print("Digite um número válido!")
        return

    if estoque[nome] >= quantidade:
        estoque[nome] -= quantidade
        print(f"{quantidade} unidades de '{nome}' removidas do estoque.")
        if estoque[nome] == 0:
            del estoque[nome]
    else:
        print(f"Estoque insuficiente! Há apenas {estoque[nome]} unidades de '{nome}'.")


def consultar_estoque():
    if not estoque:
        print("Estoque vazio!")
    else:
        print("\n=== ESTOQUE ATUAL ===")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade} unidades")


# Loop principal
while True:
    opcao = menu()
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        remover_produto()
    elif opcao == "3":
        consultar_estoque()
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")