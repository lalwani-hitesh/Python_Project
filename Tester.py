from BankAccount import BankAccount
from SavingAccount import SavingAccount
from CurrentAccount import CurrentAccount

print("Welcome to Bank Operations")
print("--------------------------")

#Create 2 BankAccounts with initial Balance 500 and 200
b1=BankAccount(500)
b2=BankAccount(200)

#withdraw 200 from 1st BankAccount
b1.WithdrawAmount(200)

#deposit 1000 in 2nd bankAccount
b2.DepoistAmount(1000)

#transfer 500 from second to first Bank Account
b2.TransferFund(b1,500)

#Balance of Both Accounts
print("Current Balance of First Account :",b1.getCurrentBalance())
print("Current Balance of Second Account :",b2.getCurrentBalance())





