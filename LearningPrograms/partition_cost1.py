def partitioncost(ip1, ip2, ip3):
    sum = 0
    print(ip1, ip2, ip3)
    for k in range(ip1):
        for p in range(ip2):
            print("k : ",k," p : ",p, "ip3[",k,'][',p,'] : ',ip3[k][p])
            sum = sum + ip3[k][p]
    print("Sum : ", sum)

    if(ip2 > 0):
        ip2 -= 1
        partitioncost(ip1, ip2, ip3)
    return sum

ip1 = 2
ip2 = 3
#ip3_rows = ip1
#ip3_cols = ip2
ip3 = [[2, 7, 5],[1, 9, 5]]
#print(ip3)
print("Sum demo : ",partitioncost(ip1,ip2,ip3))



