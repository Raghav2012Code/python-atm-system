acc_balance = 1000

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
    print("Hope you had a great time with our service! See you later!")