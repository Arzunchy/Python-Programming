num=int(input("Enter the number: "))

root=(num ** 0.5) #gives the squareroot of number 

if root * root == num: # checks the square root of eqaul to original number
    print("Perfect square")
else:
    print("Not perfect square")    