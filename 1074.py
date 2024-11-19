N = int(input())

for _ in range(N):
    X = int(input())

    if X == 0:
     print('NULL')

    elif X % 2 == 0 and X > 0:
      print('EVEN POSITIVE')

    elif X % 2 != 0 and X > 0:
     print('ODD POSITIVE')

    elif X % 2 == 0 and X < 0:
     print('EVEN NEGATIVE')

    else:
     print('ODD NEGATIVE')
