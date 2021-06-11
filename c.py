from bank import MobileMoneyAccount


phone=MobileMoneyAccount("Shadya","083247635","Safaricom")
print(phone.deposit(1000))

print(phone.buy_airtime(70))
phone.statement()