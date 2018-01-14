#Program 3 - Number of letters in the String
import re
in_str = input("Enter a string : ")
matchobj = re.match(r'([a-z]*)([a-z]*)',in_str,re.I|re.M)
num_char = len(matchobj.group())
print("Number of letters : ", num_char)
