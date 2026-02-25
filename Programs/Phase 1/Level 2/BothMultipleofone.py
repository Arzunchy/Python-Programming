a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

if a % b == 0:
    print(F'{a} is Multiple of {b}')
elif b % a == 0:
    print(F'{b} is Multiple of {a}')
else:
    print(F'Neither Multiple of other')  
    

      