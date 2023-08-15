
class BankAccount:
    __CurrentBalance=0
    

    #Constructor to add the initial amount
    def __init__(self,amount):
        if(amount<=0):
            print("Enter Amount must be greater than 0")
            print()
        else:
            self.__CurrentBalance=amount
            print("Initial Amount added :",self.__CurrentBalance)
            print()

    #Getter Method to get the Current Balance
    def getCurrentBalance(self):
        return self.__CurrentBalance
    
    #Setter Method to set the Current Balance Value
    def setCurrentBalance(self,amount):
        self.__CurrentBalance=amount


    #Method to depoist amount in the user account
    def DepoistAmount(self,amount):
        if(amount<=0):
            print("For Depoist : Enter Amount must be greater than 0")
            print()
        else:
            self.__CurrentBalance+=amount
            print(amount," Deposited in the Account")
            print()

    #Method to Withdraw amount from the User
    def WithdrawAmount(self,amount):
        if(self.__CurrentBalance>0 and self.__CurrentBalance>=amount):
            self.__CurrentBalance-=amount
            print(amount," Withdraw from the Account")
            print()
        else:
            print("Do not have sufficient balance for withdraw")
            print()

    #Method to Transfer fund from one account to another
    def TransferFund(self,OtherBankkAccount,amount):
        if(0<amount<=self.__CurrentBalance):
            self.WithdrawAmount(amount)
            OtherBankkAccount.DepoistAmount(amount)
        else:
            print("Do not have Enough Funds for transfer")
            print()


        
        

        
