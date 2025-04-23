#Escreva um programa que exiba os números de 1 a 20 e indique se cada um é par ou ímpar.

for numero in range(1, 21):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")