
# decorator passing a method as arhument or parametr is knowns as decorator
'''
def decorator(func):
    def wrapper():
        print("I ma about to execute a function.....")
        func()
        print("I have executed this function ...")
    return wrapper


def say_hello():
    print("Hello!")

# say_hello()

f=decorator(say_hello)
f();
'''
# same implimnet using @decorator

def decorator(func):
    def wrapper():
        print("I ma about to execute a function.....")
        func()
        print("I have executed this function ...")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()    
