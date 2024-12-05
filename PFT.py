import time

import sys

from datetime import datetime

current_date = datetime.now()

current_month = current_date.strftime("%B")
def sec(x):
    return time.sleep(x)

def show_user_data(username):
    db = open("personalinfo.txt", "r")
    lines = db.readlines()
    db.close()
    userinfo = {}
    for line in lines:
        line.strip()
        info = line.split(", ")
        for item in info:
            item.strip()
            key, value = item.split(": ")
            userinfo[key] = value
        if userinfo["username"]==username:
            pass
        else:
            userinfo.clear()
    

def check_login(username):
    db = open("logindatabase.txt", "r")
    users = db.readlines()
    db.close()
    for line in users:
        user, pw = line.strip().split(", ")
        if username==user:
            password=pw
    entered_pw = input("P: ")
    try:
        if entered_pw == password:
            sec(2)
            print(f"*----------------------------------------------------Welcome back {username}!------------------------------------------------------------*\n")
        else:
            print("Password incorrect. Try again.")
            check_login(username)
    except NameError:
        print("Username not found. Try again")
        home()

#-------------------------------------------------------------------------UPDATE FUNCTION(1B)--------------------------------------------------------------------------------

def update():
    username = input("What's your username??\n")
    sec(2)
    db = open("personalinfo.txt", "r")
    lines = db.readlines()
    db.close()
    infoinfiles = lines[:]  # Copy file lines for potential updates
    founduser = False
    
    # Checking each line in file
    for line in lines:
        # Remove whitespace and split entries
        line = line.strip()
        entries = line.split(", ")
        info = {}  # Initialize for each user
        
        # Populate `info` dictionary for current user
        for entry in entries:
            key, value = entry.split(": ")
            info[key.strip()] = value.strip()
        
        # Check if username matches
        if info.get("username") == username:
            founduser = True
            print("Here's your current information:")
            sec(1)
            for key, value in info.items():
                print(f"{key}: {value}")
            updateinfo(info, infoinfiles, username)  # Pass correctly
            break

    if not founduser:
        print("Username not found. Re-type it correctly.")
        backhome = input("Type 'create' to sign-up or press Enter to try again.\n")
        if backhome.lower() == "create":
            home()
        else:
            update()

def updateinfo(info, infoinfiles, username):
    newinfo = input("What do you want to change?\n")
    sec(3)
    if newinfo == "bigpaymentdate":
        if info["bigpayment"]==0:
            sec(1)
            print("You have no payment due. Make sure you add a payment first before adding a date.")
            sec(1)
            update(info, infoinfiles, username)
    if newinfo in info:
        try:
            if newinfo == "bigpaymentdate":
                updatevalue = (input(f"Enter your new {newinfo}. (mm/dd/20xx)\n"))
                info[newinfo] = updatevalue
            else:
                updatevalue = int(input(f"Enter your new {newinfo} info. (Type a number)\n"))
                sec(3)
                if newinfo == "hoursworked":
                    income = int(info["income"]) / int(info["hoursworked"])
                    weeklyearnings = round(income * updatevalue)
                    info["income"] = str(weeklyearnings)
                info[newinfo] = str(updatevalue)
                
                if newinfo == "bigpayment":
                    info[newinfo]=str(updatevalue)
                    print("When is this big payment due?")
                    sec(2)
                    print("Type the date in the following format")
                    sec(2)
                    print("mm/dd/20xx")
                    bigpdate=input()
                    sec(1)
                    info["bigpaymentdate"]=str(bigpdate)   

            # Update file contents
            updated_entry = ", ".join(f"{k}: {v}" for k, v in info.items())
            for i, line in enumerate(infoinfiles):
                if f"username: {username}" in line:
                    infoinfiles[i] = updated_entry + "\n"
                    break
            
            with open("personalinfo.txt", "w") as db:
                db.writelines(infoinfiles)
                sec(1)
                
            sec(2)
            print("Here's your updated information:\n")
            sec(2)
            for key, value in info.items():
                print(f"{key}: {value}")
            print()
            sec(2)
            if input("Type 'add' to update more or press Enter to go back home.\n").lower() == "add":
                updateinfo(info, infoinfiles, username)
            else:
                print("Thank you! Redirecting to home.")
                sec(2)
                home()

        except ValueError:
            print("Make sure to input a number ONLY.")
            sec(1)
            updateinfo(info, infoinfiles, username)
    else:
        print("Invalid entry. Type one of the following: budget, savings, income, hoursworked, groceries, transportation, housing, bigpayment, bigpaymentdate, extra")
        sec(3)
        updateinfo(info, infoinfiles, username)


#---------------------------------------------------------------------------------REGISTER FUNCTION(1A)---------------------------------------------------------------------

