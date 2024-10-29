
N1 = float(input())
N2 = float(input())
N3 = float(input())
N4 = float(input())


Media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

print(f'{Media:.1f}')

if Media > 5.0:
    print('Aluno aprovado')

else:
    print('Aluno reprovado')