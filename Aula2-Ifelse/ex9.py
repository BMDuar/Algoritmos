valor = float(input("Digite o valor do produto: "))

if valor > 100:
    valor_final = valor*0.9
    print("O valor final do produto após 10% de desconto é: ", valor_final)

else:
    print("O produto não recebeu desconto,o valor final é de: ",valor)