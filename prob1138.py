while True:
    # Lê a entrada
    entrada = input()
    A, B = map(int, entrada.split())
    
    # Verifica o caso de término
    if A == 0 and B == 0:
        break

    # Inicializa a contagem dos dígitos de 0 a 9
    contagem = [0] * 10

    # Itera sobre todos os números de A até B
    for num in range(A, B + 1):
        for digito in str(num):  # Converte o número para string para iterar sobre os dígitos
            contagem[int(digito)] += 1

    # Imprime a contagem dos dígitos
    print(" ".join(map(str, contagem)))
