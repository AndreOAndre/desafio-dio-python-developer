menu = """

[D] deposit
[W] withdraw 
[S] statement
[Q] quit

=> """

balance = 0
limit = 500
statement = ""
withdraw_number = 0
LIMIT_WITHDRAW = 3


while True:

    option = input(menu).strip().upper()

    if option == "D":
        value = float(input("Enter the deposit amount: "))

        if value > 0:
            balance += value
            statement += f"Deposit: {value:.2f}\n"

        else:
            print("Operational Error! Invalid value.")
    

    elif option == "W":
        value = float(input("Enter the withdraw amount: "))

        exceeded_balance = value > balance
        exceeded_limit = value > limit
        exceeded_withdraw = withdraw_number >= LIMIT_WITHDRAW

        if exceeded_balance:
            print("Balance exceeded. You don't have enough balance.")

        elif exceeded_limit:
            print(f"Limit exceeded. your limit is R$ {limit:.2f}")
        
        elif exceeded_withdraw:
            print("withdraw limit exceeded! Wait for renewal.")

        elif value > 0:
            balance -= value
            statement += f"Withdraw: R$ {value:.2f}\n"
            withdraw_number += 1
        
        else:
            print("Operational error! invalid value.")
        

    elif option == "S":
        print("\n================ STATEMENT ================")
        print("No bank transaction." if statement == "" else statement)
        print(f"\nBalance: R$ {balance:.2f}")
        print("==========================================")
    

    elif option == "Q":
        break
        

    else:
        print("Invalid operation! Select the desired operation again.")