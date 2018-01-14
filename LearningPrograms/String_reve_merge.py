'''Lets move from the original String to the final  : abcde
Since the length of String is odd so we select the middle character i.e c 
and append it to the new String.Now new String is abde ,
the length is even so we select the left of the middle two elements i.e b ,
new String is now ade ,now we select d ,the String becomes ae ,we select now a and finally e .
So the new String by appending all the selected characters is cbdae .
Now, You have to reverse this process and get the original String i.e. "abcde".
'''
str1 = "abcde"
str1_list = list(str1)
#print(str1_list)
str2 = ""
for i in range(len(str1)):
    if len(str1_list)%2 == 0:
        middle = len(str1_list)//2
        #str_index = middle - 1
    else:
        middle = len(str1_list)//2+1
        #str_index = middle - 1
    #print(middle)
    str2 = str2 + str1_list[middle-1]
    str1_list.pop(middle-1)
    #print(str1_list)
print(str2)
str2_list = list(str2)
str3_list = str2_list.copy()
mid = len(str2_list)//2
print(mid)
rhalf = str2_list[:mid]
lhalf = str2_list[mid:]
print(rhalf)
print(lhalf)
j = 0
for i in range(len(str2)):
    if i < mid:
        j = j + 1


