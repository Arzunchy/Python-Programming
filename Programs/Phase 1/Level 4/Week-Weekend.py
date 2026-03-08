Day=int(input("Enter the day: "))

if 1 <= Day <=5:
    print(F'This days are weekday')
elif Day == 6 or Day == 7:
    print(F'This days are Weekend')
else:
    print("No weekend")        

"""
if Day == 1:
    print(F'Sunday is weekend')
elif Day == 2:
    print(F'Monday is weekday')
elif Day == 3:
    print(F'Tuesday is weekday')
elif Day == 4:
    print(F'Wednesday is weekday')
elif Day == 5:
    print(F'Thursday is weekday')
elif Day == 6:
    print(F'Friday is weekday ')
elif Day == 7:
    print(F'Saturday is weekend')
else:
    print("No weekend") """                          