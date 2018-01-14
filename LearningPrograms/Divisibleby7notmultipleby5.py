'''que='''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).'''
print(que)'''
#count = 0
l=[]
for i in range(2000,3201):
    #print(i)
    if (i%7)==0 and (i%5)!=0:
        print("The value divisible by 7 and not multpile of 5 : ",i)
        #count+=1
        l.append(i)
#print("Total number between 2000 and 3200 which are divisible by 7 and not multiple of 5: ",count)
print(l)