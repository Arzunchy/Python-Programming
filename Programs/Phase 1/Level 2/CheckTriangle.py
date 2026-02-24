# Brute Force Method
a, b, c = map(int, input("Enter three sides: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
    if a == b and b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a Triangle")