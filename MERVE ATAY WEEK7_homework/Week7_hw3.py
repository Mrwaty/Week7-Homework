'''
Merve Atay 17.03.2022

Question 3: Write a program that list according to email addresses without email domains in a text.

Example:

Input:

The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. 
Then New Yorker article on wind farms...

Output :

franky

sinatra123
'''
import re

text= input("Write a text:\n")

patern= r"\w{1,}@"

for x in re.findall(patern,text):
    print (*x.split("@"))