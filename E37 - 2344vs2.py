Note = int(input())

if Note in range(0, 1):
    print('E')
elif Note in range(1, 36):
    print('D')
elif Note in range(36, 61):
    print('C')
elif Note in range(61, 86):
    print('B')
elif Note in range(86, 101):
    print('A')
