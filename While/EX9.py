import random

print("Simulação de Leitura de Sensor (0-100)")
print("O sensor parará quando detectar um valor fora do intervalo.\n")

while True:
    valor = random.uniform(-10, 110)  # Simula leituras ocasionalmente fora do range
    print(f"Leitura do sensor: {valor:.2f}")

    if valor < 0 or valor > 100:
        print("️ALERTA: Valor fora do intervalo permitido (0-100)! Encerrando leitura...")
        break