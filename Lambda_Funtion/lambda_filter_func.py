from collections import Counter

# Filter even numbers from a list using lambda function==========================
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = list(filter(lambda x : x % 2 ==0, a))
print(res)

# Filter numbers divisible by 13 from a list using lambda function==============
b =  [12, 65, 54, 39, 102, 339, 221, 50, 70]

res = list(filter(lambda x : x % 13 == 0, b))
print(res)

# Filter palindromic strings from a list using lambda function===================
c = ["apple", "geeg", "cherry", "date", "fig", "aa"]

res = list(filter(lambda x : (x == "".join(reversed(x))), c))
print(res)

# Filter anagrams of a given string from a list using lambda function===============
s = ["geeks", "geeg", "keegs", "practice", "aa"]
ts = "eegsk"

res = list(filter(lambda x: (Counter(ts) == Counter(x)), s))
print(res)