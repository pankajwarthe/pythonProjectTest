
tup1 = ("pankaj",1,2,3,4,5,5,5,90.2)

print(tup1)
print(tup1[1])
print(tup1[-1])
print(tup1[-2])
print(tup1.count(5))
print(tup1.index("pankaj"))
print(tup1[0:4])
print(type(tup1))
print("=================================")

# tuples are immutable example ====================================================
#tup1[0] = "pankaj"
#print(tup1)

#it's possible to convert Tuple into Set & List >> example  =======================
tup2 =  ("pankaj",1,2,3,4,5,5,5,90.2)
print(type(tup2))
print(tup2)

l1 = list(tup1)  # Tuple converted into List
print(type(l1))
print(l1)

s1 = set(tup2)  # Tuple converted into Set
print(type(s1))
print(s1)

print("=================================")

list1 = [(2,3,1),(22,33,44),(77,88,99)]
print(list1[0])
print(list1[1][2])
