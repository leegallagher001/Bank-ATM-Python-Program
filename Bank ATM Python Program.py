# Bank ATM Program - by Lee Gallagher

# This program is designed to replicate the experience of using an ATM that has the ability to allow the user to both withdraw and deposit cash

# Copious amount of (probably quite obvious) comments, as once again I'm new to using JSON with Python and I really need them!

# (0) Imports & JSON File (For Storing Current PIN)
import json

pin_file = "pin_number.json" # imported JSON file

# (1) Define Initial Functions & Variable Values

balance = 500

def checkBalance():
    global balance # need to give variable global scope to use it in multiple functions
    print("\n")
    print("Current Balance: \xa3", balance) # \xa3 = "£" sign

def cashWithdrawal():
    global balance
    print("\n")
    print("Both \xa310 and \xa320 notes are available.")
    print("\n")
    withdraw_amount = int(input("How much would you like to withdraw?: "))
    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print("\n")
        print("Successfully withdrawn \xa3", withdraw_amount, ". You have \xa3", balance, " remaining.")
    else:
        print("\n")
        print("Insufficient funds for transaction.")

def cashDeposit():
    global balance
    print("\n")
    deposit_amount = int(input("How much would you like to deposit?: "))
    balance += deposit_amount
    print("Successfully deposited \xa3", deposit_amount, ". You have \xa3", balance, " remaining.")

def changePIN():

    global pin_number

    verify_current_pin = int(input("Please enter your current PIN number: "))

    if verify_current_pin == (pin_number["pin"]):
        with open(pin_file, 'r') as f:
            pin_number = json.load(f)
            new_pin = int(input("Please enter a new PIN: "))
            pin_number["pin"] = new_pin

        with open(pin_file, 'w') as f:
            json.dump(pin_number, f, indent=4)
        print("PIN successfully changed!")

    else:
        print("Invalid PIN - please try another time.")

# (2) Opening Statements

print("Welcome to Redstone Bank!")
print("\n")

with open(pin_file, 'r') as f:
    pin_number = json.load(f)

if not pin_number:
    pin = int(input("Please enter a new PIN number: ")) # appears if no PIN number stored in JSON file

    pin_number = {
        "pin": pin
    }

    with open(pin_file, 'w') as f:
        json.dump(pin_number, f, indent=4)

else:

    enter_pin = int(input("Please enter your PIN number: ")) # appears if PIN number already present in JSON file

    with open(pin_file, 'r') as f:
        pin_number = json.load(f)
    if enter_pin == (pin_number["pin"]):

# (3) Validate PIN

        print("Hello, Dear Customer. Please choose which service you would like today from the following options below: ")
        print("\n")
        print("1. Check Balance")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Exit ATM")
        print("\n")

# (4) Activate Menu (Call Functionality)

        menuChoice = int(input("Which Option Do You Choose?: "))

        while menuChoice != 5:
            if menuChoice == 1:
                checkBalance()
                print("\n")
                menuChoice = int(input("Looking for something else? Choose another menu option: "))
            elif menuChoice == 2:
                cashWithdrawal()
                print("\n")
                menuChoice = int(input("Looking for something else? Choose another menu option: "))
            elif menuChoice == 3:
                cashDeposit()
                print("\n")
                menuChoice = int(input("Looking for something else? Choose another menu option: "))
            elif menuChoice == 4:
                changePIN()
                print("\n")
                menuChoice = int(input("Looking for something else? Choose another menu option: "))
            else:
                print("Invalid Input")
                print("\n")
                menuChoice = int(input("Looking for something else? Choose another menu option: "))

    else: # Invalid PIN, ends program after pressing 'enter'
        print("Invalid PIN.")
        input("Press 'ENTER' to exit the program.")
        exit()

print("\n")
print("Thanks for using the Redstone Bank ATM!")
print("\n")
input("Press 'ENTER' to exit the program.")
exit()

