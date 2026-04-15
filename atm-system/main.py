acc_balance = 1000
correct_pin = 3075
max_attempts = 3
attempts_left = max_attempts
transactions = []

while attempts_left > 0:
    entered_pin = int(input("Enter the PIN: "))
    
    if correct_pin == entered_pin:
        while True:
            print("\n1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. View Transactions")
            print("5. Exit")
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
                    transactions.append("Withdraw: " + str(amt_to_withdraw))
            
            elif choice == "2":
                print("How much money you want to deposit?")
                amt_to_deposit = int(input("Enter amount to deposit: "))
                
                if amt_to_deposit <= 0:
                    print("Invalid amount!")
                else:
                    acc_balance = acc_balance + amt_to_deposit
                    print("You have deposited " + str(amt_to_deposit))
                    print("Your new balance is: " + str(acc_balance))
                    transactions.append("Deposit: " + str(amt_to_deposit))
            
            elif choice == "3":
                print("Your Balance is " + str(acc_balance))
            
            elif choice == "4":
                print("Transaction History:")
                for transaction in transactions:
                    print(transaction)
            
            elif choice == "5":
                print("Thank you for using ATM!")
                break   
            
            else:
                print("Invalid option. Try again.")
        
        break   
    
    else:
        attempts_left = attempts_left - 1
        if attempts_left > 0:
            print("Wrong PIN. You have " + str(attempts_left) + " attempts left.")
        else:
            print("Card Blocked. Contact your Bank.")