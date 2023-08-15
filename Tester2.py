from BankAccount import BankAccount
from SavingAccount import SavingAccount
from CurrentAccount import CurrentAccount

print("Welcome to Bank Operations")
print()

print("Saving Account")
print()

s1=SavingAccount(2000)
s1.DepoistAmount(500)

print("Current Account")
print()

c1=CurrentAccount(2000)
c1.DepoistAmount(500)
c1.WithdrawAmount(100)

c1.TransferFund(s1,500)

print("Current Balance of Saving Account :",s1.getCurrentBalance())

print("Current Balance of Current Account:",c1.getCurrentBalance())