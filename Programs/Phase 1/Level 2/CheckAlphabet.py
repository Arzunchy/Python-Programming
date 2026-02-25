ch=input("Enter the Character: ").lower()

if ch in ("abcdefghijklm"):
    print(F'It lies between a to m')
elif ch in ("nopqrstuvwxyz"):
    print(F'It lies between n to z')
else:
    print(F'No alphabets lies') 
    


#Another way with ((Range Checking method)) 
ch=input("Enter the Charcater: ").upper()

if 'A' <= ch <= 'M':
    print(F'Lies between A to M')
elif 'N' <= ch <= 'Z':
    print(F'Lies between N to Z')
else:
    print(F'No character lies ')      