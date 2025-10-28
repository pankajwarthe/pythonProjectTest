list1 = [10,20,30,60,50]
print(list1)

list2 = ["warthe",10,20,30,60,"pankaj",'priya']
print(list2)

list3 = list1 + list2  # concatenation of 2 lists into 1
print(list3)

print(len(list3))
print(list3[4])
print(list3[0:])
print(list3[2:])
print(list3[2:6])

list1[0] = 666      #modify the list1
print(list1)

list1.append(888)   #add value at the last/end of the list1
print(list1)

list1.insert(0,123)  #insert value at the index
print(list1)

list1.extend(list2)
print(list1)

list1.pop()
print(list1)

list4=[4,3,2,34,565,2222,44]
list4.sort()
print(list4)

list4.reverse()
print(list4)