def register():
    db = open("logindatabase.txt", "r")
    print("*---------------------------------------------------------------------WELCOME TO PFT v1----------------------------------------------------------------------*\n")

    sec(2)

    name = input("Create a username: ")

    if name.lower() == "exit":
        sys.exit(0)

    sec(1)

    pw = input("Create a password: ")

    if pw.lower() == "exit":
        sys.exit(0)

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
        sec(2)
        user_info(name)
        sec(2)
        print("Thank you! You will now be redirected to the home page.")
        sec(2)
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
        savings = int(input("How much do you have in savings? (401K, Roth IRA, Stocks included)\n"))
        sec(1)
        income = int(input("How much do you earn per hour?\n"))
        sec(1)
        hoursworked = int(input("And how many hours do you work per week?\n"))
        income*=hoursworked
        sec(1)
        insuranceamt = int(input("How many insurance plans do you currently hold? (Type as a number)\n"))
        if insuranceamt != 0:
            insurancetypes={}
            for insurance in range(insuranceamt):
                print(f"For your {insurance+1} insurance, what type of insurance is it?")
                instype = input()
                print("And how much do you pay for it??")
                instypeprice = input()
                insurancetypes[instype]=instypeprice
            insurances = ", ".join(f"{key}: {value}" for key, value in insurancetypes.items())
        sec(1)
        groceries=int(input("How much do you usually spend on groceries weekly?\n"))
        sec(1)
        transportation = int(input("How much do you usually spend on your car/transportation weekly?\n"))
        sec(1)
        housing=int(input("How much do you usually spend on housing monthly?\n"))
        sec(1)
        bigpayment=int(input("Do you have a big payment coming up? If so, state the due as a number. Otherwise, type \"0\"\n"))
        if bigpayment != 0:
            sec(1)
            print("When is this big payment due?")
            sec(2)
            print("Type the date in the following format")
            sec(2)
            print("mm/dd/20xx")
            bpdate=input()
            sec(1)   
        else:
            bpdate = "N/A" 
        sec(1)
        extra=int(input("Do you spend any extra money weekly apart from what is stated here? If so, state the due as a number. Otherwise, type \"0\"\n"))
        
        db = open("personalinfo.txt", "a")
        if insuranceamt != 0:
            db.write(f"username: {username}, budget: {budget}, savings: {savings}, income: {income}, hoursworked: {hoursworked}, {insurances}, groceries: {groceries}, transportation: {transportation}, housing: {housing}, bigpayment: {bigpayment}, bigpaymentdate: {bpdate}, extra: {extra}\n")
        else:
            db.write(f"username: {username}, budget: {budget}, savings: {savings}, income: {income}, hoursworked: {hoursworked}, groceries: {groceries}, transportation: {transportation}, housing: {housing}, bigpayment: {bigpayment}, bigpaymentdate: {bpdate}, extra: {extra}\n")
        db.close()
    except ValueError:
        print("Input numbers only.")
        user_info(username)

def check_user(username):
    db = open("logindatabase.txt", "r")
    users = db.readlines()
    db.close()
        
    for line in users:
        user, pw = line.strip().split(", ")
        if username==user:
            return pw
        else:
            return None
#--------------------------------------------------------------------------------HOME FUNCTION(1)--------------------------------------------------------------------------
addline_list = [" "]
def delete_line(username, cumexpenses, expenseslist, count):
    db = open("personalinfo.txt", "r")
    lines = db.readlines()
    db.close()
    personinfo = {}
    count=0
    for line in lines:
        line.strip()
        info = line.split(", ")
        for item in info:
            item.strip()
            key, value = item.split(": ")
            personinfo[key] = value
        if personinfo["username"].strip()==username:
            break
        else:
            personinfo.clear()
            count+=1
    del_item = input("What is the name of the item you would like to delete?\n")
    sec(1)
    cumexpenses-=int(personinfo[del_item])
    personinfo.pop(del_item)
    newcontent = ", ".join(f"{key}: {value}" for key, value in personinfo.items())
    modify_line_in_file(count, newcontent)
    print()
    again = input("Type \"delete\" to delete another row, otherwise press enter\n")
    if again.lower()=="delete":
        sec(1)
        delete_line(username, cumexpenses, expenseslist, count)
    else:
        sec(1)
        show_up_payments(username, cumexpenses)
    pass
def add_line(username, addline_list, personinfo, cumexpenses, count):
    label = input("What do you want to title your upcoming payment??\n")
    price = int(input("And how much do you have to pay??\n"))
    cumexpenses+=price
    personinfo["extra"]=personinfo["extra"].strip("\n")
    personinfo[label]=price 
    newcontent = ", ".join(f"{key}: {value}" for key, value in personinfo.items())
    modify_line_in_file(count, newcontent)
    addline_list.clear()
    addline_list.append(f"|      {label:<12} |       ${price:<10} |")
    print()
    again = input("Type \"add\" to add another row, otherwise press enter\n")
    if again.lower()=="add":
        add_line(username, addline_list, personinfo, cumexpenses, count)
    else:
        show_up_payments(username, cumexpenses)
    

def modify_line_in_file(count, new_content):
    # Read all lines from the file
    file = open("personalinfo.txt", "r")
    lines = file.readlines()
    file.close()

    # Modify the desired line
    if 0 <= count < len(lines):
        lines[count] = new_content + "\n"
    else:
        print("Line number out of range.")

    # Write all lines back to the file
    db = open("personalinfo.txt", "w")
    db.writelines(lines)
    db.close()

