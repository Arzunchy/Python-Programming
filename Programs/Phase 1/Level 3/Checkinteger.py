nums=(input("Enter the digits: "))

#ABS use to remove  special symbols
length= len(abs(nums))

if length == 1:
    print(F'Single digit')
elif length == 2:
    print(F'Doubly digit')
elif length > 2:
    print(F'Multi-digit')
else:
    print(F'Invalid digits')            