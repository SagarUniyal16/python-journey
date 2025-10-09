# ===============================
# PYTHON CLASSES – COMPLETE BASICS
# ===============================

# 1️⃣ BASIC CLASS DEFINITION
class Person:
    pass  # Empty class for now

# Create an object (instance)
p1 = Person()
print("Created object:", p1)


# 2️⃣ CLASS WITH AN INITIALIZER (__init__)
class Person:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create instances
person1 = Person("Sagar", 25)
person2 = Person("Riya", 23)

person1.greet()
person2.greet()


# 3️⃣ ADDING A CLASS VARIABLE
class Employee:
    company = "TechCorp"  # class variable shared by all instances

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def show_details(self):
        print(f"Name: {self.name}, Role: {self.role}, Company: {Employee.company}")

emp1 = Employee("Sagar", "Data Engineer")
emp2 = Employee("Amit", "Developer")

emp1.show_details()
emp2.show_details()


# 4️⃣ MODIFYING CLASS AND INSTANCE VARIABLES
Employee.company = "DataWorks"
emp1.role = "Senior Data Engineer"

emp1.show_details()
emp2.show_details()


# 5️⃣ ADDING METHODS THAT RETURN VALUES
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

circle1 = Circle(5)
print("Area of circle:", circle1.area())


# 6️⃣ PRIVATE ATTRIBUTES AND METHODS (ENCAPSULATION)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.__balance}")

acc1 = BankAccount("Sagar", 1000)
acc1.deposit(500)
acc1.withdraw(300)
# print(acc1.__balance)  # ❌ will raise AttributeError


# 7️⃣ INHERITANCE
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog = Dog()
cat = Cat()
dog.speak()
cat.speak()


# 8️⃣ SUPER() FUNCTION
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)   # call parent constructor
        self.model = model

    def details(self):
        print(f"Car: {self.brand} {self.model}")

car1 = Car("Toyota", "Innova")
car1.details()


# 9️⃣ CLASS METHODS AND STATIC METHODS
class Student:
    school_name = "ABC School"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @staticmethod
    def welcome_message():
        print("Welcome to the Student Management System")

Student.welcome_message()
Student.change_school("XYZ International School")
student1 = Student("Ravi", 10)
print(student1.school_name)


# 🔟 MAGIC (DUNDER) METHODS
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

book1 = Book("Python Basics", 350)
print(book1)
print("Total pages:", len(book1))


# 1️⃣1️⃣ POLYMORPHISM EXAMPLE
class Bird:
    def fly(self):
        print("Some birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies high")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

for bird in [Sparrow(), Penguin(), Bird()]:
    bird.fly()


# 1️⃣2️⃣ COMPOSITION (HAS-A RELATIONSHIP)
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # composition

    def drive(self):
        self.engine.start()
        print("Car is moving")

car = Car()
car.drive()

# ===============================
# END OF PYTHON CLASS TUTORIAL
# ===============================
