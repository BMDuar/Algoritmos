idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Digite uma idade aceitável.")

elif idade < 12:
    print("Você é classificado como criança.")

elif 13 <= idade <= 17:
    print("Você é classificado como adolecente.")

elif 18 <= idade <= 64:
    print("Você é classificado como adulto.")

elif idade >= 65:
    print("Você é classificado como idoso.")

