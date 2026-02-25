a=int(input("Enter the Fisrt Number: "))
b=int(input("Enter the second Number: "))

if a % 2 == 0 and b % 2 == 0:
    print(F'Both Are Even')
elif a % 2 != 0 and b % 2 != 0:
    print(F'Both Are Odd') 
else:
    print(F'One is Even and One is Odd')
           