total_muthu = 70
pallanguli = [5 for i in range(14)]
print(pallanguli)
p1,p2 = 0,0
p1_start = int(input("Enter a start 0-6 : "))
muthu = pallanguli[p1_start]
pallanguli[p1_start] = 0
while(muthu != 0):
    for i in range(muthu):
        p1_start+=1
        if(p1_start > 13):
            p1_start = 0
        pallanguli[p1_start] += 1
    if (p1_start > 12):
        p1_start = -1
    print(p1_start)
    print(pallanguli)
    muthu = pallanguli[p1_start+1]
    print("Muthu : ",muthu)

print(pallanguli)