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
    def update(cls):
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    def create_account(self):
        data={
            "name":input("Enter your name:"),
            "age":int(input("Enter your age:")),
            "email":input("Enter your email:"),
            "pin":input("Enter your pin:"),
            "account_No":''.join(random.choices(string.digits,k=10)),
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
            Bank.update()





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

