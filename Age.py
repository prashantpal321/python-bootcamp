from datetime import date

# Function to calculate age
def calculate_age(birth_year):
    current_year = date.today().year
    age = current_year - birth_year
    return age

# Taking input from the user
birth_year = int(input("Enter your birth year: "))

# Calculating and displaying the result
age = calculate_age(birth_year)
print(f"Your age is: {age} years")