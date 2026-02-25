ch=input("Enter the Character: ")

if ch in ("abcdefghijklm"):
    print(F'It Lies Between a to m')
elif ch in ("nopqrstuvwxyz"):
    print(F'It Lies Between n to z')
else:
    print(F'No Alphabets Lies') 


#Another way with ((Range Checking method)) 
ch=input("Enter the Charcater: ")

if 'A' <= ch <= 'M':
    print(F'Lies Between A to M')
elif 'N' <= ch <= 'Z':
    print(F'Lies Between N to Z')
else:
    print(F'No Character Lies ')      