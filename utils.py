import random
import string


def generate_account_number(existing_accounts):

    while True:

        account = ''.join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=10
            )
        )

        if account not in existing_accounts:
            return account