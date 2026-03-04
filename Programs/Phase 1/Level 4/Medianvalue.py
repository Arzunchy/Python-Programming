a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

if (a > b and a < c) or (a < b and a > c):
    print(F'Median value is A')
elif (b > a and b < c) or ( b < a and b > c):
    print(F'Median value is B')
else:
    print("Median value is C")
