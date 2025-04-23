#Solicite ao usuário um número e verifique se ele é par ou ímpar.
#Se o número for par, divida-o por 2 e exiba o resultado.
#Se o número for ímpar, multiplique-o por 3 e exiba o resultado.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    resultado = numero / 2
    print(f"O número {numero} é par. {numero} ÷ 2 = {resultado}")
else:
    resultado = numero * 3
    print(f"O número {numero} é ímpar. {numero} × 3 = {resultado}")