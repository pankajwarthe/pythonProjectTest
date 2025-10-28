
print("Welcome to If loop program")

a = 30

if a < 40:
    print("If condition is True")
else:
    print("Else is executed")
print("=======================================")

name = "pankaj"
if name == "pankajj":
    print("Hello pankaj")
else:
    print("goodbye pankaj")

print("Thanks for watching")
print("=======================================")

lang = input("What language are you using? :")
#lang="python"

if lang == "java":
    print("Hello java")
elif lang == "javascript":      # else-if example
    print("Hello javascript")
elif lang == "python":
    print("Hello python")
else:
    print("Sorry, I don't understand your language")
print("=======================================")

salary = input("What is your salary? : ")
salary = float(salary)

if salary > 50000:
    print("Eligible for car loan")
    if salary > 70000:
        print("Eligible for home loan")
        if salary > 100000:
            print("Eligible for all loans")
else:
    print("not eligible for any loans")
