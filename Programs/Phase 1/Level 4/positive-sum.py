num1=int(input("Enter first number: "))
num2=int(input("Enter the second number: "))

if num1 > 0 and num2 > 0:
    if (num1 + num2) <= 100:
        print(F'Yes')
    else:
        print(F'No')
else:
    print("Invalid number ")    
