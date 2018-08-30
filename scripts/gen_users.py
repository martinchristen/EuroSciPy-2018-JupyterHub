#!/opt/anaconda3/bin/python

#Python Script to generate random users

import crypt
import os
import string
import random
from collections import OrderedDict

if os.getuid()!= 0:
    print("This script must be called as superuser: sudo python gen_users.py")
    exit(0)


def createUser(name,username,password):
    encPass = crypt.crypt(password,"22")   
    os.system("useradd -p "+encPass+ " -G jupyter -s "+ "/bin/bash "+ "-d "+ "/home/" + username+ " -m "+ " -c \""+ name+"\" " + username)
    os.system("usermod -a -G anaconda " + username)

def idgenerator(size=5):
    chars = string.ascii_lowercase
    return "".join(random.choice(chars) for x in range(size)) 


s = input("How many users do you want to create ? >")
try:
   num = int(s)
except:
   print("error, please specify a number!")
   exit(0)


batch = idgenerator(2)
users = OrderedDict()
for i in range(num):
    username = batch + str(i)
    password = idgenerator(6)
    users[username] = password
    print("username: " + username + ", password: " + password)


q = ""
while True:
    q = input("create ? (y/n) >")
    if q == "y" or q=="n":
        break


if q=="n":
   print("ok. stop. bye!")
   exit(0)
elif q=="y":
   print("creating users.")
   file  = open("userlist_" + batch + ".txt", "a")
   for user in users:
       createUser(user,user,users[user])
       file.write(user + ", " + users[user] + "\n")
   file.close()
      
print("\n")
print("to remove users call: userdel -f < userlist_" + batch + ".txt")
