status = False
names = ["java", "js", "python"]

for name in names:          # for loop ->job
    if name == "python":
        status = True
        break
    else:
        print("please wait we have to search")

if status:
    print("we are glad that we found the record")
else:
    print("we are glad that we did not find the record")


