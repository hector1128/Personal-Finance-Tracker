import time

def sec(x):
    return time.sleep(x)

def access(username, pw):
    entered_pw = input("P: ")
    if entered_pw == pw:
        sec(2)
        print(f"*----------------------------------------------------Welcome back {username}!------------------------------------------------------------*")
        sec(3)
    else:
        print("Password incorrect. Try again.")
        sec(1)
        access(username, pw)

#-------------------------------------------------------------------------UPDATE FUNCTION(1B)--------------------------------------------------------------------------------

def update():
    username=input("What's your username??\n")
    sec(3) 
    db = open("personalinfo.txt", "r")
    lines=db.readlines()
    db.close()
    info = {}
    infoinfiles=lines[:]
    founduser=False
    checkforuser=True
    # Checking each line in file
    for line in lines:
        # Removes white space of line
        line = line.strip()
        # Then splits each entry into a list based on ", " into ['username: input', 'budget: input']
        entries = line.split(", ")
        # Looping through the list "entries"
        for entry in entries:
            # Splitting each value into username hector.cordero income 200
            key, value=entry.split(": ")
            # Looping through 
            for items in entry:
                # Saving the items in the file as a dictionary (JSON) format
                info[key.strip()]=value.strip()

        # Looping through info of file in dictionary (JSON) format
        for key, value in info.items():
            # If the input from the user matches any value in the username 
            if value == username:
                checkforuser = False
                print("Here's your current information:")
                sec(1)
                for key, value in info.items():
                    print(f"{key}: {value}")
                updateinfo(username, infoinfiles, info)
                break

    if checkforuser:        
        print("username not found. Re-type it correctly.")
        print("If you would like to create an account, type \"create\" to sign-up. Otherwise, click Enter to try again.")
        sec(3)
        backhome=input()
        if backhome=="create":
            home()
        else:
            update()                        
        info.clear()

def updateinfo(info, infoinfiles, username):
    newinfo=input("What do you want to change?\n") 
    sec(3)
    if newinfo in info:
        try:
            updatevalue=int(input(f"Enter your new {newinfo} info. (Type a number)\n"))
            sec(3)
            if newinfo == "hoursworked":
                income = int(info["income"])/int(info["hoursworked"])
                weeklyearnings = round(income*updatevalue)
                info["income"]=weeklyearnings
            info[newinfo]=updatevalue
            inputvalue=", ".join(f"{key}: {value}" for key, value in info.items())
            for i, line in enumerate(infoinfiles):
                if username in line:
                    infoinfiles[i]=inputvalue+"\n"
                    break
            db=open("personalinfo.txt", "w")
            for line in infoinfiles:
                db.write(line)
            db.close()
            sec(2)
            print("Here's your updated information:\n")
            sec(2)
            for key, value in info.items():
                print(f"{key}: {value}")
            addinfo = input("Would you like to add anything else? If so, type \"add\". Otherwise, click \"Enter\" to go back home.\n")
            addinfo.lower()
            if addinfo=="add":
                updateinfo(username, info, infoinfiles)
            else:
                print("Thank you! You will now be redirected to the home page.")
                sec(2)
                home()


        except ValueError:
            print("Make sure to input a number ONLY.")
            sec(1)
            updateinfo(username, info, infoinfiles) 

    else:
        print("Invalid entry. Make sure you type one of the following:")
        print("budget, income, hoursworked, groceries, transportation, housing, bigpayment, extra")
        sec(3)
        updateinfo(username, info, infoinfiles)

    

#---------------------------------------------------------------------------------REGISTER FUNCTION(1A)---------------------------------------------------------------------

def register():
    db = open("logindatabase.txt", "r")
    print("*---------------------------------------------------------------------WELCOME TO PFT v1----------------------------------------------------------------------*\n")

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
        print(f"Sign up successful. Welcome {name}!")
        sec(3)
        user_info(name)
        sec(3)
        print("Thank you! You will now be redirected to the home page.")
        sec(3)
        home()

#-----------------------------------------------------------------------------GETTING USER INFO(2)-------------------------------------------------------------------------

def user_info(username):
    try:            
        print("Let's get some personal info so we can build the right tracker for YOU!")
        sec(2)
        print("**NOTE: INPUT A NUMBER ONLY**")
        sec(1)
        budget = int(input("How much do you have in checkings? (DOES NOT INCLUDE YOUR SAVINGS)\n"))
        sec(1)
        income = int(input("How much do you earn per hour?\n"))
        sec(1)
        hoursworked = int(input("And how many hours do you work per week?\n"))
        income*=hoursworked
        sec(1)
        groceries=int(input("How much do you usually spend on groceries?\n"))
        sec(1)
        transportation = int(input("How much do you spend weekly on your car/transportation?\n"))
        sec(1)
        housing=int(input("How much do you usually spend on housing monthly?\n"))
        sec(1)
        bigpayment=int(input("Do you have a big payment coming up? If so, state the due as a number. Otherwise, type \"0\"\n"))
        sec(1)
        extra=int(input("Do you spend any extra money weekly apart from what is stated here? If so, state the due as a number. Otherwise, type \"0\"\n"))
        
        db = open("personalinfo.txt", "a")
        db.write(f"username: {username}, budget: {budget}, income: {income}, hoursworked: {hoursworked}, groceries: {groceries}, transportation: {transportation}, housing: {housing}, bigpayment: {bigpayment}, extra: {extra}\n")
        db.close()
    except ValueError:
        print("Input numbers only.")
        user_info(username)

#--------------------------------------------------------------------------------HOME FUNCTION(1)--------------------------------------------------------------------------

def home():
    founduser=False
    print("**----------------------------------------------------------PERSONAL FINANCE TRACKER**-----------------------------------------------------------------------**\n")

    sec(3)

    print("If you don't have an acccount, type **\"new\"** to sign up.")

    sec(1)

    print("If you wish to update your information type **\"update\"**.\n")

    sec(1)

    print("*----------ENTER USERNAME BELOW-----------*")

    username=input("U: ")

    sec(3)

    try:    
        if username =="new":
            register()
        
        if username=="update":
            update()
            
        db = open("logindatabase.txt", "r")
        users = db.readlines()
        db.close()
        
        for line in users:
            if line.strip():
                user, pw = line.strip().split(", ")
                if username==user:
                    founduser=True
                    access(username, pw)
                    break
        if not founduser:
            print("Username not found. Try again.")
            sec(2)
            home()
    except SyntaxError:
        print("Invalid character. Run the program again and use valid characters.")

home()
