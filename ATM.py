

class ATM():
    serial_number = 0
    
    def deposit (self , account, amount):
        account. current_balance = account.current_balance + amount
        print("Deposit Complete")
    def widthdraw(self, account, amount):
        account. current_balance = account.current_balance - amount
        print("Widthdraw Complete")
    def check_currentbalance(self, account):
        print(account.current_balance)
        