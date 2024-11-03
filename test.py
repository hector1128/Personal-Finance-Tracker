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
    print(f"groceries: 80, {insurances}, budget: bomboclat")
    


        
    









        

    

