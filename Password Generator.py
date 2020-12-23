import string 
from random import *

print("Hello wellcome to the password genertaor. This program will create a password for you \n")
#importing upper case and lower case strings, 0-9, symbols
#https://docs.python.org/3/library/string.html useful link that explains more in dept on python libraries
characters = string.ascii_letters + string.digits + string.punctuation 

#join characters atleast between 8 to 16
#randint basically stands for random integer.
password = "".join(choice(characters) for x in range(randint(8,16)))

print(password)

