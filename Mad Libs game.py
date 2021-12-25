friends = ["Kite", "Hughes", "Shiden"]

print(friends[1:])
print("\"     \"")
print(friends[0:2])
print(friends.index("Shiden"))
print(min(2,3))
print(friends[1])
friends.insert(1, "Kanji")
friends[1] = "kai"
print(friends[1])
lucky_numbers = [2, 4, 8, 16]
print(lucky_numbers[1:])
friends.append("yuhan")

print(friends)
friends.extend(lucky_numbers)
print(friends)
print(friends.count("Hughes"))
del friends[1]
print(f'{friends}')
friends2 = friends.copy()
print(f'{friends2}')
coordinates = ('huge', 'mid', 2)
print(coordinates[1])
def mid_diff(kid, boy, boi):
    print("sit " + boy)

mid_diff("mid diff", "boy", "wew")

is_fruit = False
is_ripe = True
    
if is_fruit and is_ripe:
    print("It is a ripe fruit")
elif is_fruit and not (is_ripe):
    print("It is an unripe fruit")
elif is_ripe and not (is_fruit):
    print("It is a ripe vegetable")
else:
    print("It is not a fruit and it is unriped")


    
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3
print(max_num(1, 2, 3))




from math import *
radius = float(input('Enter a radius: '))
area = pi*radius**2
print(f'Area of a circle with radius {radius} is {area:.2f}')

def my_name():
    nameFunc = input("Naruto ")
    lameFunc = "yeehaw"
    return nameFunc 
def my_age():
    ageFunc = input("Age? ")
    return ageFunc
def my_address():
    addressFunc = input("Address? ")
    return addressFunc


def display_output(name, age, address):
    print(f"My name is Uzumaki {name} and I am {age} years old. I live in {address}")

name = my_name()
age = my_age()
address = my_address()
display_output(name, age, address)




