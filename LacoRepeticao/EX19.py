#O computador escolhe um número aleatório de 1 a 10, e o usuário tem 3 tentativas para adivinhar. Dê dicas se o número é maior ou menor.
import random

numero_secreto = random.randint(1, 10)
tentativas = 3

print("Jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 10. Você tem 3 tentativas.")

for tentativa in range(1, tentativas + 1):
    print(f"\nTentativa {tentativa} de {tentativas}")
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou! O número era {numero_secreto}.")
        break
    elif palpite < numero_secreto:
        print("Dica: O número é maior que isso.")
    else:
        print("Dica: O número é menor que isso.")

    if tentativa == tentativas:
        print(f"\nSuas tentativas acabaram! O número era {numero_secreto}.")