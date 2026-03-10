# ||\ bouns task /||
FLOW_CHART = """ 
Start
  │
  ▼
Prompt: Enter Username
  │
  ▼
Is Username in Users?
  ├─ No → Print "Username not found" → Go back to Start
  │
  └─ Yes → Prompt: Enter PIN
           │
           ▼
        Is PIN correct?
           ├─ No → Print "Wrong PIN" → Retry PIN or EXIT
           │
           └─ Yes → Display Menu:
                     1. Check Balance
                     2. Withdraw
                     3. Deposit
                     4. Transaction History
                     5. Exit
                     6. flow chart
                     │
                     ▼
                User selects option
                     │
                     ▼
              ┌─────────────┬─────────────┬─────────────┬─────────────┬───────────┐
              │             │             │             │             │           │
          Option 1      Option 2      Option 3      Option 4      Option 5      Option 6
              │             │             │             │             │           │         
      Call Check_Balance  Call Withdraw  Call Deposit  Show History  Exit Menu   FLOW_CHART  
              │             │             │             │             │             │
              ▼             ▼             ▼             ▼             ▼             ▼
           Back to Menu → Back to Menu → Back to Menu → Back to Menu  → End   ← Back to Menu"""
  # ||| task TWO |||
#-##### account holders #####-#
class EYAD:
    Money = 100 # account holder balance
    History = []  # empty LIST to (record Deposit Withdraw etc..) 

class TARIQ:
    Money = 999999 
    History = []

class MOHAMMAD:
    Money = 100
    History = []
   # using dict to make the ATM more flexible put every user aginst his PIN 
Users = {
    "EYAD": {"class": EYAD, "pin": "Eyad1234"}, 
    "TARIQ": {"class": TARIQ, "pin": "Tariq1234"},
    "MOHAMMAD": {"class": MOHAMMAD, "pin": "Mo1234"},
}
# ||| task THREE |||
def Check_Balance(user_class): # define a funtion to checking the account holder Balance
    print("\nYour Total Balance is:", user_class.Money) # using /n for make the output organized
    input("Type Enter to go back...")

def Withdraw(user_class): # define a funtion for Withdraw 
    while True:
        #Makes sure the input is an Integer and nothing else
        try: # define a VAR [TakenMoney] to know how much the withdraw amount 
            TakenMoney = int(input("\nEnter the amount to withdraw (or 0 to Exit): ")) 
        except ValueError: # if the account holder put a value not an Integer like [words, float etc ...]
            print("Invalid input. Please enter an Integer")
            continue
        
        if TakenMoney == 0: # if the account holder write ZERO its will back to the menu
            break
        if TakenMoney < 0:  # if there NGE value input , its will be ignored and ask the user to input again
            continue
        if TakenMoney > user_class.Money: # if there not enough balance, the user will get a message
            print("You don't have enough balance!")
            continue # askes the account holder to input again

        user_class.Money -= TakenMoney # sub the input value to done the Withdrew easily
        user_class.History.append(f"Withdrew {TakenMoney}, Balance: {user_class.Money}") 
        print("You withdrew:", TakenMoney, "Remaining balance:", user_class.Money)
        break # show off the NOW balance , and update the History

def Deposit(user_class): # define another funtion to Deposit progress
    while True:
        #Makes sure the input is an Integer and nothing else
        try: # define a VAR [AddedMoney] to know how much the deposit amount 
            AddedMoney = int(input("\nEnter the amount to deposit (or 0 to Exit): "))
        except ValueError: # if the account holder put a value not an Integer like [words, float etc ...]
            print("Invalid input. Please enter an Integer")
            continue # askes the account holder to rewrite the value 
        if AddedMoney < 0: # NO NEG again
            continue
        if AddedMoney == 0:  # if the account holder write ZERO its will back to the menu
            break

        user_class.Money += AddedMoney # Add the value to the Balance 
        user_class.History.append(f"Deposited {AddedMoney}, Balance: {user_class.Money}")  
        print("You deposited:", AddedMoney, "New balance:", user_class.Money) 
        break # tell the account holder the input value and update NOW balance 

def Transaction_History(user_class): # define a funtion to do the Trans things e.g. >
    print("\nTransaction History:") 
    if not user_class.History: # if there is not any transactions History its just will print that <
        print("No transactions yet.")
    else:
        for action in user_class.History: # show off the transactions 
            print("-", action)
    input("Type Enter to go back...") # to back to the menu



 # ||| task ONE |||
while True:
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓       🪙  WELCOME TO ATM 🪙         ▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    User_name = input("Enter Username: ").upper()
    #Username and PIN Checks
    if User_name in Users:
        while True:
            User_PIN = input("Enter PIN (or type EXIT to go back): ")

            if User_PIN.upper() == "EXIT":
                break

            if User_PIN == Users[User_name]["pin"]:
                print("Hello, Welcome Back", User_name)
                account = Users[User_name]["class"]

                while True:
                    print("\n1: Check Balance\n2: Withdraw\n3: Deposit\n4: Transaction History\n5: Exit\n6: ATM flow chart")
                    try:
                        Choice = int(input("Enter Number: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue

                    match Choice:
                        case 1: Check_Balance(account)
                        case 2: Withdraw(account)
                        case 3: Deposit(account)
                        case 4: Transaction_History(account)
                        case 5: break
                        case 6: print(FLOW_CHART)
                        case _: print("This option is not available")
                break
            else:
                print("Wrong PIN try again. Type EXIT to exit out of the menu")
    else:
        print("Username not found, please try again.")
        continue