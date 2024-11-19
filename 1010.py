
Values1 = input().split()

P1 = int(Values1[0])
N1 = int(Values1[1])
V1 = float(Values1[2])

Values2 = input().split()

P2 = int(Values2[0])
N2 = int(Values2[1])
V2 = float(Values2[2])


Total = (N1 * V1) + (N2 * V2)


print(f'VALOR A PAGAR: R$ {Total:.2f}')