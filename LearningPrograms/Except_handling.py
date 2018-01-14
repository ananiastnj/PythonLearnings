class NameErr(Exception):
    def __init__(self):
        print("Hello")

try:
    a = 10
    print(a)
    raise NameErr()
except NameErr as e:
    print(e)