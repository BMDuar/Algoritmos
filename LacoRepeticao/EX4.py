#Peça ao usuário três números: início, fim e passo e exiba a sequência correspondente.
inicio = int(input("Digite o início:"))
fim = int(input("Digite o fim:"))
passo = int(input("Digite o passo:"))

for i in range(inicio,fim + passo,passo):
    print(i)
