#Adds and Update
d={}

#Add the elements
d["name"]="Ram"     

#Update the elements
d["name"]="Jhon"      #override the element

#Multiple update
d.update({"Age":21,"City":"Bhopal"})

print(d)

"""output
{'name': 'Jhon', 'Age': 21, 'City': 'Bhopal'}
"""
