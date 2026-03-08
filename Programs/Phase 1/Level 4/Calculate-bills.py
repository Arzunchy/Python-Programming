units=int(input("Enter the electricity unit: "))
bills=0

if units <=100: #for 100 units 5 rs units
    bills= units * 5
elif units <=200: #for 200 units 7 rs units
    bills=(100 * 5) + (units - 100) * 7 
elif units <=300:
    bills=(100 * 5) + (100 * 7) + (units - 200) * 10
else:
    bills=(100 * 5) + (100 * 7) + ( 100 * 10) + ( units - 300) * 12

print(F'Electricity Bill is {bills}')
