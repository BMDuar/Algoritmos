idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade.")

elif idade > 65:
    print("Você faz parte do grupo de idosos.")

elif 18 < idade < 65:
    print("Você é maior de idade.")

else:
    print("Insira uma informação coerente.")