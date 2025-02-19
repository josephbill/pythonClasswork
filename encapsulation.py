class Bankaccount:
    def __init__(self, balance):
        self.__balance = balance  ## the two underscores -> encapsulaltion

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account1 = Bankaccount(10000)
print(account1.get_balance())
# even in encapsulation our objects can still add new properties
account1.balance = 000
print(account1.balance)