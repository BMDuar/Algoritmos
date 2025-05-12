contador = 0
while True:
    numero = int(input("Digite o número que deseja somar, digite 0 para sair: "))
    if numero == 0 :
        print("Saindo do sistema")
        break
    else:
        contador += numero
        print(f"A soma é igual a:{contador}")
