#Accseeing
d={"Name":"Ram","Age":20}
print(d["Name"])
print(d.get("Age"))
"""
output
Ram
20
"""
print(d.get("city"))
"""
output
None
"""
print(d["City"])
"""output
Key error"""
