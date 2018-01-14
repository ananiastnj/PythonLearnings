'''def args1(args,*args2):
    print("Args : ", args)
    for i in args2:
        print("Another Args2 : ",i)

args1(1,"Two",3,4)
'''

def args1(ar, **kwargs):
    print(ar)
    for k in kwargs:
        print("Another KWArgs : ", kwargs[k])
args1(ar =1, myarg=10, myarg2=20)

def arg3(ar1,ar2,ar3):
    print("Ar 1 : ",ar1)
    print("Ar 2 : ",ar2)
    print("Ar 3 : ",ar3)

args = ("hi","hello")
arg3(1,*args)

def arg4(ar1, ar2,ar3):
    print("Ar 1 : ", ar1)
    print("Ar 2 : ", ar2)
    print("Ar 3 : ", ar3)

kwargs = {"ar3" : 3, "ar2" : 2}
arg4(1,**kwargs)

