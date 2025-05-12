positivos = 0
negativos = 0
zeros = 0

print("Digite os valores (digite 'fim' para terminar):")

while True:
    entrada = input("Valor: ")

    if entrada.lower() == 'fim':
        break

    try:
        valor = float(entrada)

        if valor > 0:
            positivos += 1
        elif valor < 0:
            negativos += 1
        else:
            zeros += 1
    except ValueError:
        print("Por favor, digite um número válido ou 'fim' para terminar.")

print(f"Valores positivos: {positivos}")
print(f"Valores negativos: {negativos}")
print(f"Zeros: {zeros}")