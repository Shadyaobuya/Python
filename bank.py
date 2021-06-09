from datetime import datetime
class Account():
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transaction_fee=200
        self.loan=0
        self.loan_limit=50000
        self.loan_fees=0.5
        self.transactions=[]

    def deposit(self,amount):
        if amount<=0:
           return "Enter a valid amount"
        else:
            self.balance+=amount
            transaction={
                "amount":amount,
                "balance":self.balance,
                "narration":"You deposited",
                "time":datetime.now()
            }
            self.transactions.append(transaction)
            
            return "Hello {} you have deposited {}. New balance is {} ".format(self.name,amount,self.balance)

    #Amount must be greater than 0
    # Amount must be greater than balance
    def withdraw(self,amount):
        total_rate=amount+self.transaction_fee
        if amount<=0:
            return "You cannot withdraw 0 or less"
        elif total_rate>self.balance:
            return "Your balance must cover amount to be withdrawn and the transaction fees"
        else:
            self.balance-=total_rate
            transaction={
                "amount":amount,
                "balance":self.balance,
                "narration":"You withdrew",
                "time":datetime.now()
            }
            self.transactions.append(transaction)
            return "Hello {} you have withdrawn {}. New balance is {} ".format(self.name,amount,self.balance)
    
    def borrow(self,amount):
        loan_rate=amount * self.loan_fees
        payable_amount=loan_rate + amount
        if amount>self.loan_limit:
            return "Amount to be borrowed has to be less than the loan limit"
        elif self.loan!=0:
            return "You need to have a loan balance of zero before being given another"
        elif amount<=0:
            return "Ask for a valid Loan"
        else:
            self.loan+=payable_amount
            self.balance+=amount
            transaction={
                "amount":amount,
                "balance":self.balance,
                "narration":"Took a loan",
                "time":datetime.now()
            }
            self.transactions.append(transaction)

            return "You have successfully qualified for {} ksh Loan . Your new bank account balance is {}. You will be required to pay {} KSH. Interest is {}".format(amount,self.balance,payable_amount,loan_rate)

    def repay(self,amount):
        if amount<=0:
            return "Enter valid amount"
        elif amount>self.loan:
            excess_amount=amount-self.loan
            self.balance+=excess_amount
            transaction={
                "amount":amount,
                "balance":self.balance,
                "narration":"You repaid",
                "time":datetime.now()
            }
            self.transactions.append(transaction)
            return "you have paid {} in excess. It has been added to your account".format(excess_amount)
        else:
            self.loan-=amount
            transaction={
                "amount":amount,
                "balance":self.balance,
                "narration":"You repaid",
                "time":datetime.now()
            }
            self.transactions.append(transaction)
            return "you have paid {}. outstanding loan balance is {}".format(amount,self.loan)

    def statement(self):
        for transaction in self.transactions:
            amount=transaction['amount']
            narration=transaction['narration']
            balance=transaction['balance']
            time=transaction['time']
            date=time.strftime('%D')
        
            print('''{}.......{}.......{}.....Balance {}'''.format(date,narration,amount,balance,))

        


    


   