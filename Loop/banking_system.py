# ATM Simulation using loops

balance = 5000  # initial balance
chances = 3     # number of attempts to enter correct PIN

# PIN verification using while loop
while chances > 0:
    pin = input("Enter your 4-digit PIN: ")
    if pin == "1234":
        print("PIN accepted. Welcome!")
        # Main menu using a loop
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                print("Your balance is:", balance)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                if amount <= balance:
                    balance -= amount
                    print(f"{amount} withdrawn successfully.")
                    print("Remaining balance:", balance)
                else:
                    print("Insufficient balance.")
            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                balance += amount
                print(f"{amount} deposited successfully.")
                print("New balance:", balance)
            elif choice == "4":
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
        break
    else:
        chances -= 1
        print(f"Wrong PIN. {chances} attempt(s) left.")

if chances == 0:
    print("Your account is locked due to too many failed attempts.")
