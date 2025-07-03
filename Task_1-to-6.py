import re


accounts = {
    "123456": 1200.50,
    "234567": 4300.00,
    "345678": 875.25
}

while True:
    print("\n--- Bank System Menu ---")
    print("1. Loan Eligibility Check")
    print("2. ATM Transaction Simulation")
    print("3. Compound Interest Calculator")
    print("4. Account Balance Checker")
    print("5. Password Validator")
    print("6. Transaction History Recorder")
    print("7. Exit")

    choice = input("Select a task (1-7): ")

    if choice == '1':
        # Task 1: Loan Eligibility
        print("\n--- Loan Eligibility Check ---")
        credit_score = int(input("Enter your credit score: "))
        income = float(input("Enter your annual income: $"))

        if credit_score > 700 and income >= 50000:
            print("You are eligible for a loan.")
        else:
            print("You are NOT eligible for a loan.")

    elif choice == '2':
        # Task 2: ATM Simulation
        print("\n--- ATM Simulation ---")
        balance = float(input("Enter your current balance: $"))
        print("Options: 1) Check Balance  2) Withdraw  3) Deposit")
        option = input("Choose an option (1/2/3): ")

        if option == '1':
            print(f"Your balance is: ${balance:.2f}")
        elif option == '2':
            amount = float(input("Enter withdrawal amount (multiples of 100 or 500): $"))
            if amount > balance:
                print("Insufficient funds.")
            elif amount % 100 != 0 and amount % 500 != 0:
                print("Amount must be in multiples of 100 or 500.")
            else:
                balance -= amount
                print(f"Withdrawal successful. New balance: ${balance:.2f}")
        elif option == '3':
            deposit = float(input("Enter deposit amount: $"))
            balance += deposit
            print(f"Deposit successful. New balance: ${balance:.2f}")
        else:
            print("Invalid option.")

    elif choice == '3':
        # Task 3: Compound Interest
        print("\n--- Compound Interest Calculation ---")
        customers = int(input("Enter number of customers: "))
        for i in range(customers):
            print(f"\nCustomer {i+1}")
            principal = float(input("Enter initial balance: $"))
            rate = float(input("Enter annual interest rate (%): "))
            years = int(input("Enter number of years: "))
            future_balance = principal * ((1 + rate/100) ** years)
            print(f"Future balance after {years} years: ${future_balance:.2f}")

    elif choice == '4':
        # Task 4: Account Validation and Balance Check
        print("\n--- Account Balance Check ---")
        while True:
            acc = input("Enter your account number: ")
            if acc in accounts:
                print(f"Your account balance is: ${accounts[acc]:.2f}")
                break
            else:
                print("Invalid account number. Try again.")

    elif choice == '5':
        # Task 5: Password Validation
        print("\n--- Password Validation ---")
        password = input("Create your bank account password: ")

        if len(password) < 8:
            print("Password must be at least 8 characters long.")
        elif not re.search(r'[A-Z]', password):
            print("Password must contain at least one uppercase letter.")
        elif not re.search(r'\d', password):
            print("Password must contain at least one digit.")
        else:
            print("Password is valid!")

    elif choice == '6':
        # Task 6: Transaction History
        print("\n--- Transaction History Recorder ---")
        transactions = []

        while True:
            txn = input("Enter transaction (deposit/withdraw amount) or 'exit' to finish: ").strip().lower()
            if txn == 'exit':
                break
            elif txn.startswith('deposit') or txn.startswith('withdraw'):
                transactions.append(txn)
            else:
                print("Invalid transaction format. Try again.")

        print("\nTransaction History:")
        for i, t in enumerate(transactions, 1):
            print(f"{i}. {t.capitalize()}")

    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
