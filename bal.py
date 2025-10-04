# Program to update balance after deposit and withdrawal

# Taking input from user
initial_balance = float(input("Enter your initial balance: "))

# Deposit
deposit_amount = float(input("Enter the deposit amount: "))
balance_after_deposit = initial_balance + deposit_amount
print("Balance after deposit:", balance_after_deposit)

# Withdrawal
withdraw_amount = float(input("Enter the amount to withdraw: "))

# Check if sufficient balance
if withdraw_amount > balance_after_deposit:
    print("Insufficient balance! Withdrawal not possible.")
    updated_balance = balance_after_deposit
else:
    updated_balance = balance_after_deposit - withdraw_amount
    print("Withdrawal successful!")

# Display final balance
print("Your updated balance is:", updated_balance)
