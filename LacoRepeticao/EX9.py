#Peça um número ao usuário e some seus dígitos

numero = int(input("Digite um número: "))
soma = 0

for digito in str(numero):
  soma += int(digito)

print(f"A soma dos dígitos é: {soma}")
