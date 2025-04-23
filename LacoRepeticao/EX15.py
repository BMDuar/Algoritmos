#Peça ao usuário 10 números e exiba quantos são positivos, negativos ou zero.

positivos = 0
negativos = 0
zeros = 0

for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    elif numero == 0:
        zeros += 1

print(f"\nQuantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade de zeros: {zeros}")


