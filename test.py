budget = int(input("How much money do you have?\n"))
income = int(input("How much do you earn weekly?\n"))
groceries=int(input("How much do you usually spend on groceries?\n"))
transportation = int(input("How much do you spend weekly on your car/transportation?\n"))
housing=int(input("How much do you usually spend on housing?\n"))
bigpayments=int(input("Do you have any big payments coming up?\n"))
extra=int(input("Do you spend any extra money apart from what is stated here? If not, type \"0\""))

class User:
    def __init__(self, budget, income, groceries, transportation, housing, bigpayments, extra=0):
        self.budget=budget
        self.income=income
        self.groceries=groceries
        self.transportation=transportation
        self.housing=housing
        self.bigpayments=bigpayments
        self.extra=extra

user1=User(budget, income, groceries, transportation, housing, bigpayments, extra)

print(user1.budget)