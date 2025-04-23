#Peça ao usuário um número N e exiba todos os números de 1 até N que são múltiplos de 3 e 5
N = int(input("Digite um número inteiro positivo N: "))

print(f"\nNúmeros de 1 a {N} que são múltiplos de 3 e 5 (múltiplos de 15):")

for numero in range(1, N + 1):
    if numero % 3 == 0 and numero % 5 == 0:
        print(numero)