first_name="pankaj"
last_name="warthe"
print(first_name)
print(last_name)
print(first_name+" "+last_name)

print("\"Python\"")

print("i know\tPython")
print("i know\nPython")

#name="ssasdasd"--------- # (hashtag) is used for comment

print("=============================")
sent = "i love python"
print(type(sent))
print(len(sent))            # len() is to find out the length of the string
print(sent.count("o"))      # .count will return count of matching character
print(sent.count("Python")) # .count will return count of matching string
print(sent.index("o"))      # .index will return first index value of matching char. evenIf there are duplicate chars, it will always return 1st index
print(sent.replace("p","J"))  # .replace will replace all character from a string
print(sent.replace("o","J"))  # .replace will replace all character from a string
print(sent.split('p'))      # split the string before & after 'P'
print(sent.split(' '))      # split the string when it found the " "
print(sent.upper())         # .upper makes all chars in capitals
print(sent.lower())         # .lower makes all chars in lower letters
print(sent.islower())       # .isLower return true if all chars are lower letters
print(sent.isupper())       # .isUpper return true if all chars are upper letters