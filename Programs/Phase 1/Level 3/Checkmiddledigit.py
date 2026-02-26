#Check middile digit are largest, smallest or neither
a=int(input("Enter the first digit: "))
b=int(input("Enter the second digit: "))
c=int(input("Enter the third digit: "))

if b > a and b > c:
    print(F'Middle digit is largest')
elif b < a and b < c:
    print(F'Middle digit is smallest')
else:
    print(F'Middle digit is Neither largest or smallest')        