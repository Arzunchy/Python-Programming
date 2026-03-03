ch=input("Enter the character: ")

if ch.isalpha():
    print(F'It is letter')
elif ch.isdigit():
    print(F'It is digit')
else:
    print("Neither letter or digit")        