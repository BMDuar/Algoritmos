#Peça um número ao usuário e exiba sua tabuada de 1 a 10, mas se for múltiplo de 3, substitua pelo texto "Multiplo de 3".
numero = int(input("Digite um número: "))
if numero % 3 == 0:
    print("Múltiplo de 3")
else:
    print(f"Tabuada do número {numero}")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")