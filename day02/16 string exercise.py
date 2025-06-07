# Ask the user for the information of three items

initial_balance = float(input("Initial balance: "))
time_years = int(input("Input time elapsed (in years): "))
interest_rate = float(input("Input interest rate: ")) / 100

print(f"Initial Balance: {initial_balance:.2f}")
print(f"Time (in Years): {time_years:.4f}")
print(f"Interest Rate: {interest_rate:.4%}")

# Then print the following output
#     Initial Balance: PHP Initial Balance (two decimal places)
#     Time (in Years): Years (four decimal places)
#     Interest Rate: Interest Rate in Percentage (four decimal places)
#     ===================================================================
#     Simple Interest: initial_balance * (1 + interest_rate * time_years)