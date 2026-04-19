class ContaBancaria:
    def __init__(self, account_id, account_name, account_balance):
        self.account_id = int(account_id)
        self.account_name = str(account_name)
        self.account_balance = account_balance

    def withdrawal(self, value): 
        if value >= self.account_balance:
            print("Error! You will be in debit")
        else:
            self.account_balance = self.account_balance - value


    def deposit(self, value):
        self.account_balance = self.account_balance +  value

    def showAccount(self):
        print(f"ID da conta: {self.account_id}\nNome do titular: {self.account_name}\nSaldo da conta: {self.account_balance}")
    
conta = ContaBancaria(1234, "Kauan", 50)
conta.withdrawal(51)
conta.showAccount()
