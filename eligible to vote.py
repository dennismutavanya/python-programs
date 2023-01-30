
def eligible_to_vote(citizenship, age):
    if citizenship in ['Kenya', 'Uganda', 'Tanzania'] and age >= 18:
        return True
    return False

citizenship = input("Enter your citizenship: ")
age = int(input("Enter your age: "))

if eligible_to_vote(citizenship, age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

