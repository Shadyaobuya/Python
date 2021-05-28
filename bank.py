class Bank():
    def __init__(self,account_number,account_name,balance):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=balance
       
    def deposit(self,amount):
        self.balance+=amount
        return "Account Number {} made a deposit of {}. New balance is {} ".format(self.account_number,amount,self.balance)
    def withdraw(self,amount):
        return "Account Name: {} made a withdrawal of {} ".format(self.account_name,amount)
    def get_details(self):
        return "Account Number: {}, Account name: {}, Account Balance: {}".format(self.account_number,self.account_name,self.balance)


