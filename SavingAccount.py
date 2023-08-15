from BankAccount import BankAccount
class SavingAccount(BankAccount):
    def DepoistAmount(self, amount):
        if(amount<=0):
            print("For Depoist : Enter Amount must be greater than 0")
            print()
        else:
            interest=(amount)*0.03
            super().DepoistAmount(amount+interest)
            print("Interest :",interest)
            print("Amount Deposit :",amount)
            print("Total Amount added in Saving Account:",amount+interest)
            print()
    