CountPar = 0

for i in range(5):
    number = int(input())

    if number % 2 == 0:

        CountPar += 1

print(f'Você digitou {CountPar} números pares.')