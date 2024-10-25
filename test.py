username=input("What's your username??\n") 
print("Here's your current information:")
db = open("personalinfo.txt", "r")
lines=db.readlines()
db.close()
info = {}
for line in lines:
    line.strip()
    entries = line.split(", ")
    for entry in entries:
        key, value=entry.split(": ")
        info[key.strip()]=value.strip()
    for key, value in info.items():
        if value == username:
            for key, value in info.items():
                print(f"{key}: {value}")       
    info.clear()
            
        
