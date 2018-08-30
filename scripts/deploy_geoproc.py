#!/opt/anaconda3/bin/python

from sys import argv
from shutil import copyfile
from os import chmod
import os

DEPLOYDIR = "/home/"
COURSESHORTCUT = "fm"
USERCOUNT = 24

if len(argv) == 1 or len(argv)>3:
    print("wrong usage!")
    print("deploy.py file")
    print("deploy.py dir -d")
    exit(0)


directory = False

if len(argv) == 3 and argv[2]=="-d":
    print("copy directory...")
    directory = True

filename = argv[1]
coursename = COURSESHORTCUT
users = USERCOUNT

for i in range(users):
   username = coursename+str(i)
   dest = DEPLOYDIR + username + "/" + filename
   print("copy " + filename + " to " + dest) 
   #copyfile(filename, dest)
   if directory:
       dest = DEPLOYDIR + username + "/"
       os.system("rsync -r " + filename + " " +  dest)
   else:
       os.system("cp " + filename + " " + dest)
   #chmod(dest, 0777)

   if directory:
       print("chown " + username + ":" + username + " " + DEPLOYDIR +  username + "/" + filename + " -R")
       os.system("chown " + username + ":" + username + " " + DEPLOYDIR +  username + "/" + filename + " -R")
   else:
       os.system("chown " + username + ":" + username + " " + DEPLOYDIR +  username + "/" + filename)
