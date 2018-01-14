#ip1 = int(input());
ip1 = 2
#ip2 = int(input());
ip2 = 3
ip3_rows = 0
ip3_cols = 0
#ip3_rows = int(input())
ip3_rows = 2
#ip3_cols = int(input())
ip3_cols = 3
#ip3 = []
ip3 = [[2, 7, 5],[1, 9, 5]]
'''for ip3_i in range(ip3_rows):
    print("ip3_i : ", ip3_i)
    ip3_temp = [int(ip3_t) for ip3_t in input().strip().split(' ')]
    ip3.append(ip3_temp)
'''
#output = divisioncost(ip1,ip2,ip3)
#print(str(output))
print(ip3)
sum=0
ip3_lp2 = 0
ip3_lp1 = 0
ip3_lp2_1 = 0
ip3_lp1_1 = 0

for i in range(ip1):
    for j in range(ip2):
        sum=sum+ip3[i][j]
        if (j == (ip2 - 1)):
            ip3_lp2 = ip3[i][j] + ip3_lp2
        else:
            ip3_lp1 = ip3[i][j] + ip3_lp1

        if (i == (ip1 - 2) and j!=(ip2-1)):
            ip3_lp2_1 = ip3[i][j] + ip3_lp2_1
        elif(j!=(ip2-1)):
            ip3_lp1_1 = ip3[i][j] + ip3_lp1_1


sum = sum + ip3_lp2 + ip3_lp1 + ip3_lp2_1 + ip3_lp1_1
print("Before partion total trees : ", sum)


#After add all the values calculate the last partition divided

'''
ip3_lp2 = 0
ip3_lp1 = 0
for i in range(ip1):
    for j in range(ip2):
        if(j== (ip2-1)):
            ip3_lp2 = ip3[i][j]+ip3_lp2
        else:
            ip3_lp1 = ip3[i][j] + ip3_lp1
'''
print("ip3_lp2 : ",ip3_lp2)
print("ip3_lp1 : ",ip3_lp1)
sum = ip3_lp2+ip3_lp1+sum
print("Sum of total : ", sum)
#
'''
for i in range(ip1):
    for j in range(ip2-1):
        if(i==(ip1-2)):
            ip3_lp2_1 = ip3[i][j] + ip3_lp2_1
        else:
            ip3_lp1_1 = ip3[i][j] + ip3_lp1_1
'''
print("ip3_lp2_1 : ", ip3_lp2_1)
print("ip3_lp1_1 : ", ip3_lp1_1)
sum = ip3_lp2_1 + ip3_lp1_1 + sum
print("Sum of total : ", sum)
#

