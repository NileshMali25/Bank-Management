import json
import random
import string
from pathlib import Path



class Bank:
    database='data.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data=json.loads(fs.read())
        else:
            print("no such file exists")

    except Exception as err:
        print(f"an exception occurred as {err}")
    
    @classmethod
    def __update(cls):
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices(string.punctuation,k=1)
        acc_id=alpha+num+spchar
        random.shuffle(acc_id)
        return ''.join(acc_id)

    def create_account(self):
        data={
            "name":input("Enter your name:"),
            "age":int(input("Enter your age:")),
            "email":input("Enter your email:"),
            "pin":int(input("Enter your pin:")),
            "account_No":Bank.__accountgenerate(),
            "balance":0
        }

        if data['age']<18 or len(str(data['pin']))!=4:
            print("Sorry you cannot create your account")

        else:
            print("account has been created successfully")
            for i in data:
                print(f"{i}:{data[i]}")
            print("Please note down your account number for future reference")

            Bank.data.append(data)
            Bank.__update()

    def deposit_money(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        found = False

        for i in Bank.data:
            if i['account_No'] == accnumber and i['pin'] == pin:

                amount = int(input("Please tell the amount you want to deposit: "))

                if amount > 10000 or amount < 0:
                    print("Sorry you cannot deposit more than 10000 or less than 0")
                else:
                    i['balance'] += amount
                    print(f"Your account has been credited with {amount}")
                    print(f"Current balance is {i['balance']}")
                    Bank.__update()

                found = True
                break

        if not found:
            print("Sorry, no account found. Please check your account number and PIN.")

    def withdraw_money(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        found = False

        for i in Bank.data:
            if i['account_No'] == accnumber and i['pin'] == pin:

                amount = int(input("Please tell the amount you want to withdraw: "))

                if  i['balance'] < amount:
                    print("Sorry you cannot withdraw more than your current balance")
                else:
                    i['balance'] -= amount
                    print("Amount Withdrawn successfully")
                    print(f"Your account has been debited with {amount}")
                    print(f"Current balance is {i['balance']}")
                    Bank.__update()

                found = True
                break

        if not found:
            print("Sorry, no account found. Please check your account number and PIN.")

    def show_details(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        found = False
        for i in Bank.data:
            if i['account_No'] == accnumber and i['pin'] == pin:
                print("Account Details:")
                for key, value in i.items():
                    print(f"{key}: {value}")
                found = True
                break
        if not found:
            print("Sorry, no account found. Please check your account number and PIN.")

    def update_details(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        found = False
        for i in Bank.data:
            if i['account_No'] == accnumber and i['pin'] == pin:
                print("What detail would you like to update?")
                print("1. Name")
                print("2. Pin")
                print("3. Email")
                choice = int(input("Enter your choice (1-3): "))

                if choice == 1:
                    new_name = input("Enter new name: ")
                    i['name'] = new_name
                elif choice == 2:
                    new_pin = int(input("Enter new pin: "))
                    i['pin'] = new_pin
                elif choice == 3:
                    new_email = input("Enter new email: ")
                    i['email'] = new_email
                else:
                    print("Invalid choice.")
                    return

                print("Details updated successfully.")
                Bank.__update()
                found = True
                break

        if not found:
            print("Sorry, no account found. Please check your account number and PIN.")

    def delete_account(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        found = False
        for i in Bank.data:
            if i['account_No'] == accnumber and i['pin'] == pin:
                Bank.data.remove(i)
                print("Account deleted successfully.")
                Bank.__update()
                found = True
                break

        if not found:
            print("Sorry, no account found. Please check your account number and PIN.")

user=Bank()
print("Press 1 for Creating an account")
print("Press 2 for Deposit the money in the bank")
print("Press 3 for Withdrawing the money")
print("Press 4 for Details")
print("Press 5 for Updating the details")
print("Press 6 for Deleting the account")

check=int(input("Tell your response:"))

if check==1:
    user.create_account()

if check==2:
    user.deposit_money()

if check==3:
    user.withdraw_money()

if check==4:
    user.show_details()

if check==5:
    user.update_details()

if check==6:
    user.delete_account()

else:
    print("Invalid choice. Please select a valid option.")