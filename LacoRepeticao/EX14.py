#Peça ao usuário para digitar 5 números e exiba o maior e o menor deles
numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"\nO maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")