print("**PERSONAL FINANCE TRACKER**")

print("ENTER USERNAME BELOW")
print("If you don't have an acccount, type \"new\" to sign up.")
print("If you wish to update your information type \"update\".\n")
username=input()
try:
    if username =="new":
        print("WELCOME TO PFT v1\n")
        budget = int(input("How much money do you have?\n"))
        income = int(input("How much do you earn weekly?\n"))
        groceries=int(input("How much do you usually spend on groceries?\n"))
        transportation = int(input("How much do you spend weekly on your car/transportation?\n"))
        housing=int(input("How much do you usually spend on housing?\n"))
        bigpayments=int(input("Do you have any big payments coming up?\n"))
        extra=int(input("Do you spend any extra money apart from what is stated here? If not, type \"0\""))
        
    if True:# Username exists:
        print("WELCOME BACK")

        print('TOTAL BUDGET')

        print('ratio between spendatures and income')

        print("Max amnt of money users should spend per week")

    if username=="update":
        pass
except SyntaxError:
    print("Invalid character. Run the program again and use valid characters.")

except:
    print("Oops. Something went wrong. Try again.")


# Classes ----------------------------------------------------------------------
class User:
    def __init__(self, budget, income, groceries, eatingout, housing, bigpayments, extra==0):
        self.budget=budget
        self.income=income
        self.groceries=groceries
        self.eatingout=eatingout
        self.housing=housing
        self.bigpayments=bigpayments
        self.extra=extra








