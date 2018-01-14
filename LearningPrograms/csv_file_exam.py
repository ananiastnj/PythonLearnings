import csv
with open("csv_file.csv",'r') as csvfile1:
    csvreader = csv.reader(csvfile1,delimiter = ' ', quotechar = '|')
    print(csvfile1)
    print("Readlines : ",csvfile1.readlines())
    for row in csvreader:
        print("Join1 : ",(", ".join(row)))
    for readline1 in csvfile1.readlines():
        readline1 = csvfile1.readline()
        print("Readline1 : ",readline1)

import csv
with open('csv_file.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print(list(reader))
    for row in reader:
        print(row['first_name'], row['last_name'])
        print(row)
