rows = int(input("Enter row size : "))
cols = int(input("Enter col size : "))
m1=[[]]
for i in range(rows):
    for j in range(cols):
        print("i : ",i," j : ",j)
        m1[i][j]=int(input("Enter a vlaue : "))

print(m1)


