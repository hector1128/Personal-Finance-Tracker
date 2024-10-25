import time

def sec(x):
    return time.sleep(x)

def user_info(username):
    try:            
        print("Let's get some personal info so we can build the right tracker for YOU!")
        budget = int(input("How much money do you have?\n"))
        income = int(input("How much do you earn weekly?\n"))
        groceries=int(input("How much do you usually spend on groceries?\n"))
        transportation = int(input("How much do you spend weekly on your car/transportation?\n"))
        housing=int(input("How much do you usually spend on housing?\n"))
        bigpayments=int(input("Do you have any big payments coming up?\n"))
        extra=int(input("Do you spend any extra money apart from what is stated here? If not, type \"0\"\n"))
        
        db = open("personalinfo.txt", "a")
        db.write(f"{username}, {budget}, {income}, {groceries}, {transportation}, {housing}, {bigpayments}, {extra}\n")
        db.close()
    except SyntaxError:
        print("Input numbers only.")
        user_info(username)


def home():
    print("**PERSONAL FINANCE TRACKER**\n")

    sec(1)

    print("*----------ENTER USERNAME BELOW-----------*")

    sec(3)

    print("If you don't have an acccount, type \"new\" to sign up.")

    sec(1)

    print("If you wish to update your information type \"update\".\n")

    username=input()

    try:    
        if username =="new":
            def register():
                db = open("logindatabase.txt", "r")
                print("WELCOME TO PFT v1\n")
                name = input("Create a username: ")
                pw = input("Create a password: ")
                pw2 = input("Re-enter your password: ")
                u = []
                p = []
                
                for line in db:
                    if line.strip():
                        a,b=line.split(", ")
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
                elif name in u:
                    print("Username already exists. Choose another one.")
                    register()
                else:
                    db.close()
                    db=open("logindatabase.txt", "a")
                    db.write(name + ", " + pw + "\n")
                    db.close()
                    print(f"Sign up successful. Welcome {name}")
                    sec(3)
                    user_info(name)
                    print("You will now be redirected to the home page.")
                    sec(3)
                    home()

            register()
        
        if username=="update":
            pass

        db = open("logindatabase.txt", "r")
        users = db.readlines()
        db.close()
        for line in users:
            if line.strip():
                user, pw = line.strip().split(", ")
                if username==user:
                    def access():
                        entered_pw = input("P: ")
                        if entered_pw == pw:
                            print(f"WELCOME BACK {username}!")
                        else:
                            print("Password incorrect. Try again.")
                            access()
                    access()
                    break

        
            
    except SyntaxError:
        print("Invalid character. Run the program again and use valid characters.")

    

home()










