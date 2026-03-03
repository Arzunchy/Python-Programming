nums=int(input("Enter the number: "))

if nums % 3 == 0 and nums % 5 == 0:
    print(F'It is divisible by both')
elif nums % 3 == 0:
    print(F'This is fizz')
elif nums % 5 == 0:
    print(F'This is buzz')
else:
    print("Neither both of it")            