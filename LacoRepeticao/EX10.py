#Solicite um número ao usuário e exiba o seu fatorial (n!).
numero = int(input("Digite o número: "))

fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
    print(fatorial)

