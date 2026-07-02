from database import load_data, save_data
from utils import generate_account_number


class Bank:

    def __init__(self):
        self.accounts = load_data()

    def save(self):
        save_data(self.accounts)

    def create_account(self, name, age, email, pin):

        if age < 18:
            return False, "Age must be 18 or above."

        if len(pin) != 4 or not pin.isdigit():
            return False, "PIN must contain exactly 4 digits."

        existing = [i["account_no"] for i in self.accounts]

        account_no = generate_account_number(existing)

        account = {
            "account_no": account_no,
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "balance": 0,
            "transactions": []
        }

        self.accounts.append(account)

        self.save()

        return True, account_no

    def login(self, account_no, pin):

        for account in self.accounts:

            if account["account_no"] == account_no and account["pin"] == pin:

                return account

        return None

    def deposit(self, account_no, pin, amount):

        account = self.login(account_no, pin)

        if account is None:
            return False, "Invalid account."

        if amount <= 0:
            return False, "Invalid amount."

        account["balance"] += amount

        account["transactions"].append(
            f"Deposited ₹{amount}"
        )

        self.save()

        return True, account["balance"]

    def withdraw(self, account_no, pin, amount):

        account = self.login(account_no, pin)

        if account is None:
            return False, "Invalid account."

        if amount <= 0:
            return False, "Invalid amount."

        if amount > account["balance"]:
            return False, "Insufficient Balance."

        account["balance"] -= amount

        account["transactions"].append(
            f"Withdraw ₹{amount}"
        )

        self.save()

        return True, account["balance"]

    def get_details(self, account_no, pin):

        account = self.login(account_no, pin)

        if account:

            return True, account

        return False, "Invalid Account."

    def update_details(self, account_no, pin, name, email):

        account = self.login(account_no, pin)

        if account is None:
            return False, "Invalid Account"

        account["name"] = name
        account["email"] = email

        self.save()

        return True, "Updated Successfully"

    def change_pin(self, account_no, old_pin, new_pin):

        account = self.login(account_no, old_pin)

        if account is None:
            return False, "Invalid Account"

        if len(new_pin) != 4:

            return False, "PIN must be 4 digits"

        account["pin"] = new_pin

        self.save()

        return True, "PIN Updated"

    def delete_account(self, account_no, pin):

        account = self.login(account_no, pin)

        if account is None:
            return False, "Invalid Account"

        self.accounts.remove(account)

        self.save()

        return True, "Account Deleted"

    def get_transactions(self, account_no, pin):

        account = self.login(account_no, pin)

        if account:

            return account["transactions"]

        return []