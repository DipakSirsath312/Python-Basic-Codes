class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # private attribute.

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account(9538238741,"Dipak@312")

print(acc1.acc_no)
acc1.reset_pass()