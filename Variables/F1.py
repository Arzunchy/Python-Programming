#print simple program
name = "Arjun"
age = 19
number = 7
print(name)

#checks the type of variables values
name ="Arjun"
age = 19
height = 5.6
print(type(name))
print(type(age))
print(type(height))

#print whole details in once using f-string
name="Arjun"
age = 19
occupation = "data scientist"
no = 8791012880
details = f"""---personal details ---
name : {name}
age  : {age}
occupation: {occupation}
no   : {no}
"""
print(details)
