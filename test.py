class Account:
    def __init__(self, owner, balances=0):
        self.owner = owner
        self.balances = balances

    def __str__(self):
        return f"Account Owner: {self.owner}, Balance: {self.balances}"

    def deopsit(self, amount):
        self.balances = self.balances + amount
        print("The deposit is accepted!")

    def withdrawal(self, amount):
        if self.balances - amount <0:
            print("You do not have enough funds")
        else:
            self.balances = self.balances - amount
            print("Withdraw is completed!")

    

acct1 = Account('Jose', 100)
print(acct1)

acct1.deopsit(50)
print(acct1)

acct1.withdrawal(200)
print(acct1) 