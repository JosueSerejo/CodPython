n1 = float(input())

while n1 < 0 or n1 > 10:
    print('nota inválida')
    break


n2 = float(input())
while n2 < 0 or n2 > 10:
    print('nota inválida')
    exit()

m = (n1 + n2) / 2

print(f'media = {m:.2f}')
