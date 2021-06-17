from banktrial import MobileMoneyAccount


phone=MobileMoneyAccount("Shadya","083247635","Safaricom")
print(phone.deposit(1000))

print(phone.buy_airtime(70))
print(phone.withdraw(100))
phone.statement()