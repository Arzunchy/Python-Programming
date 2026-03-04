hours=int(input("Enter the hour(24 hours): "))
minutes=int(input("Enter the minute: "))

if 0 <= hours < 24 and 0 <= minutes < 60:
    if hours > 12:
        print(F'Its AM')
    else:
        print(F'its PM')
else:
    print("Invalid time")        
