# Python program to find ASCII value of all characters

#importing string function
import string

# printing ascii value of character
for c in string.ascii_letters:
    print(c,':', ord(c), end = ', ')