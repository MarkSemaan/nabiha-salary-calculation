import random

print("Welcome, Nabiha.\n")

# Input from user
salary = float(input("Please enter your salary for the month: "))
month = input("Please enter the name of the month: ")
savings_percent = float(input("Enter the percentage allocated to savings (%): "))
rent_percent = float(input("Enter the percentage allocated to rent (%): "))
electricity_percent = float(input("Enter the percentage allocated to electricity (%): "))

# Calculations for allocations
savings = (savings_percent / 100) * salary
rent = (rent_percent / 100) * salary
electricity = (electricity_percent / 100) * salary

total_spent = savings + rent + electricity
remainder = salary - total_spent

# Yearly projections
yearly_rent = rent * 12
yearly_electricity = electricity * 12

# Fun calculation
salary_squared = salary ** 2

# Additional savings calculation
additional_savings = random.randint(50, 100)  # Random amount between $50 and $100
savings_ratio = additional_savings / savings  # Could cause division by zero if savings is 0

# Display results
print("\n--- Monthly Financial Report for", month, "---")
print(f"Salary: ${salary:.2f}")
print("\nExpenses Allocation:")
print(f"Savings ({savings_percent}%): ${savings:.2f}")
print(f"Rent ({rent_percent}%): ${rent:.2f}")
print(f"Electricity ({electricity_percent}%): ${electricity:.2f}")
print(f"\nTotal Expenses: ${total_spent:.2f}")
print(f"Remaining Salary: ${remainder:.2f}")
print("\nYearly Projections:")
print(f"Yearly Rent: ${yearly_rent:.2f}")
print(f"Yearly Electricity: ${yearly_electricity:.2f}")
print(f"\nFun Calculation - Salary Squared: ${salary_squared:.2f}")
print("\nAdditional Savings Calculation:")
print(f"Additional Savings Amount: ${additional_savings:.2f}")
print(f"Additional Savings Divided by Allocated Savings: {savings_ratio:.2f}")