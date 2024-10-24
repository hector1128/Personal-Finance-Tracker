import time

def sec(x):
    return time.sleep(x)


# The user's information
class User:
    def __init__(self, budget, income, groceries, transportation, housing, bigpayments, extra=0):
        self.budget=budget
        self.income=income
        self.groceries=groceries
        self.transportation=transportation
        self.housing=housing
        self.bigpayments=bigpayments
        self.extra=extra
    def ratio(self):
        pass

# Each transaction
class Transaction:
    def __init__(self):
        pass



print("**PERSONAL FINANCE TRACKER**\n")

sec(1)

print("ENTER USERNAME BELOW")

print("If you don't have an acccount, type \"new\" to sign up.")

print("If you wish to update your information type \"update\".\n")

username=input()



try:
    db = open("logindatabase.txt", "r")
    
    if username in db:
        def access():
            pw = input("P: ")
            if pw in db:
                print("WELCOME BACK")

                print('TOTAL BUDGET')
            # print(name.budget)
                print('ratio between spendatures and income')

                print("Max amnt of money users should spend per week")
            else:
                print("Password incorrect. Try again.")
        access()
    db.close()
    
    if username =="new":
        def register():
            db = open("logindatabase.txt", "r")
            print("WELCOME TO PFT v1\n")
            name = input("Create a username: ")
            pw = input("Create a password: ")
            pw2 = input("Re-enter your password: ")
            u = []
            p = []
            for i in db:
                a,b=i.split(", ")
                b= b.strip()
                u.append(a)
                p.append(b)
            login = dict(zip(u, p))
            
            if len(pw)<6:
                print("Password is too short. Try again")
                register()
            elif pw != pw2:
                print("passwords do not match, try again.")
                register()
            elif name in db:
                print("Username already exists. Choose another one.")
                register()
            else:
                db=open("logindatabase.txt", "a")
                db.write(name + ", " + pw + "\n")
                print("Sign up successful.")
            db.close()
        register()
            
            #budget = int(input("How much money do you have?\n"))
            #income = int(input("How much do you earn weekly?\n"))
            #groceries=int(input("How much do you usually spend on groceries?\n"))
            #transportation = int(input("How much do you spend weekly on your car/transportation?\n"))
            #housing=int(input("How much do you usually spend on housing?\n"))
            #bigpayments=int(input("Do you have any big payments coming up?\n"))
            #extra=int(input("Do you spend any extra money apart from what is stated here? If not, type \"0\"\n"))
            #name=User(budget, income, groceries, transportation, housing, bigpayments, extra)
            # Save that info in a file ^^
        
    

    #while True:
        #if username=="update":
           # username = input("What is your username?\n")
        # If username in files:
            # Retrieve user
            
except SyntaxError:
    print("Invalid character. Run the program again and use valid characters.")

except:
    print("Oops. Something went wrong. Try again.")









