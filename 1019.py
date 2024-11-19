#BeeCrowd - 1019

timeSecond = int(input(''))

hora = timeSecond // 3600
resto = timeSecond % 3600

minuto = resto // 60
segundo = resto % 60

print(f'{hora}:{minuto}:{segundo}')

