icecream="chocolate"

def update_flavour():
    icecream="strawberry"
    def normal_test():
        icecream="vanilla"
        print(icecream)
    normal_test()
    print(icecream)


update_flavour()
print(icecream)

print("After non local :->")

icecream1="chocolate"

def update_flavour():
    icecream1="strawberry"
    def nonlocal_test():
        nonlocal icecream1
        icecream1="vanilla"
        print(icecream1)
    nonlocal_test()
    print(icecream1)


update_flavour()
print(icecream1)


print("After Global :->")

icecream2="chocolate"

def update_flavour():
    icecream2="strawberry"
    def global_test():
        global icecream2
        icecream2="vanilla"
        print(icecream2)
    global_test()
    print(icecream2)


update_flavour()
print(icecream2)