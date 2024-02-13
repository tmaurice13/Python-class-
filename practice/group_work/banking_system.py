Bal=0
def deposit():
    global balance
    balance += amount
    print("Deposit ${}.Current balance: ${}".format(amount, balance))
def withdraw(amount):
    global balance
    if amount <= balance:
        balance-=amount
        print("withdraw ${}.Current balance: ${}".format(amoun,balance))
    else:
        print("Insufficient funds.")
    checkbalance()
def withdraw (amount):
    Bal=Bal-amount
    checkbalance()
def checkbalance():
    print("current balance: ",Bal) 
# options
print("1.Create account\n2.withdraw\n 3.Deposit\n4.Check balance")
choice=input("Select any option")
if(choice==1):
   Accounts()
elif(choice==2):
    amount=int(input("Enter amount to withdraw: "))
    withdraw(amount)
elif(choice==3):
    amount=int(input("enter amount to deposit: "))
    Deposit(amount)
elif(choice==4):
    checkbalance()
