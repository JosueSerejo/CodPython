
sum_ages = 0
quantity = 0

while True:
    age = int(input())

    if age < 0:
     break

    sum_ages += age
    quantity += 1


if quantity > 0:
   total = sum_ages / quantity

print(f'{total:.2f}')