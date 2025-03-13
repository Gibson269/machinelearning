print("Welcome to UBA Banking")

# Create PIN
pin = input("Create your 4-digit ATM PIN for all transactions: ")

# Check if the PIN is exactly 4 digits
if len(pin) != 4 or not pin.isdigit():
    print("Invalid PIN! It must be exactly 4 digits.")
else:
    balance = 5000  # Initial account balance
    attempts = 3  # Allowed PIN attempts

    while attempts > 0:
        re_entered_pin = input("Re-enter your PIN to proceed: ")

        if re_entered_pin == pin:
            print("Login successful!")
            option = input("Select Option: Check Balance, Withdraw Money, Deposit Money: ")

            if option == "Check Balance":
                print("Your Available Balance is $", balance)

            elif option == "Withdraw Money":
                withdrawal_amount = int(input("Enter an amount for withdrawal: "))
                if withdrawal_amount > balance:
                    print("Insufficient Funds!")
                else:
                    balance -= withdrawal_amount
                    print("Withdrawal successful! New Balance: $", balance)

            elif option == "Deposit Money":
                deposit_amount = int(input("Enter an amount to deposit: "))
                balance += deposit_amount
                print("Deposit successful! New Balance: $", balance)

            else:
                print("Invalid option selected!")

            break  # Exit the loop after a successful transaction

        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect PIN! You have {attempts} attempt(s) left.")
            else:
                print("PIN incorrect! Your account is locked. Please contact Customer Support.")

print("Thank you for banking with UBA!")