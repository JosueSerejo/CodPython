
Salary = float(input())

if Salary >= 0 and Salary <= 400.00:
   Percent = Salary * 0.15
   NewSalary = Salary + Percent
   Readjustment = NewSalary - Salary
   PercentNumber = 15

elif Salary >= 400.01 and Salary <= 800.00:
   Percent = Salary * 0.12
   NewSalary = Salary + Percent
   Readjustment = NewSalary - Salary
   PercentNumber = 12

elif Salary >= 800.01 and Salary <= 1200.00:
   Percent = Salary * 0.10
   NewSalary = Salary + Percent
   Readjustment = NewSalary - Salary
   PercentNumber = 10


elif Salary >= 1200.01 and Salary <= 2000.00:
   Percent = Salary * 0.07
   NewSalary = Salary + Percent
   Readjustment = NewSalary - Salary
   PercentNumber = 7

elif Salary > 2000.00:
   Percent = Salary * 0.04
   NewSalary = Salary + Percent
   Readjustment = NewSalary - Salary
   PercentNumber = 4




print(f'Novo salario: {NewSalary:.2f}')
print(f'Reajuste ganho: {Readjustment:.2f}')
print(f'Em percentual: {PercentNumber} %')