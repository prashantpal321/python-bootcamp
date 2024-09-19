# Function to convert USD to INR
def convert_dollar_to_rupees(dollars):
    # Assuming the conversion rate is 1 USD = 83 INR (the rate may vary)
    conversion_rate = 83
    rupees = dollars * conversion_rate
    return rupees

# Taking input from the user
dollars = float(input("Enter amount in US dollars: "))

# Converting and displaying the result
rupees = convert_dollar_to_rupees(dollars)
print(f"{dollars} USD is equal to {rupees} INR")






