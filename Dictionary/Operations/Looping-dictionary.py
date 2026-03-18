#
d={"a":1,"b":2}
#keys
for keys in d:
    print(keys)
""""output
a
b    
"""
#for values
d={"a":1,"b":2}
for value in d.values():
    print(value)
""""output
1
2    
"""
#Key-value pairs
d={"a":1,"b":2}
for k,v in d.items():
    print(k,v)
""""output
a 1
b 2    
"""
