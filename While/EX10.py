votos = {"Candidato A": 0, "Candidato B": 0, "Candidato C": 0}

print("Sistema de Votação (Candidatos: A, B, C)")
print('Digite "fim" para encerrar e mostrar resultados.\n')

while True:
    voto = input("Voto (A/B/C): ").upper().strip()

    if voto == "FIM":
        break
    elif voto in ("A", "B", "C"):
        candidato = f"Candidato {voto}"
        votos[candidato] += 1
        print(f"Voto registrado para {candidato}.")
    else:
        print("Opção inválida! Use A, B ou C.")

print("\n=== RESULTADO DA VOTAÇÃO ===")
for candidato, qtd_votos in votos.items():
    print(f"{candidato}: {qtd_votos} votos")