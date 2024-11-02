even = 0
odd = 0
pos = 0
neg = 0


for i in range(5):
    number = int(input())

    if number % 2 == 0:
        even += 1

    else:
        odd += 1


    if number > 0:
        pos += 1

    elif number < 0:
        neg += 1


print(f'{even} valor(es) par(es)')
print(f'{odd} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')