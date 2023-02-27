def calculate_compound_interest(principal, rate, time, compound_periods):
    """
    Calculates compound interest using the formula:
    A = P(1 + r/n)^(nt)
    where A is the amount, P is the principal, r is the annual interest rate,
    t is the number of years, and n is the number of times interest is compounded per year.
    """
    amount = principal * (1 + rate/compound_periods)**(compound_periods*time)
    return amount - principal

# Example usage:
principal = 1000
rate = 0.05
time = 5
compound_periods = 12

interest = calculate_compound_interest(principal, rate, time, compound_periods)
print(f"The compound interest after {time} years at an annual rate of {rate} is ${interest:.2f}")
