
num = input().split()

n1 = float(num[0])
n2 = float(num[1])
n3 = float(num[2])
n4 = float(num[3])


Media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

print(f'Media: {Media:.1f}')

if Media >= 7.0:
    print('Aluno aprovado.')
    exit()

elif Media < 5.0:
    print('Aluno reprovado.')
    exit()

else:
    print('Aluno em exame.')

    Exame = float(input(''))

    Final = (Exame + Media) / 2

    print(f'Nota do exame: {Exame:.1f}')

if Final >= 5.0:

    print('Aluno aprovado.')

else:
    print('Aluno reprovado.')

print(f'Media final: {Final:.1f}')
