#without using parenthsis
num=1,2,3
print(num)  
#automatically packed in a tuple

#UNPACKING means Iterable unpacking also known as sequence unpacking this is in assingnment statments 
a,b="12"
c,d="34"
print(a,b,c)
"""
output
1,2,3
"""

#(*)Extended iterable unpacking 
first,*rest,last="python"
print(first,last)
"""
output
p n
"""
