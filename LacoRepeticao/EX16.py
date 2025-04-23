#Peça ao usuário um número N e exiba quantos números entre 1 e N são múltiplos de 3 ou 5.
N = int(input("Digite um número inteiro positivo N: "))

contador = 0

for numero in range(1, N + 1):
    if numero % 3 == 0 or numero % 5 == 0:
        contador += 1

print(f"\nEntre 1 e {N}, existem {contador} números múltiplos de 3 ou 5.")