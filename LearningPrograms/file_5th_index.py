file1 = open("File3.txt","r")
fl = []
for line in file1:
    str2 = ""
    line = str(line.rstrip())
    #print(line)
    for i in range(len(line)):
        str2 = str2 + line[i]
        if i%5 == 4:
            str2 = str2 + ","
    #str2 = str2[::-1]
    str2 = str2.split(",")
    fl.append(str2)
print(fl)
'''
str1 = "ABCDEFGHIJKLMNOPQ"
list1 = list(str1)
str2 = ""
#print(list1)
for i in range(len(str1)):
    #print(str1[i])
    str2 = str1[i] + str2
    if i%5 == 4:
        str2 = "," + str2
        #print(str2)
str2 = str2[::-1]
str2 = str2.split(",")
print(str2)
'''