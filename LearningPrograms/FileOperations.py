#import os - is module to access a file processing such rename and remove
import os
import re
#os.rename("Test.txt","Test2.txt")
read1 = open("Test2.txt","r")
#print(read1.read())
#os.mkdir("Test")
print(os.getcwd())
#os.chdir("C:/Users/ajesuraj/PycharmProjects/PrimeMaui-new/LearningPrograms/Test")
#print(os.getcwd())
#os.rmdir("Test")
fid = read1.fileno()
ftty = read1.isatty()
print("Fileno : ",fid)
print("isatty : ",ftty)
'''
line1 = read1.__next__()
print(line1)
line2 = read1.__next__()
print(line2)
'''
#print(read1.read(5))
print(read1.readline())
print(read1.readlines())