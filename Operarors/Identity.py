
# ""IS"" operator check two variable with same object  in memory

x=[1,2,3]
y=x
z=[1,2,3]
print(x is y)  # same object 

print(x is z) # diffrent object with same values 


# """IS NOT""" check they are  different objects
x=[1,2,3]
y=x
z=[1,2,3]
print(x is not z)