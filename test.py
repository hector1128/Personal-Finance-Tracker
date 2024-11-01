username = input("U: ")




db = open("test.txt", "r")
users = db.readlines()
db.close()
    
neverfound = ""
for line in users:
    user, pw = line.strip().split(", ")
    if username==user:
        password=pw



entered_pw = input("P: ")
try:
    if entered_pw == password:
        
        print(f"*----------------------------------------------------Welcome back {username}!------------------------------------------------------------*")
            
    else:
        print("Password incorrect. Try again.")
except NameError:
    print("Username not found. Try again")

        









        

    

