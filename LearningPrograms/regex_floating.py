import re
val1 = input("Enter a floating number : ")
mat1 = re.match(r'(\d*)\.(\d+)',val1)
print(bool(mat1))


#Finding valid mobile number :
l1 = ['9876543210','9801235674','8901235456','adsfertwe']
#pattern = r'^[9](\d){9}$'
#pattern = r'^9[0-9]{9}$'
for i in l1:
    mat1 = re.match(r'^[9](\d){9}$',i)
    if(mat1):
        print(i, " is valid mobile number")
    else:
        print(i," is not valid mobile number")