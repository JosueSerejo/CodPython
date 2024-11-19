Person_Age = int(input())


Years = Person_Age // 365
Rest = Person_Age % 365
Month = Rest // 30
Day = Rest % 30

print(f'{Years} ano(s)')
print(f'{Month} mes(s)')
print(f'{Day} dia(s)')
