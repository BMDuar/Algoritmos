maiorNumero = 0
while True:
    numero = int(input("Digite um número, digite 0 para encerrar: "))
    if numero == 0:
        print("saindo do sistema")
        break
    else:
        if numero > maiorNumero:
            maiorNumero = numero
            print(f"O maior número é: {maiorNumero}")
        else:
            print(f"O maior número ainda é: {maiorNumero}")