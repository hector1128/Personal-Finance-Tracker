username=input("What's your username??\n") 
print("Here's your current information:")
db = open("test.txt", "r")
lines=db.readlines()
db.close()
info = {}
for line in lines:
    line = line.strip()
    entries = line.split(", ")
    for entry in entries:
        key, value=entry.split(": ")
        info[key.strip()]=value.strip()
    for key, value in info.items():
        if value == username:
            for key, value in info.items():
                print(f"{key}: {value}")
            def update():
                newinfo=input("What do you want to change?\n") 
                if newinfo in info:
                    updatevalue=int(input("How much do you want to add?? (Type a number)\n"))
                    try: 
                        info[newinfo]=updatevalue
                    except ValueError:
                        print("Make sure to input a number ONLY.")
                        update()
                    db=open("test.txt", "w")
                    entries=[]
                    for key, value in info.items():
                        entries.append(f"{key}: {value}")
                    db.write(", ".join(entries))
                else:
                    print("Invalid entry. Make sure you type one of the following:")
                    print("budget, income, groceries, transportation, housing, bigpayment, other")
                    update()
            update()              
    info.clear()

