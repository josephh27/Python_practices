class Master:
    def __init__(self, name, age, specialty, home, dojo):
        self.name = name
        self.age = age
        self.specialty = specialty
        self.home = home
        self.dojo = dojo
name = 'Nikhil'
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def say_hi(self):
        print("Hello, my name is", self.name)
    def my_age(self):
        print("My age is", self.age)

name1 = input("What is the name of the first master? ")
p1 = Person(name1, 18)

p1.say_hi()
p1.my_age()

def per_son(name, age):
    print(f"Hello, my name is {name}.")
    print(f"My age is {age}.")

per_son("Khan", 18)


