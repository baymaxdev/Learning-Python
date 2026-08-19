#Importing Built-in Modules
import os
import sys

#Importing Self-Made Modules
# import myModule , Imports The Whole Module
# from myModule import generateFullName, generateGreeting
from myModule import generateFullName as gF
from myModule import generateGreeting as gG
from myModule import generateStrongPassword as gSP

gG(gF("Ammar", "Awan"))

gSP(30)

print(os.getcwd())

#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
if len(sys.argv) > 1:
    print(f'Welcome {sys.argv[1]}. Enjoy {sys.argv[2]} challenge!')
else:
    print("No Argument")

