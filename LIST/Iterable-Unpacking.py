#(*)extended iterable unpacking
data=["Alice",20,"Bhopal"]
first,*_,last=data
print(F"{first} is {20} years old city {last}")

""""output
Alice is 20 years old city Bhopal
"""