#SIMPLE CALCULATOR FOR USER

operation=input("choose choice:(+,-,*,/)")
num1=float(input("enter first choice : "))
num2=float(input("enter second choice : "))

if operation == "+":
    result = num1 + num2
    print(result)
elif operation == "-":
    result = num1 - num2
    print(result)
elif operation == "*":
    result = num1 * num2
    print(result)
elif operation == "/":
    if num2 !=0:
        result = num1 / num2
        print(result)
    else:
        print("not divisible :")

else:
    print("invalid number")              
