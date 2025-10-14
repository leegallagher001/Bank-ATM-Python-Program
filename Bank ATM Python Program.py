# Bank ATM Program - by Lee Gallagher

# This program is designed to replicate the experience of using an ATM that has the ability to allow the user to both withdraw and deposit cash

# (1) Opening Statements

pin_number = 1234

print("Welcome to Redstone Bank!")
print("\n")
entered_pin = int(input("Please Enter Your PIN: "))  # to keep things simple, the initial PIN is 1234
print("\n")

# (2) Validate PIN

if entered_pin == pin_number:
    print("Hello, Dear Customer. Please choose which service you would like today from the following options below: ")
    print("\n")
    print("1. Check Balance")
    print("2. Cash Withdrawal")
    print("3. Cash Deposit")
    print("4. Change PIN")
    print("5. Exit ATM")
    print("\n")
else:
    print("Invalid PIN.")
    input("Press 'ENTER' to exit the program.")

# (3) Define Initial Variable Values & Functions

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
    print("\n")
    verify_current_pin = int(input("Enter Your Current PIN: "))
    if verify_current_pin == pin_number:
        pin_number = int(input("Enter A New PIN Number: "))

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

print("\n")
print("Thanks for using the Redstone Bank ATM!")
print("\n")
print("Press 'ENTER' to exit the program.")

