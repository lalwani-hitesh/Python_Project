from BankAccount import BankAccount
class CurrentAccount(BankAccount):
    def WithdrawAmount(self, amount):
        if(self.getCurrentBalance()>0 and self.getCurrentBalance()>=amount+200):
            charge=200
            super().WithdrawAmount(amount+charge)
            print("Interest Charged:",charge)
            print(amount," Withdraw from the Current Account")
            print("Total Amount deduced from Current Account :",amount + charge)
            print()
        else:
            print("Do not have sufficient balance for withdraw in Current Account")
            print()
    
    