#Shallow copy() of the dictionary

d={"a":1,"b":2}  #change in duplicate won't affect original
d2=d.copy()
print(d2)
""""output
{'a': 1, 'b': 2}
"""