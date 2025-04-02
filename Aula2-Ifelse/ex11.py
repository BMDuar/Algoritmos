idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Sua categoria será a INFANTIL")

elif  18 <= idade <= 30:
    print("Sua categoria será a ADULTO")

elif idade > 30:
    print("Sua categorai será a VETERANO")