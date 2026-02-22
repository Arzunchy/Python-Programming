# 1. Check if three sides form a valid triangle
a, b, c = map(int, input("Enter three sides: ").split())
if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a Triangle")

# 2. Marks to Grade
marks = int(input("Enter marks (0-100): "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Grade F")

# 3. Check if one number is a multiple of the other
x, y = map(int, input("Enter two numbers: ").split())
if x % y == 0 or y % x == 0:
    print("One is a multiple of the other")
else:
    print("Not multiples")

# 4. Greeting based on hour
hour = int(input("Enter hour (0-23): "))
if 5 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
elif 17 <= hour < 21:
    print("Good Evening")
else:
    print("Good Night")

# 5. Voting eligibility
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# 6. Even/Odd check
m, n = map(int, input("Enter two numbers: ").split())
if m % 2 == 0 and n % 2 == 0:
    print("Both Even")
elif m % 2 == 1 and n % 2 == 1:
    print("Both Odd")
else:
    print("One Even, One Odd")

# 7. Alphabet range check
ch = input("Enter a lowercase alphabet: ")
if 'a' <= ch <= 'm':
    print("Between a and m")
elif 'n' <= ch <= 'z':
    print("Between n and z")
else:
    print("Invalid input")

# 8. Day number to name
day = int(input("Enter day number (1-7): "))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if 1 <= day <= 7:
    print(days[day - 1])
else:
    print("Invalid day number")

# 9. Month number to days (ignoring leap years)
month = int(input("Enter month number (1-12): "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    print("28 days")
else:
    print("Invalid month number")


    # the number of  three number of 
    a,b,c=map(int, input(" three sides : ".spilt()))
    