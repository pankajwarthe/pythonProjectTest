
myLang = "i know {}".format("python")
print(myLang)

myLang = "i know {} {} {}".format("python","java","JS")
print(myLang)

myLang = "i know {2} {1} {0}".format("python","java","JS")  #using index value
print(myLang)

myLang = "i know {p} {j} {js}".format(p='python',j='java',js='JS') #using key-value pair
print(myLang)
#===================================================================================================

name="pankaj"
prog='Python'
print(f"my name is {name} and i know {prog}")
#===========================================================================

var = "Python is very easy"
print(var[2:6])  # here is start reading from 2nd indext and stop at 6th
print(var[2:])   # here it will skip 2 indexes and print the rest of the string
print(var[:2])   # here it will print first 2 indexes and skips the rest
print(var[::2])  # here
print(var[::-1]) # this is to reverse the string