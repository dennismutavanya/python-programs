def calculate_bonus(salary, years_of_service):
    if years_of_service >= 10:
        bonus = salary * 0.10
    elif years_of_service >= 6 and years_of_service <= 10:
        bonus = salary * 0.08
    elif years_of_service < 6:
        bonus = salary * 0.05
    else:
        bonus = 0
    
    net_bonus = salary + bonus
    return net_bonus

salary = float(input("Enter your salary: "))
years_of_service = float(input("Enter your years of service: "))

result = calculate_bonus(salary, years_of_service)
print("Your net bonus amount is:", result)
