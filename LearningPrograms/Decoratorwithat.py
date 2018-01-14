def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

#ordinary = make_pretty(ordinary)

ordinary()
#make_pretty(ordinary)


'''
def ordinary():
    print("I'm ordinary")
ordinary = make_pretty(ordinary)
'''