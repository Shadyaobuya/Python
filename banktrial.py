from datetime import datetime
class Account:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transactions=[]

    def deposit(self,amount):
        try:
            amount+10
        except:
            return "Enter amount in figures"
        if amount<=0:
            return "Enter valid input"
        else:
            self.balance+=amount
            transaction={
                'date':datetime.today(),
                'narration':"You deposited",
                'amount':amount,
                'balance':self.balance
                }
            self.transactions.append(transaction)
            return "Hello, you have deposited {} shillings. Your balance is {} {}".format(amount,self.balance,self.transactions)

    def get_statement(self):
        for trans in self.transactions:
            cdate= trans['date']
            tdate=cdate.strftime('%x')
            narration=trans['narration']
            balance=trans['balance']
            amount=trans['amount']
        print('''
    {}...........{}........{}........Balance {}
    '''.format(tdate,narration,amount,balance))
            


acc=Account("Shadya","0789888")
print(acc.deposit(1000))
acc.get_statement()