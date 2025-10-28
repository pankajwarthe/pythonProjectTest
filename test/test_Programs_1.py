# ======================== sum of all numbers in the List #=========

numbers = [70,20, 40, 80, 90]           # list
finalSum = 0

for j in numbers:
    finalSum = finalSum + j
    Total = str(finalSum)

print("Sum of all numbers: " + Total)

# ======================== print Even & Odd numbers in the List #=========
print("=========================================")
evenList = []
oddList = []
for x in range(0, 20):
    if x % 2 == 0:
        evenList.append(x)
    else:
        oddList.append(x)

print("Even List: " + str(evenList))
print("Odd List: " + str(oddList))

# ======================== print values in the List #=========

try:
    print("=========================================")
    l1 = ["pankaj", "priya", "keerat"]
    l2 = ["qa", "dev", "manager"]

    for a in l1:
        for b in l2:
            print(a + " " + b)

    # ======================== #=========
    print("=========================================")

except ValueError:
    print("Value Error occurred")