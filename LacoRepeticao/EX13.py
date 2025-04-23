#Peça um número ao usuário e some separadamente os pares e os ímpares de 1 até esse número.
soma_pares = 0
soma_impares = 0

numero = int(input("Digite um número:"))

for i in range(1, numero + 1):
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i

print(f"\nSoma dos números pares de 1 até {numero}: {soma_pares}")
print(f"Soma dos números ímpares de 1 até {numero}: {soma_impares}")
