import re

username = input("What is your username?")
password = input("What is your password?")

x= re.findall("\d", username)
y= re.findall("[a-z]", username)
a= re.search("^[a-zA-Z]", password)
b= re.search("[1-9]$", password)

if (x):
    print("FALSE, not the correct usename")
elif len(username)!=7:
    print("FALSE, not the correct username")
elif (y):
    print("FALSE, not the correct username")
elif len(password)!=7:
    print("FALSE, not the correct password")
elif (password[0]!=password[1]!=password[2]):
    print("FALSE, not the correct username")
elif (password[4]!=password[5]!=password[6]):
    print("FALSE, not the correct username")
elif (password[3]!="*"):
    print("FALSE, not the correct username")
elif (a):
    print("FALSE, not the correct password")
elif (b):
    print("FALSE, not the correct username")
else:
    print("TRUE, Welcome" + username)