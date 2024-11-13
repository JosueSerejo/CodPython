A, B, C = map(int, input().split())

if (A + B + C == 0 or 
    A + B - C == 0 or 
    A - B + C == 0 or 
    A - B - C == 0 or 
    -A + B + C == 0 or 
    -A + B - C == 0 or 
    -A - B + C == 0 or 
    -A - B - C == 0):
    print("S")
else:
    print("N")
