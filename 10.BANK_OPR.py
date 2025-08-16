#wap create bank,deposit,withdraw,ministaement

class bank():
    bank_name="bank of india"
    address="namakkal"
    print(f"welcome to {bank_name} {address}".center(100,"*"))
    def __init__(self,name,age,pan,location):
        self.name=name
        self.age=age
        self.pan=pan
        self.location=location
        self.amount=0.0
        print("your account successfully created!!!!")
        print("thanks for choosing bank of india")
    def deposit(self,amount):
        self.amount=self.amount+amount
        print(f"your {amount} successfully deposited")
    def withdraw(self,amount):
        if amount<=self.amount:
            self.amount=self.amount-amount
            print(f"your {amount} successfully withdrawn")
        else:
            print("your account has insuffient funds")
            print(f"your acount balance is {self.amount}")
    def ministatement(self):
        print(f"your account balance is: {self.amount}")
       
name=input("enter your name:: ".strip())
age=int(input("enter your age:: "))
pan=input("enter your pan details:: ".strip())
location=input("enter your location:: ".strip())

bank_obj=bank(name,age,pan,location)

while True:
    print("please choos below option")
    print("1.Deposit\n2.withdraw\n3.ministatement\n4.stop")
    choice=int(input("enter your option:: "))
    if choice==1:
        amount=float(input("enter your amount:: "))
        bank_obj.deposit(amount)
    elif choice==2: 
        amount=float(input("enter your amount:: "))
        bank_obj.withdraw(amount)
    elif choice==3:
        bank_obj.ministatement()
    else:
        print(f"thanks for using {bank.bank_name}")
        break





    





