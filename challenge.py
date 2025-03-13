## Employee Bonus Salary Calculator
Updated_salary=[]
salary_input = input ("Enter salary for each employees and use space to separate them : ")
salary = list(map(float, salary_input.split())) ## Converts Salaary input into a list while accepting input as float
print(salary)

## Checking for salary bonus

for increase in salary:
    if increase <=50000:
        updated_pay= (0.2 * increase) + increase #Calculating the Salary Gain

    elif increase > 50000 and increase <= 100000:
        updated_pay= (0.1 * increase) + increase #Calculating the Salary Gain

    else:
        updated_pay=increase

    Updated_salary.append(updated_pay)

print(Updated_salary)
total_pay=sum(Updated_salary)
print("Total Payout is:", total_pay)








    
        




