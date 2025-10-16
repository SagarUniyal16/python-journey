def token_dispenser(start=1):
    token = start
    try:
        while True:
            new_start = yield token
            if new_start:
                token = new_start
            else:
                token += 1
    except GeneratorExit:
        print("Dispenser closed.")


dispenser = token_dispenser()
print(next(dispenser))      # Output: 1
print(next(dispenser))      # Output: 2
print(dispenser.send(100))  # Output: 100
print(next(dispenser))      # Output: 101
