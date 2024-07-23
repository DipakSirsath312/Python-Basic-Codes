class Account:
    def __init__(self,bal):
        print("--------------------------")
        name = str(input("Enter Youe Name:-"))
        acc_no = int(input("Please Enter Account No:-"))
        self.account_no = acc_no
        self.balance = bal
        print("Your Balance:-",self.balance)

    def debit(self,ammount):
        print("---------------------------")
        self.balance -= ammount
        print("Rs.",ammount,"Was Debited")
        print("Total Balance:-",self.balance)

    def credit(self,ammount):
        print("---------------------------")
        self.balance += ammount
        print("Rs.",ammount,"Was Credited")
        print("Total Balance:-",self.balance)

    def get_balance(self):
        return self.balance
        
acc1 = Account(10000)
acc1.debit(5000)
acc1.credit(1000)