## Task One - ATM Transaction System

print (" Welcome to UBA Banking  ")
pin = (input("create your 4 digit ATM Pin for all transaction "))

option = (input("Select Option: Check Balance, Withdraw Money, Deposit Money "))

operation= input(" Are you sure you want to carry out an operation ?  Yes/No   ")

if operation == "Yes":
    reenter_pin=input("Re-enter your pin  ")
    if reenter_pin == pin:
        ##print(option = input("Select Option: Check Balance, Withdraw Money, Deposit Money "))
        print("You are about to ", option)
        if option == "Check Balance":
            print ("Your Available Balance is $5000")

        elif option == ("Withdraw Money"):
           Amount = int((input("Enter an Amout for withdrawal  ")))

        elif option == ("Deposit Money"):
            print(int((input("Enter an Amount" ))))
            print ("New Balance = $", count + 5000)
        

    elif reenter_pin != pin:
        print (input( "Pin Incorrect!!! Please try again "))

    elif reenter_pin != pin:
            print (input( "Pin Incorrect!!! You have One Trial Left "))

    elif reenter_pin != pin:
        print (input( "Please contact Customer Support ! Thanks"))


else:
    print ("You can chill and drink hot beer ! ")







    
























