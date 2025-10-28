
def helloworld():
    print("Hello World")
    c= 10 + 20
    print(c)
    print("Function execution completed =================================")

helloworld()
#===================================

def sum(num1, num2):
    total = num1 + num2
    print(total)

sum(22,33)
#===================================

def greeting(fname, lname):
    print("Hello "+fname+" "+lname)

greeting("Pankaj", "warthe")
greeting(fname="Pankaj", lname="Warthe")        # this is called keyword argument
#===================================

def swap(num1, num2):
    num1, num2 = num2, num1
    print("After swapping: num1 =", num1)
    print("After swapping: num2 =", num2)
swap(10, 20)
#===================================

def extend_list(val, list=[]):
    list.append(val)
    return list

list1 = extend_list(10)
list2 = extend_list(123,[])
list3 = extend_list('a')
print(list1)
print(list2)
print(list3)

list = ['a', 'b', 'c', 'd', 'e']
print(list[10:])