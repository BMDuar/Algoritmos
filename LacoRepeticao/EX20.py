#Crie um programa que solicite ao usuário um número e informe se ele é primo ou não. Lembre-se de que um número primo é aquele que é divisível apenas por 1 e por ele mesmo.
numero = int(input("Digite um número inteiro positivo: "))

if numero > 1:
    eh_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
else:
    eh_primo = False

if eh_primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")