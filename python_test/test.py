def info(*args,**kwargs):
    T=()
    D={}
    T=args
    D=kwargs
    return T,D

T,D=info("Human","occupation",Name="Sagar Uniyal",Age=25)

print(T)
print(D)

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



