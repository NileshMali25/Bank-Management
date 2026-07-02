# 🏦 Bank Management System

A modern **Bank Management System** built using **Python** and **Streamlit**. This project allows users to create bank accounts, deposit and withdraw money, update account details, view account information, and delete accounts. Account data is stored in a JSON file for simplicity.

---

## 🚀 Features

- ✅ Create a New Bank Account
- 💰 Deposit Money
- 💸 Withdraw Money
- 👤 View Account Details
- ✏️ Update Account Information
- 🔒 Change Account PIN
- 🗑️ Delete Account
- 📜 View Transaction History
- 💾 JSON-based Data Storage
- 🌐 Interactive Streamlit Web Interface

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit**
- **JSON**
- **Object-Oriented Programming (OOP)**

---

## 📂 Project Structure

```
Bank-Management/
│── app.py              # Streamlit frontend
│── bank.py             # Banking operations
│── database.py         # JSON read/write functions
│── utils.py            # Helper functions
│── data.json           # Database
│── requirements.txt    # Project dependencies
│── README.md           # Project documentation
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/Bank-Management.git
```

### 2. Go to the Project Directory

```bash
cd Bank-Management
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Console Version

```bash
python main.py
```

The console version provides a menu-driven banking system that runs in the terminal.


### 4. Run the streamlit Application

```bash
streamlit run app.py
```

If the `streamlit` command is not recognized, use:

```bash
python -m streamlit run app.py
```

---

## 📸 Application Features

### 🏦 Create Account

- Enter Name
- Age
- Email
- 4-digit PIN
- Automatically generates a unique Account Number

### 💰 Deposit Money

Deposit money into an existing account.

### 💸 Withdraw Money

Withdraw money after verifying the account number and PIN.

### 👤 Account Details

View account information, including:

- Account Number
- Name
- Email
- Balance

### ✏️ Update Details

Update account name and email.

### 🔒 Change PIN

Change your existing 4-digit PIN securely.

### 🗑️ Delete Account

Delete an account permanently after verification.

### 📜 Transaction History

View all deposit and withdrawal transactions.

---

## 📷 Screenshots

You can add screenshots of the application here.

Example:

```
screenshots/
│── home.png
│── create_account.png
│── deposit.png
```

---


⭐ If you found this project helpful, don't forget to **Star** the repository!
