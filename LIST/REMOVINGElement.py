#REMOVE we use element to remove it

numbers=[10,20,30,40,50]
numbers.remove(30)
print(numbers)
""""
output
[10, 20, 40, 50]
"""
#popped for last element
numbers=[1,2,3,4,5]
popped_value=numbers.pop()
print(numbers)
""""output
[1, 2, 3, 4]
"""

#popped for index value
numbers=[1,2,3,4,5]
popped_index_value=numbers.pop(2)
print(numbers)
""""output
[1, 2, 4, 5]
"""

#DELETE
numbers=[1,2,3,4,5]
del numbers[0]
print(numbers)
""""output
[2, 3, 4, 5]
"""
#CLEAR for remove all elements
numbers=[1,2,3,2,4,5]
numbers.clear() 
print(numbers)
""""output
[]"""


#REMOVE using set because set returns unique elements
nums=[1,2,3,4,2,5]
nums=list(set(nums))
print(nums)
""""output
[1, 2, 3, 4, 5]
"""


