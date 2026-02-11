nums = [2,4,6,8]
nums.append(10)
print(len(nums))    

#counting the length
nums = [2,5,6,9,10]
nums.append(13)
print(len(nums))

#removing the values using slice operator
values = [2,2,2,3,4,2]
for v in values[:]:
    if v != 2:
        values.remove(v)
    print(values)    

#reverse string
    name = "Python"
    print(name[::-1])

#getting the every 2nd and element
    nums = [10,20,30,40,50,60,70]
    print(nums[::2])

#another 
nums=[1,2,3]
print(nums[-3:-1])    