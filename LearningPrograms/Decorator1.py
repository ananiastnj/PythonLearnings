'''
def foo(bar):
    return bar + 1
print(foo(2) == 3)
print(foo)
print(type(foo))

def call_foo_with_arg(foo, arg):
    return foo(arg)

print(call_foo_with_arg(foo, 3))
'''
'''
def parent(num):
    print("I'm parent")

    def first_child():
        print("I'm First child")

    def second_child():
        print("I'm second child")

    try:
        assert num == 10
        return first_child()
    except AssertionError:
        return second_child()

parent(10)
parent(16)
# First_Child() function cannot be called outside Parent function
#Decorator is a Nested function or taking the functios of inside function without modifying it.
# First_Child() and Second_Child() functions scope is inside functions alone.
'''
def my_decorator(some_function):
    def wrapper():
        num = 10
        if num == 10:
            print("YES .. !")
        else:
            print(" NO .. !")
        some_function()
        print(" After some_function")
    return wrapper()

if __name__ == "__main__":
    my_decorator(just_some_function)

@my_decorator()
def just_some_function():
    print("Wheee..!")
''''''
#just_some_function = my_decorator(just_some_function)
#print(type(just_some_function))
# Function name can be called as object. Another function name is the argument of another function.
