print("**PERSONAL FINANCE TRACKER**")

print("ENTER USERNAME BELOW")
print("If you don't have an acccount, type \"new\" to sign up.")
username=input()

if username =="new":
    print("WELCOME TO PFT v1\n")
    budget = int(input("How much do you ha?\n"))
    income = int(input("How much do you earn weekly?\n"))
    groceries=int(input("How much do you usually spend on groceries?\n"))
    eatingout = int(input("How much do you earn weekly?\n"))
    housing=int(input("How much do you usually spend on housing?\n"))
    extra=int(input("Do you spend any extra money apart from what is stated here? If not, type \"n\""))

elif True:# Username exists:
    print('TOTAL BUDGET')

    print('How much i should spend per week')


# Classes ----------------------------------------------------------------------
class User:
    def __init__(self, budget, income, groceries, eatingout, housing, extra==0):
        self.budget=budget
        self.income=income
        self.groceries=groceries
        self.eatingout=eatingout
        self.housing=housing
        self.extra=extra








