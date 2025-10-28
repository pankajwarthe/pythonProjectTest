x=1

while x < 5:
    print(x)
    x=x+1

# ======================== #=========
print("=========================================")

num = 2

while num < 10:
    print(num)
    num = num + 1
else:
    print("num is no longer less than 10")      # here else block will be executed
# ======================== #=========
print("=========================================")

count = 1

while count < 15:
    count = count + 1
    print(count)
    if count == 10:
        break
else:
    print("count is no longer less than 15")    # here else block will not be executed due to break statement

# ======================== #=========
print("=========================================")

cnt = 1

while cnt < 10:
    cnt = cnt + 1
    if count == 3:
        continue
        print("Python")
    print(cnt)