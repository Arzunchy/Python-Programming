#Distinct means digits should not equal if equal this is not distinct
a=int(input("Enter the first digit(hundred): "))
b=int(input("Enter the second digit(tens): "))
c=int(input("Enter the third digit(ones): "))

#check the digits 
if a != b and b !=c and c != a:
    print(F'Digits are distinct ')
else:
    print(F'Digits are not distinct')    
