#sorting 
d={"a":3,"b":1,"c":2}

#sort by keys
sorted_by_keys=dict(sorted(d.items()))
print(sorted_by_keys)

#sort by values
d={"a":3,"b":1,"c":2}             #>[1] means giving the index of values
sorted_by_values=dict(sorted(d.items(),key=lambda items:items[1])) 
print(sorted_by_values)
""""output
{'b': 1, 'c': 2, 'a': 3}
"""