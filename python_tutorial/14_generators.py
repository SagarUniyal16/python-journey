#Basics
def icecream_order():
    print("Please order the ice cream you want to consume")
    order=yield
    while True:
        print(f"Ordered Ice cream is {order}")
        order=yield

order=icecream_order()
next(order)
order.send("Chocolate")
order.send("Strawberry")

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

for cup in stall:
    print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai)) # gives error



#Infinite generators

def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))


#Send generators

def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall) # start the generator

stall.send("Masala Chai")
stall.send("Lemon Chai")


#Close generators
def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")


stall = chai_stall()
print(next(stall))
stall.close() #cleanup






