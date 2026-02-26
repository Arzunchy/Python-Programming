x=int(input("Enter the value of x-axis: "))
y=int(input("Enter the value of y-axis: "))

#(+ve and +ve)
if x > 0 and y > 0:
    print("Lies on the first quadrant")
#(-ve and +ve)    
elif x < 0 and y > 0:
    print("Lies on the second quadrant")
#(-ve and -ve)    
elif x < 0 and y < 0:
    print("Lies on the third quadrant ")
#(+ve and -ve)    
elif x > 0 and y < 0:
    print("Lies on the fourth quadrant")
else:
    print("Invalid quadrant ")                           

