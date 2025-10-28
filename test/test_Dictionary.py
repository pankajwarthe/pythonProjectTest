emp = {"qa":"pankaj","dev":"priya","devOps":"rock","dev":"keerat"}
print(emp)

emp2 = {"qa":["pankaj","mukesh","sushant"],"devOps":"rock222"}
print(emp2)
print(emp2["qa"])
print(emp2["devOps"])
#print(emp2[])

print("====================")

employee = {"qa":"pankaj","dev":{"frontend":"priya","devOps":"rocky"}}
print(employee)
print(employee.get("dev").get("frontend"))

print("====================")

employee["manager"]="mayur"     # add value to dict
print(employee)

print("====================")

employee.pop("devOps")
print(employee)
print(employee.keys())

print(employee.values())
