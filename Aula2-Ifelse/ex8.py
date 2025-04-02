peso = float(input("Digite o seu peso em kg:"))
altura = float(input("Digite a sua altura em mentros"))

imc = peso/(altura*altura)
print(imc)

if imc < 18.5:
    print("\nPeso abaixo do normal")

elif 18.5 <= imc <= 25:
    print("\nPeso normal")

elif 25 <= imc <= 30:
    print("\nSobrepeso")

elif imc > 30:
    print("\nObeseidade")