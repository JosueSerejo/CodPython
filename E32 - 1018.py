#Cédulas


Valor = int(input())

Initial_Valor = Valor


Bank_Notes = [100, 50, 20, 10, 5, 2, 1]


for nota in Bank_Notes:
    quantidade = Valor // nota 
    Bank_Notes %= nota               

print(f"{quantidade} nota(s) de R$ {nota},00")