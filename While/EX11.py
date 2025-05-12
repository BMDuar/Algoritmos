total = 0
quantidade_itens = 0

print("=== CAIXA REGISTRADORA ===")
print('Digite "sair" para finalizar a compra.\n')

while True:
    preco = input("Preço do produto (R$): ").strip()
    if preco.lower() == "sair":
        break

    try:
        preco_float = float(preco)
        if preco_float <= 0:
            print("Preço deve ser maior que zero!")
            continue
    except ValueError:
        print("Digite um valor válido!")
        continue

    quantidade = input("Quantidade: ").strip()
    try:
        quantidade_int = int(quantidade)
        if quantidade_int <= 0:
            print("Quantidade deve ser maior que zero!")
            continue
    except ValueError:
        print("Digite um número inteiro válido!")
        continue

    subtotal = preco_float * quantidade_int
    total += subtotal
    quantidade_itens += quantidade_int
    print(f"Subtotal: R$ {subtotal:.2f}\n")

print("\n=== RESUMO DA COMPRA ===")
print(f"Total de itens: {quantidade_itens}")
print(f"Valor total: R$ {total:.2f}")