nota = int(input("Digite a nota do aluno: "))

if 90 <= nota <= 100:
    print("Nota A.")

elif 80 <= nota < 89:
    print("Nota B.")

elif 70 <= nota <= 79:
    print("Nota C.")

elif 60 <= nota <= 69:
    print("Nota D.")

elif nota < 60:
    print("Nota F.")

