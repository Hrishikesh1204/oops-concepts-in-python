class account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc
        def debit(self,amount):
            self.bal-=amount
            print("Rs.",amount,"was debited")
        def credit(self,amount):
            self.bal+=amount
            print("Rs.",amount,"was credited")
        def get_bal(self):
            return self.bal