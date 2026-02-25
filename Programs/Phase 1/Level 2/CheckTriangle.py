# Brute Force Method
a = int( input("Enter first sides: "))
b = int(input("Enter second sides: "))
c = int(input("Enter third sides: ")) 

if a+b > c and a+c >b and b+c >a:
    print("Valid Triangle")
    if a == b and b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a Triangle")