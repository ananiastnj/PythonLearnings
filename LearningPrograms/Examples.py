'''numbers = [6,5,3,8,4,2,5,4,11]
sum = 0
#numbers[3]
length = len(numbers)
print("Length : ",length)
for i in range(length):
    print(numbers[i])
print(i)
'''
#n = int(input("Enter n: "))

'''n = 5
# initialize sum and counter
sum = 0
i = 1
while(i <= n):
    sum = sum + i
    i = i+1 # update counter
# print the sum print("The sum is",sum)

print("Sum : ",sum)
'''
'''
for val in "ananias":
    pass
'''
'''
    if(val == "a"):
        #continue
        break
    print(val)
print("The end")
'''


vowels = "aeiouAEIOU"
# infinite loop
while(True):
    v = input("Enter a vowel: ") # condition in the middle
    if v in vowels:
        print("This is a vowel")
        break
    print("That is not a vowel. Try again!")
print("Thank you!")

