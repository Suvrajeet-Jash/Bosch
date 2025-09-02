from datetime import datetime, timedelta

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount:.2f} to {self.account_number}. New balance: {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        print(f"Withdrew {amount:.2f} from {self.account_number}. New balance: {self.balance:.2f}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number}] - Holder: {self.account_holder}, Balance: {self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest of {interest:.2f} applied. New balance: {self.balance:.2f}")

    def __str__(self):
        return f"SavingsAccount[{self.account_number}] - Holder: {self.account_holder}, Balance: {self.balance:.2f}, Interest Rate: {self.interest_rate}%"


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, overdraft_limit, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Withdrawal amount exceeds overdraft limit.")
        self.balance -= amount
        print(f"Withdrew {amount:.2f} from {self.account_number}. New balance: {self.balance:.2f}")

    def __str__(self):
        return f"CurrentAccount[{self.account_number}] - Holder: {self.account_holder}, Balance: {self.balance:.2f}, Overdraft Limit: {self.overdraft_limit:.2f}"


class FixedDepositAccount(BankAccount):
    def __init__(self, account_number, account_holder, lock_in_period_days, interest_rate, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.lock_in_period = timedelta(days=lock_in_period_days)
        self.interest_rate = interest_rate
        self.start_date = datetime.now()

    def withdraw(self, amount):
        if datetime.now() < self.start_date + self.lock_in_period:
            raise ValueError(f"Funds are locked until {(self.start_date + self.lock_in_period).date()}. Withdrawal not allowed.")
        super().withdraw(amount)

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest of {interest:.2f} applied to Fixed Deposit Account. New balance: {self.balance:.2f}")

    def __str__(self):
        lock_until = self.start_date + self.lock_in_period
        return (f"FixedDepositAccount[{self.account_number}] - Holder: {self.account_holder}, Balance: {self.balance:.2f}, "
                f"Interest Rate: {self.interest_rate}%, Locked Until: {lock_until.date()}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        if account.account_number in self.accounts:
            raise ValueError(f"Account number {account.account_number} already exists.")
        self.accounts[account.account_number] = account
        print(f"Account {account.account_number} added to {self.name}.")

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError(f"Account {account_number} not found.")
        return self.accounts[account_number]

    def transfer_funds(self, from_acc_num, to_acc_num, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        from_acc = self.get_account(from_acc_num)
        to_acc = self.get_account(to_acc_num)
        try:
            from_acc.withdraw(amount)
            to_acc.deposit(amount)
            print(f"Transferred {amount:.2f} from {from_acc_num} to {to_acc_num}.")
        except ValueError as e:
            print(f"Transfer failed: {e}")

    def __str__(self):
        return f"Bank: {self.name}, Accounts: {len(self.accounts)}"


# Test program
def main():
    print("=== Bank System Test ===")

    bank = Bank("MyBank")

    # Creating accounts
    savings = SavingsAccount("SA123", "Suvrajeet", interest_rate=3.5, balance=1000)
    current = CurrentAccount("CA456", "Dheeraj", overdraft_limit=500, balance=500)
    fixed_deposit = FixedDepositAccount("FD789", "Nithin", lock_in_period_days=30, interest_rate=5, balance=2000)

    # Adding accounts to bank
    bank.add_account(savings)
    bank.add_account(current)
    bank.add_account(fixed_deposit)

    print("\n-- Initial Account States --")
    print(savings)
    print(current)
    print(fixed_deposit)

    # Performing deposits
    print("\n-- Deposits --")
    savings.deposit(500)
    current.deposit(300)
    try:
        fixed_deposit.deposit(100)  
    except Exception as e:
        print(e)

    # Performing withdrawals
    print("\n-- Withdrawals --")
    try:
        savings.withdraw(200)
    except Exception as e:
        print(e)

    try:
        current.withdraw(900) 
    except Exception as e:
        print(e)

    try:
        fixed_deposit.withdraw(100)  
    except Exception as e:
        print(f"Fixed Deposit Withdrawal Error: {e}")

    # Applying interest on savings
    print("\n-- Applying Interest on Savings --")
    savings.apply_interest()

    # Applying interest on fixed deposit
    print("\n-- Applying Interest on Fixed Deposit --")
    fixed_deposit.apply_interest()

    # Transferring funds
    print("\n-- Transfer Funds --")
    bank.transfer_funds("SA123", "CA456", 300)

    # Showing final balances
    print("\n-- Final Account States --")
    for acc in bank.accounts.values():
        print(acc)

if __name__ == "__main__":
    main()
