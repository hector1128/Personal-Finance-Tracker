def update():
    username=input("What's your username??\n")
    #sec(3) 
    db = open("test.txt", "r")
    lines=db.readlines()
    db.close()
    info = {}
    infoinfiles=lines[:]
    def updateinfo():
        newinfo=input("What do you want to change?\n") 
        #sec(3)
        if newinfo in info:
            try:
                updatevalue=int(input(f"Enter your new {newinfo}. (Type a number)\n"))
                #sec(3)
                if newinfo == "hoursworked":
                    income = info["income"]
                    info["income"]=income*updatevalue
                info[newinfo]=updatevalue
                inputvalue=""
                inputvalue=", ".join(f"{key}: {value}" for key, value in info.items())
                for i, line in enumerate(infoinfiles):
                    if username in line:
                        infoinfiles[i]=inputvalue+"\n"
                        break
                db=open("test.txt", "w")
                for line in infoinfiles:
                    db.write(line)
                db.close()
            except:
                print("Make sure to input a number ONLY.")
                #sec(1)
                updateinfo() 

        else:
            print("Invalid entry. Make sure you type one of the following:")
            print("budget, income, groceries, transportation, housing, bigpayment, extra")
            #sec(3)
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
                        #sec(1)
                        for key, value in info.items():
                            print(f"{key}: {value}")
                        updateinfo()
                        break
                if checkforuser:        
                    print("username not found. Re-type it correctly.")
                    print("If you would like to create an account, type \"create\" to sign-up. Otherwise, click Enter to try again.")
                    #sec(3)
                    backhome=input()
                    if backhome=="create":
                        #home()
                        pass
                    else:
                        update()                        
                    info.clear()

update()