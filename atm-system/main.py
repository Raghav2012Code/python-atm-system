acc_balance = 1000
correct_pin = 3075
entered_pin = int(input("Enter the PIN: "))

if correct_pin == entered_pin:
    while True:
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")
        choice = input("Enter option: ")
        if choice == "1":
            print("Hi, how much money you want to withdraw?")
            amt_to_withdraw = int(input("Enter amount to withdraw: "))

            if amt_to_withdraw <= 0:
                print("Invalid amount.")

            elif amt_to_withdraw > acc_balance:
                print("Insufficient balance in the account")
                print("You only have " + str(acc_balance))

            else:
                acc_balance = acc_balance - amt_to_withdraw
                print("Withdrawal successful!")
                print("You have withdrawn rupees " + str(amt_to_withdraw))
                print("You have " + str(acc_balance) + " remaining in your account.")

        elif choice == "2":
            print("Your Balance is " + str(acc_balance))

        elif choice == "3":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid option. Try again.")
else:
    print("Wrong PIN, Goodbye!")