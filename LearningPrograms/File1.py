import re
import pep8
file1 = open("File1.txt","r")
mat, mmat = 0, 0
for line in file1:
    try:
        sch = re.compile(r'^(School)$')
        #print(sch.search(line))
        #print(sch.search(line).group())
        if sch.search(line).group() in "School":
            mat += 1
    except Exception:
        mmat += 1
print("School matched ",mat," times")
print("School mismatched ",mmat," times")


'''
import re
wri = open("File1.txt","r+")
#wri.write("School\nSchool\nschool\nshoolc\nScholl")
#print(wri.readlines())
#line = wri.readlines()
cou =1
mat = 0
mmat = 0
#print(line)
if "School" == "School":
    print("School matched")
else:
    print("School not matched")

for line in wri:
    print("Line ",cou," : ",line)
    cou += 1
    line.rstrip()
    if line == "School\n":
        mat+=1
    else:
        mmat+=1

    matchobj = re.match(r'^School\n$',line,re.I|re.M)
    try:
        print(matchobj.group())
        if matchobj.group():
            mat += 1
    except Exception as e:
            print("Error : ", e)
            mmat += 1
    else:
        mmat += 1


'''