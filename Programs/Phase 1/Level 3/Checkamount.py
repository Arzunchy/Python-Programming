amount=int(input("Enter the currency: "))

if amount > 100:
    amount %=2000  #decreasing the amount
    amount %=500
    amount %=100
else:
    print("Enter amount > 100")    
if amount == 0: # if amount == 0 can't evenly distributed
    print("Divide ")
else:
    print("Not divide evenly with currency notes")    