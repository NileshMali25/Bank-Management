import streamlit as st
from bank import Bank

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="centered"
)

bank = Bank()

st.title("🏦 Bank Management System")
st.markdown("---")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create Account",
        "Deposit",
        "Withdraw",
        "Account Details",
        "Update Details",
        "Change PIN",
        "Transaction History",
        "Delete Account"
    ]
)

# ---------------- CREATE ACCOUNT ----------------

if menu == "Create Account":

    st.header("Create New Account")

    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create Account"):

        success, message = bank.create_account(
            name,
            age,
            email,
            pin
        )

        if success:
            st.success("Account Created Successfully")
            st.info(f"Your Account Number : {message}")

        else:
            st.error(message)

# ---------------- DEPOSIT ----------------

elif menu == "Deposit":

    st.header("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):

        success, message = bank.deposit(
            acc,
            pin,
            amount
        )

        if success:
            st.success("Money Deposited Successfully")
            st.write("Current Balance : ₹", message)

        else:
            st.error(message)

# ---------------- WITHDRAW ----------------

elif menu == "Withdraw":

    st.header("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):

        success, message = bank.withdraw(
            acc,
            pin,
            amount
        )

        if success:
            st.success("Money Withdrawn Successfully")
            st.write("Current Balance : ₹", message)

        else:
            st.error(message)

# ---------------- DETAILS ----------------

elif menu == "Account Details":

    st.header("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show Details"):

        success, account = bank.get_details(acc, pin)

        if success:

            st.subheader("Account Information")

            st.write("**Account Number:**", account["account_no"])
            st.write("**Name:**", account["name"])
            st.write("**Age:**", account["age"])
            st.write("**Email:**", account["email"])
            st.write("**Balance:** ₹", account["balance"])

        else:
            st.error(account)

# ---------------- UPDATE ----------------

elif menu == "Update Details":

    st.header("Update Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    new_name = st.text_input("New Name")
    new_email = st.text_input("New Email")

    if st.button("Update"):

        success, message = bank.update_details(
            acc,
            pin,
            new_name,
            new_email
        )

        if success:
            st.success(message)

        else:
            st.error(message)

# ---------------- CHANGE PIN ----------------

elif menu == "Change PIN":

    st.header("Change PIN")

    acc = st.text_input("Account Number")
    old_pin = st.text_input("Old PIN", type="password")
    new_pin = st.text_input("New PIN", type="password")

    if st.button("Change PIN"):

        success, message = bank.change_pin(
            acc,
            old_pin,
            new_pin
        )

        if success:
            st.success(message)

        else:
            st.error(message)

# ---------------- HISTORY ----------------

elif menu == "Transaction History":

    st.header("Transaction History")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show History"):

        history = bank.get_transactions(
            acc,
            pin
        )

        if history:

            st.success("Transactions")

            for item in history:
                st.write("•", item)

        else:
            st.warning("No Transactions Found")

# ---------------- DELETE ----------------

elif menu == "Delete Account":

    st.header("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    st.warning("This action cannot be undone.")

    if st.button("Delete Account"):

        success, message = bank.delete_account(
            acc,
            pin
        )

        if success:
            st.success(message)

        else:
            st.error(message)