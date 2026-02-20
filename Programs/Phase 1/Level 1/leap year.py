year =int(input("enter the year : "))

if year % 4 ==0 and (year % 100 != 0 or year % 400 == 0):
    print(F'{year} is Leap year')
else:
    print(F'{year}is Not leap year')    