from main.bank import Bank
from decimal import Decimal
from exception.invalid_account_exception import InvalidAccountException

def main():
    bank = Bank()

    while True:
        print("\nBANK SYSTEM MENU")
        print("1. Create Account")
        print("2. Perform Bank Transactions")
        print("3. Check Loan Eligibility")
        print("4. Calculate Compound Interest")
        print("5. View Account Details")
        print("6. Create Password ")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nCreate New Account")
            print("1. Savings Account")
            print("2. Current Account")
            acc_type = input("Choose account type : ")

            if acc_type in ["1", "2"]:
                print("\nEnter Customer Details")
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                dob = input("Date of Birth (YYYY-MM-DD): ")
                email = input("Email: ")
                phone = input("Phone Number: ")
                address = input("Address: ")

                customer= bank.find_or_create_customer(first_name, last_name, dob, email, phone, address)
                if customer:
                    print(f"\nCustomer ID: {customer.get_customer_id()}")

                    balance = Decimal(input("Initial Deposit Amount: "))
                    account_type = "Savings" if acc_type == "1" else "Current"

                    if account_type == "Savings":
                        interest_rate = float(input("Enter Interest Rate (%): "))
                    else:
                        interest_rate = None

                    account_number = bank.create_account(customer, balance, account_type,interest_rate)
                    print(f"{account_type} Account created with Account Number: {account_number}")

                else:
                    print("Please create a new customer first with valid details.")

            else:
                print("Invalid account type selected.")

        elif choice == "2":
            print("\nBank Transactions")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Calculate Interest (Savings Only)")
            print("6. View Transaction History")
            transaction_choice = input("Choose a transaction: ")

            if transaction_choice == "1":
                while True:
                    try:
                        acc_num = int(input("Enter account number: "))
                        bank.check_balance(acc_num)
                        break

                    except ValueError as ve:
                        print("Enter a valid account number!The account number you have entered is invalid. Please try again.")

                    except InvalidAccountException as e:
                        print("Enter a valid account number!The account number you have entered is invalid. Please try again.")

            elif transaction_choice == "2":
                acc_num = int(input("Enter Account Number: "))
                amount = Decimal(input("Enter deposit amount: "))
                bank.deposit(acc_num, amount)

            elif transaction_choice == "3":
                acc_num = int(input("Enter Account Number: "))
                amount = Decimal(input("Enter withdrawal amount: "))
                try:
                    bank.withdraw(acc_num, amount)
                except InvalidAccountException as e:
                    print(e)

            elif transaction_choice == "4":
                from_acc_num = int(input("Enter Account Number to transfer from: "))
                to_acc_num = int(input("Enter Account Number to transfer to: "))
                amount = Decimal(input("Enter transfer amount: "))
                bank.transfer(from_acc_num, to_acc_num, amount)

            elif transaction_choice == "5":
                acc_num = int(input("Enter Account Number: "))
                bank.calculate_interest(acc_num)

            elif transaction_choice == "6":
                acc_num = int(input("Enter Account Number: "))
                bank.show_transaction_history(acc_num)

            else:
                print(" Invalid transaction choice!")

        elif choice == "3":
            bank.check_loan_eligibility()

        elif choice == "4":
            num_customers = int(input("Enter the number of customers: "))

            for i in range(1, num_customers + 1):
                print(f"\nCustomer {i}:")

                initial_balance = float(input("Enter initial balance: "))
                annual_interest_rate = float(input("Enter annual interest rate (in %): "))
                years = int(input("Enter number of years: "))

                future_balance = bank.calculate_compound_interest(initial_balance,annual_interest_rate,years)

                print(f"Future balance after {years} years: ₹{future_balance:.2f}")

        elif choice == "5":
            acc_num = int(input("Enter Account Number: "))
            bank.print_account_details(acc_num)

        elif choice == "6":
            acc_num =int(input("Enter Account number: "))
            password=input("Enter Password: ")
            res=bank.is_valid_password(password,acc_num)
            if res==True:
                print("Password is valid")
            elif res==False:
                print("Password is invalid")

        elif choice == "7":
            print("Exiting Banking System. Thank you!")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
