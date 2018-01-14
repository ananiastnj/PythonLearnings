num = input("Enter a number : ")
search = open("file2.txt","r")
for line in search:
  if num in line:
      print(line)