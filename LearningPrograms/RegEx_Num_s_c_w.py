str1 = "1.The Cisco Network Plug and Play solution provides a simple, secure, unified, and integrated offering for enterprise network customers to ease new branch or campus rollouts, or for provisioning updates to an existing network. 2.The solution provides a unified approach to provision enterprise networks comprised of Cisco routers, switches, and wireless devices with a near zero touch deployment experience. 3.For more information on the Cisco Network Plug and Play solution, see Solution Guide for Cisco Network Plug and Play."

'''Print the number of characters, words, symbols , numbers and lines.
a.	Output should be
i.	Number of characters :
ii.	Number of words :
iii.	Number of symbols:
iv.	Number of numbers :
v.	Number of lines :
'''
import re
digits1 = re.match(r'(\d*)', str1, re.I|re.M)
print(digits1.group())
words1 = mo.group(2)
print(words1)
symb1 = mo.group(3)
print(symb1)

