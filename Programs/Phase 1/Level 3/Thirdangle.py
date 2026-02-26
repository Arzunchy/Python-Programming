a=float(input("Enter the first angle: "))
b=float(input("Enter the second angle: "))

c=180-(a+b)

if c < 180:
    print(F'Third angle is {c}')
else:
    print("Not a valid angle")
    
