# ===============================
# PYTHON FUNCTIONS – COMPLETE BASICS
# ===============================

# 1️⃣ BASIC FUNCTION
def greet():
    print("Hello, welcome to Python!")

# Call the function
greet()


# 2️⃣ FUNCTION WITH PARAMETERS
def greet_person(name):
    print(f"Hello, {name}! Nice to meet you.")

greet_person("Sagar")
greet_person("Alex")


# 3️⃣ FUNCTION WITH MULTIPLE PARAMETERS
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

add_numbers(5, 3)
add_numbers(10, 20)


# 4️⃣ FUNCTION THAT RETURNS A VALUE
def multiply(x, y):
    return x * y

product = multiply(4, 5)
print("Product:", product)


# 5️⃣ DEFAULT PARAMETERS
def greet_default(name="Guest"):
    print(f"Welcome, {name}!")

greet_default()          # Uses default
greet_default("Sagar")   # Overrides default


# 6️⃣ FUNCTION WITH KEYWORD ARGUMENTS
def introduce(name, age, city):
    print(f"My name is {name}, I'm {age} years old, from {city}.")

introduce(age=25, name="Sagar", city="Dehradun")


# 7️⃣ VARIABLE NUMBER OF ARGUMENTS (*args)
def show_numbers(*args):
    print("Numbers:", args)
    print("Total numbers:", len(args))

show_numbers(1, 2, 3, 4, 5)


# 8️⃣ VARIABLE NUMBER OF KEYWORD ARGUMENTS (**kwargs)
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

show_details(name="Sagar", role="Data Engineer", location="India")


# 9️⃣ NESTED FUNCTIONS
def outer_function():
    print("Outer function called")

    def inner_function():
        print("Inner function called")

    inner_function()

outer_function()


# 🔟 LAMBDA (ANONYMOUS FUNCTION)
square = lambda x: x ** 2
print("Square of 6:", square(6))


# 1️⃣1️⃣ FUNCTION AS ARGUMENT
def apply_function(func, value):
    return func(value)

print("Using lambda inside a function:", apply_function(lambda n: n * 3, 10))


# 1️⃣2️⃣ DOCSTRING (FUNCTION DOCUMENTATION)
def divide(a, b):
    """This function divides two numbers and returns the result."""
    return a / b

print(divide.__doc__)
print("Result of division:", divide(10, 2))


# ===============================
# END OF PYTHON FUNCTION TUTORIAL
# ===============================
