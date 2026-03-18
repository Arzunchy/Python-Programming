#Create a new dictionary with given keys and a singe default value
keys=["a","b","c"]
d= dict.fromkeys(keys,0)
print(d)
""""output
{'a': 0, 'b': 0, 'c': 0}  #All keys return the same default value
"""