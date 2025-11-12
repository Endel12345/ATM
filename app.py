# operations
operations = (
    "1. Balance\n",
    "2. Withdraw\n",
    "3. Deposite\n",
    "4. Transfer\n",
    "5. History\n",
    "6. Logout"
)

# accounts_table 
accounts = {
    12345:'6789',
    12346:'6788'
            }


# user_details table 
user_details = {
    12345: ["codegnan",1000, "Codegnan@codegnan.com"],
    12346: ['Destination', 2000,'Destination@codegnan']

}

# login function
def login(user_name:int, password:str):
    # checking user_name present in accounts table or not
    if user_name in accounts:
        if accounts[user_name] == password:
            print("Successfully logedin to Codegnan Online Netbanking")
            return True
        else:
            print("Check your user credencialts")
    else:
        print("User not Found")
    return False


# opearions functions creation 
# balence function creartion 
def balence(user_name:int):
    # check user is present in users table
    if user_name in user_details:
        amount = user_details[user_name][1]
        print(f"Current balence is {amount}")
    # user is not in users table
    else:
        print("User not Found")
    

# withdraw function creation
def withdraw(user_name: int, withdraw_amount: int):
     # check user is present in users table
    if user_name in user_details:
        amount = user_details[user_name][1]
        if withdraw_amount <= amount:
            user_details[user_name][1] -= withdraw_amount
            print(f"Successfully withdraw your amount {withdraw_amount}")
            print(f"Current Balence is {user_details[user_name][1]}")
        else:
            print("Insufficent Amount in your account")
    
    # user is not in users table
    else:
        print("User not Found")


# deposite function defination
def deposite(user_name:int, deposite_amount:int):
     # check user is present in users table
    if user_name in user_details:
        user_details[user_name][1] += deposite_amount
        print(f"Current balence is {user_details[user_name][1]}")
    # user is not in users table
    else:
        print("User not Found")

# Transfer function defination
def transfer(user_name:int, to_account: int, transfer_amount: int):
    if user_name in user_details:
        if to_account in user_details:
            amount = user_details[user_name][1]
            if transfer_amount <= amount:
                user_details[user_name][1] -= transfer_amount
                user_details[to_account][1] += transfer_amount 
                print(f"Current Balence is {user_details[user_name][1]}")
            else:
                print(f"Insufficent Amount in {user_name}")
        else:
            print(f"{to_account} user not Found")
    else:
        print(f"{user_name} user not Found")


# mini statement function 
def history(user_name: int):
    print("Development under processing....")


# logout function defination 
def logout():
    print("User successfully logout")
    exit()
    pass




# main function 
if __name__ == "__main__":
    print("Welcome to the Codegnan Online net banking app")
    account = int(input("Please enter your account number: "))
    password = input("Please enter your password: ")
    if login(user_name= account, password=password):
        while True:
            print(*operations)
            choice = int(input("Please select your operation:"))

            if choice == 1:
                balence(user_name=account)

            elif choice == 2:
                amount = int(input("Please enter your withdraw amount: "))
                withdraw(user_name=account, withdraw_amount=amount)

            elif choice == 3:
                amount = int(input("Please enter your deposite amount: "))
                deposite(user_name=account, deposite_amount= amount)

            elif choice == 4:
                reciver_account = int(input("Please enter your recivier account number: "))
                amount = int(input("Please enter your transfer amount: "))
                transfer(user_name= account, to_account=reciver_account , transfer_amount=amount)

            elif choice == 5:
                history(user_name= account)
            
            elif choice == 6:
                logout()
            else:
                print("Please enter between 1-6")