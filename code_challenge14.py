# Simple Bank Simulation Program

def display_currency_breakdown(amount):
    print("\nBills breakdown for PHP", amount)
    bills = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    for bill in bills:
        if amount >= bill:
            count = amount // bill
            print(f"{bill} x {count}")
            amount %= bill

def start_account():
    print("Welcome to the Bank!")
    name = input("Enter your full name: ")
    print(f"Account successfully created for {name}.")
    return name

def add_money(balance):
    amount = int(input("\nEnter the amount to deposit: "))
    display_currency_breakdown(amount)
    balance += amount
    print(f"Deposit completed! New balance: PHP {balance}")
    return balance

def remove_money(balance):
    amount = int(input("\nEnter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds! Cannot withdraw.")
    else:
        display_currency_breakdown(amount)
        balance -= amount
        print(f"Withdrawal completed! Remaining balance: PHP {balance}")
    return balance

def main():
    balance = 0
    name = start_account()
    
    # Initial deposit
    print("\nMake your initial deposit to activate the account.")
    balance = add_money(balance)
    
    while True:
        print("\nOptions Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        option = input("Select an option: ")
        
        if option == "1":
            balance = add_money(balance)
        elif option == "2":
            balance = remove_money(balance)
        elif option == "3":  
            # Simplified "Check Balance" option
            print(f"Your current balance is: PHP {balance}")
        elif option == "4":
            print(f"Thank you for banking with us, {name}!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()