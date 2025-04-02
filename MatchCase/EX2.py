#Calculo da área de figuras geométricas
opcao = input("Qual figura geometrica você deseja saber a área? ")

match opcao:
    case "quadrado":
        aresta = input("Digite o valor da aresta da figura: ")
        calculo = aresta*aresta
        print(f"A área do quadrado é:{round(calculo,2)}m²")

    case "triangulo":
        altura = float(input("Digite o valor da altura da figura: "))
        base = float(input("Digite o valor da base da figura: "))
        calculo = (base*altura)/2
        print(f"A área do triângulo é:{round(calculo,2)}m²")

    case "retangulo":
        altura = float(input("Digite o valor da altura da figura: "))
        base = float(input("Digite o valor da base da figura: "))
        calculo = base*altura
        print(f"A área do triângulo é:{round(calculo, 2)}m²")