def show_up_payments(username, cumexpenses):
    db = open("personalinfo.txt", "r")
    lines = db.readlines()
    db.close()
    personinfo = {}
    count=0
    for line in lines:
        line.strip()
        info = line.split(", ")
        for item in info:
            item.strip()
            key, value = item.split(": ")
            personinfo[key] = value
        if personinfo["username"].strip()==username:
            break
        else:
            personinfo.clear()
            count+=1
    keys = list(personinfo.keys())

    expenseslist={}
    for key, value in personinfo.items():
        expenseslist[key.strip()]=value.strip()
    expenseslist.pop("budget")
    expenseslist.pop("username")
    expenseslist.pop("savings")
    expenseslist.pop("income")
    expenseslist.pop("hoursworked")
    expenseslist.pop("bigpaymentdate")
    expensestemp=0
    if cumexpenses==0:
        for value in expenseslist.values():
            expensestemp+=int(value)
        cumexpenses+=expensestemp
    incomeweekly = int(personinfo['income']) * 52
    income = incomeweekly/12
    expenses = cumexpenses/12

    if int(personinfo["bigpayment"])!=0:
        print(f"***You have an upcoming large payment on {personinfo['bigpaymentdate']}***\n")
        print(f"${personinfo['bigpayment']}\n")

    print(f"Here are your upcoming payments for the month of {current_month}")
    print()

    sec(1)
    print("-----------------------------------------")
    print("| UPCOMING PAYMENTS |  $$$ (in dollars) |")
    print("-----------------------------------------")
    print(f"|   housing/rent    |       ${personinfo['housing']:<10} |")
    print("-----------------------------------------")
    print(f"|  transportation   |       ${personinfo['transportation']:<10} |")
    print("-----------------------------------------")
    print(f"|     groceries     |       ${personinfo['groceries']:<10} |")
    print("-----------------------------------------")
    insuranceamt = 0
    if keys[5] != "groceries":
        for item in range(5, len(keys)):
            if keys[item] == "groceries":
                break
            else:
                insuranceamt+=1
                print(f"|  {keys[item]+" insurance":<16} |       ${personinfo[keys[item]]:<10} |")
                print("-----------------------------------------")
    print(f"|       extra       |       ${personinfo['extra'].strip():<10} |")
    print("-----------------------------------------")
    labels=[]
    for key in personinfo.keys():
        labels.append(key)
    if labels[11+insuranceamt:]==" ":
        pass
    else:
        for item in labels[11+insuranceamt:]:
            personinfo[item]=personinfo[item].strip()
            print(f"|  {item:<16} |       ${personinfo[item]:<10} |")
            print("-----------------------------------------")
    print(f"|       total       |       ${cumexpenses:<10} |")
    print("-----------------------------------------")
    print()
    sec(1)
    if income*0.65>expenses or income*0.75>expenses:
        pass
    elif income>expenses:
        pass
    elif income<expenses:
        print("It seems your debt is increasing faster than your income")
        print(f"You are earning ${income}, while spending a total of ${expenses} monthly")
        print("Based on your personal situation, I'd suggest reducing or removing the following payments:\n")
        sorteddict = dict(sorted(expenseslist.items(), key=lambda item: item[1]))
        for key, value in sorteddict.items():
            print(f"{key}: {value}")

    print() 
    sec(1)
    print("")
    print("If you want to add a line to your upcoming payments, type \"add\"")
    sec(1)
    print("To remove a line, type \"delete\".")
    sec(1)
    print("If you want to see your payments in a pie chart, type \"pie\". (CURRENTLY NOT WORKING)")
    sec(1)
    print("If you wish to exit the program, type \"exit\".\n")
    function = input()
    while True:
        if function == "add":
            sec(1)
            add_line(username, addline_list, personinfo, cumexpenses, count)
        if function== "delete":
            sec(1)
            delete_line(username, cumexpenses, expenseslist, count)
        if function == "exit":
            sys.exit(0)
        else:
            sec(1)
            print("Make sure to type \"add\", \"delete\", \"pie\", or \"exit\".\n")
            function = input()



def home():
    cumexpenses=0
    print("**----------------------------------------------------------PERSONAL FINANCE TRACKER**-----------------------------------------------------------------------**\n")

    sec(2)

    print("If you don't have an acccount, type **\"new\"** to sign up.")

    sec(1)

    print("If you wish to update your information type **\"update\"**.")

    sec(1)

    print("If you wish to exit the program, type **\"exit\"**.\n")

    sec(1)

    print("*----------ENTER USERNAME BELOW-----------*")

    username=input("U: ")

    sec(3)

    try:    
        if username.lower() =="new":
            register()
        
        elif username.lower()=="update":
            update()

        elif username.lower() =="exit":
            sys.exit(0)
        
        else:
            check_login(username)

        show_up_payments(username, cumexpenses)
        
    except SyntaxError:
        print("Invalid character. Run the program again and use valid characters.")

home()
