#Removing elements
d={"a":1,"b":2,"c":3}

d.pop("a")  #remove key 'a'
print(d)
"""output
{'b': 2, 'c': 3}
"""
d={"a":1,"b":2,"c":3}
d.popitem() #remove last inserted item
print(d)
"""output
{'a': 1, 'b': 2}
"""

d={"a":1,"b":2,"c":3}
del d["b"]  #delete specific
print(d)
"""output
{'a': 1, 'c': 3}
"""

d.clear    #empty dictionary -remove all elements from dictionary
"""output
{}
"""