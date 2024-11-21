dict1={"username": "hector1128", "budget": 200, "test": 0}
db=open("test.txt", "r")
lines = db.readlines()
for line in lines:
    testlist = line.strip().split(", ")
    print(testlist.split(": "))



    









        

    

