from functools import wraps

def decoratorss(func):
    @wraps(func)
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decoratorss
def print_name():
    print("My name is Sagar")

print_name()