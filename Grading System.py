def get_grade(score):
    if score >= 70 and score <= 100:
        return "A"
    elif score >= 60 and score <= 69:
        return "B"
    elif score >= 50 and score <= 59:
        return "C"
    elif score >= 40 and score <= 49:
        return "D"
    elif score >= 0 and score <= 39:
        return "Fail"
    else:
        return "Invalid score. Please enter a score between 0 and 100."

score = int(input("Enter your score: "))

result = get_grade(score)
print("Your grade is:", result)
