import time

def sec(x):
    return time.sleep(x)

#-----------------------------------------------------------------------------GETTING USER INFO(2)-------------------------------------------------------------------------
def user_info(username):
    try:            
        print("Let's get some personal info so we can build the right tracker for YOU!")
        budget = int(input("How much money do you have?\n"))
        income = int(input("How much do you earn weekly?\n"))
        groceries=int(input("How much do you usually spend on groceries?\n"))
        transportation = int(input("How much do you spend weekly on your car/transportation?\n"))
        housing=int(input("How much do you usually spend on housing?\n"))
        bigpayment=int(input("Do you have any big payments coming up?\n"))
        extra=int(input("Do you spend any extra money apart from what is stated here? If not, type \"0\"\n"))
        
        db = open("personalinfo.txt", "a")
        db.write(f"username: {username}, budget: {budget}, income: {income}, groceries: {groceries}, transportation: {transportation}, housing: {housing}, bigpayment: {bigpayment}, extra: {extra}\n")
        db.close()
    except SyntaxError:
        print("Input numbers only.")
        user_info(username)

#--------------------------------------------------------------------------------HOME FUNCTION(1)--------------------------------------------------------------------------
def home():
    print("**PERSONAL FINANCE TRACKER**\n")

    sec(1)

    print("*----------ENTER USERNAME BELOW-----------*")

    sec(3)

    print("If you don't have an acccount, type **\"new\"** to sign up.")

    sec(1)

    print("If you wish to update your information type **\"update\"**.\n")

    username=input("U: ")

    sec(3)

    try:    
        if username =="new":
#---------------------------------------------------------------------------------REGISTER FUNCTION(1A)---------------------------------------------------------------------           
            def register():
                db = open("logindatabase.txt", "r")
                print("*----------------------WELCOME TO PFT v1----------------------*\n")

                sec(3)

                name = input("Create a username: ")

                sec(1)

                pw = input("Create a password: ")

                sec(1)

                pw2 = input("Re-enter your password: ")

                sec(1)

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
                    sec(1)
                    register()
                elif pw != pw2:
                    print("passwords do not match, try again.")
                    sec(1)
                    register()
                elif name in u:
                    print("Username already exists. Choose another one.")
                    sec(1)
                    register()
                else:
                    db.close()
                    db=open("logindatabase.txt", "a")
                    db.write(name + ", " + pw + "\n")
                    db.close()
                    print(f"Sign up successful. Welcome {name}")
                    sec(3)
                    user_info(name)
                    sec(3)
                    print("Thank you! You will now be redirected to the home page.")
                    sec(3)
                    home()

            register()
        
#-------------------------------------------------------------------------UPDATE FUNCTION(1B)--------------------------------------------------------------------------------
        if username=="update":
            def update():
                username=input("What's your username??\n") 
                db = open("personalinfo.txt", "r")
                lines=db.readlines()
                db.close()
                info = {}
                infoinfiles=lines[:]
   
                def updateinfo():
                    newinfo=input("What do you want to change?\n") 
                    if newinfo in info:
                        try:
                            updatevalue=int(input(f"Enter your new {newinfo}. (Type a number)\n"))
                            info[newinfo]=updatevalue
                            inputvalue=""
                            inputvalue=", ".join(f"{key}: {value}" for key, value in info.items())
                            for i, line in enumerate(infoinfiles):
                                if username in line:
                                    infoinfiles[i]=inputvalue+"\n"
                                    break
                            db=open("personalinfo.txt", "w")
                            for line in infoinfiles:
                                db.write(line)
                            db.close()
                        except:
                            print("Make sure to input a number ONLY.")
                            updateinfo() 

                    else:
                        print("Invalid entry. Make sure you type one of the following:")
                        print("budget, income, groceries, transportation, housing, bigpayment, extra")
                        updateinfo()
                checkforuser=True
                for line in lines:
                    line = line.strip()
                    entries = line.split(", ")
                    for entry in entries:
                        key, value=entry.split(": ")
                        info[key.strip()]=value.strip()

        
                    for key, value in info.items():
                        if value == username:
                            checkforuser = False
                            print("Here's your current information:")
                            for key, value in info.items():
                                print(f"{key}: {value}")
                            updateinfo()
                            break
                if checkforuser:        
                    print("username not found. Re-type it correctly.")
                    print("If you would like to create an account, type \"create\" to sign-up. Otherwise, click Enter to try again.")
                    backhome=input()
                    if backhome=="create":
                        register()
                    update()                        
                    info.clear()

            update()
            
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

        db = open("logindatabase.txt", "r")
        users = db.readlines()
        db.close()
        usercheck=True
        for line in users:
            if line.strip():
                user, pw = line.strip().split(", ")
                if username==user:
                    usercheck = False
                    def access():
                        entered_pw = input("P: ")
                        if entered_pw == pw:
                            print(f"*----------------------------Welcome back {username}!---------------------------------*")
                            sec(3)
                        else:
                            print("Password incorrect. Try again.")
                            sec(1)
                            access()
                    access()
                    break
        if usercheck:
            print("Username not found. Try again.")
            home()

        
            
    except SyntaxError:
        print("Invalid character. Run the program again and use valid characters.")

    

home()










