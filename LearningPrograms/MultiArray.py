'''row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
print(multi_list)
for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)
'''
#m_list = [[5,10,15,20],[4,8,12,16]]
#print(m_list[1][2])
row_size = int(input("Enter a row size : "))
col_size = int(input("Enter a col size : "))
multi_list = [[int(input("Enter a value : ")) for col in range(col_size)] for row in range(row_size)]
print(multi_list)
'''for row_v in range(row_size):
    for col_v in range(col_size):
        multi_list[row_v][col_v] = int(input("Enter a value : "))
print(multi_list)'''
