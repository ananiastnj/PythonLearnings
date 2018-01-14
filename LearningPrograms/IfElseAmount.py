amount=int(input("Enter amount : "))
if(amount<1000): discount=amount*0.05
else: discount=amount*0.10
print("Netpayable : ",amount-discount)

if None:
    print("None")


#int(input("Enter amount : ") - Combined 3 lines in 1
#No variable life scope
#Arithmatic operater work in the print line... only assignment won't happen in the printline
