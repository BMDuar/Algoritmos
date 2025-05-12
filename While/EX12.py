estoque = {"Camiseta": 10, "Calça": 5, "Tênis": 3}

print("=== SISTEMA DE VENDAS ===")
print("Produtos disponíveis:")
for produto, qtd in estoque.items():
    print(f"{produto}: {qtd} unidades")
print('Digite "sair" para encerrar.\n')

while True:
    produto = input("Produto: ").strip().title()
    if produto.lower() == "sair":
        break

    if produto not in estoque:
        print("Produto não encontrado!")
        continue

    try:
        qtd_venda = int(input("Quantidade: "))
        if qtd_venda <= 0:
            print("Quantidade deve ser maior que zero!")
            continue
    except ValueError:
        print("Digite um número válido!")
        continue

    if estoque[produto] >= qtd_venda:
        estoque[produto] -= qtd_venda
        print(f"Venda realizada: {qtd_venda} {produto}(s). Estoque restante: {estoque[produto]}")
    else:
        print(f"Estoque insuficiente! Apenas {estoque[produto]} {produto}(s) disponíveis.")

print("\n=== ESTOQUE FINAL ===")
for produto, qtd in estoque.items():
    print(f"{produto}: {qtd} unidades")