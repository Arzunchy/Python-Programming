#squares
d={x:x*x for x in range(1,6)}
print(d)

""""output
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
#with condition
d={x:x*x for x in range (10)if x%2==0}
print(d)
""""output
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
"""