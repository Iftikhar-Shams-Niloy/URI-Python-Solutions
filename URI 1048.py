
salary = float(input())
if salary >= 0 and salary <=400:
    salary_increase = salary*0.15
    new_salary = salary+salary_increase
    increase_percentage = 15
elif salary>=400.01 and salary <= 800:
    salary_increase = salary*0.12
    new_salary = salary+salary_increase
    increase_percentage = 12
elif salary >=800.01 and salary <=1200:
    salary_increase = salary*0.1
    new_salary = salary+salary_increase
    increase_percentage = 10
elif salary >= 1200.01 and salary <= 2000:
    salary_increase = salary*0.07
    new_salary = salary + salary_increase
    increase_percentage = 7
elif salary > 2000:
    salary_increase = salary*0.04
    new_salary = salary+salary_increase
    increase_percentage = 4

print("Novo salario: %.2f"%new_salary)
print("Reajuste ganho: %.2f"%salary_increase)
print("Em percentual: {} %".format(increase_percentage))
