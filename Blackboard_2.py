#import blackboard as bld
#car_list = [
#    "GTR R35", "Maserati", "Ferrari", "Mustang"
#    ]

#cars_prompt = [
#    bld.car("Black", 350, "new"),
#    bld.car("Red", 450, "old"),
#    bld.car("Yellow", 379, "new")
#    ]

#def car_show(cars):
#    for car in cars:
#        print("Car color:", car.color, "<> Car horsepower:", car.horsepower)
#        print(car.brand_new())
  

#print(cars_prompt[0].brand_new())

#car_show(cars_prompt)

# from blackboard import masterChef, doggo
# class Chef(masterChef, doggo):
#     def make_sandwich(self):
#         print("*Sandwich made*")

#     def make_adobo(self):
#         print("*Adobo made*")

#     def make_hotdog(self):
#         print("*Hotdog made*")

#     def __call__(self, age, restaurant):
#         print(age, end = ", ")
#         print(restaurant)



    


# the_chef = Chef()
# the_chef.make_specialty()
# the_chef.eat_poop()
# the_chef = Chef()
# the_chef(18, "Khan Restaurant")
# random_list = ["dog", "cat", "alligator", "crocodile"]
# random_list1 = random_list.copy()
# random_list1.clear()
# print(random_list)


# def name_checking():
#     global count
#     names = ["eren", "armin", "mikasa", "levi"]
#     alive_people = ["armin", "mikasa", "levi"]
#     count = 0
#     for name in names:
#         if name in alive_people:
#             count += 1

# name_checking()
# print(count)

# var1 = [("animal", "okay"),
#        ("sdsa", "dsds"),
#        ("oakai", "dasdsa")]
# for row in var1:
#     for column in row:
#         print(column)

# print(var1[i] for i in range(len(var1)))
# print(list(var1[i] for i in range(len(var1))))

# def my_generator():
#     n = 1
#     print("This is number 1")
#     yield n

#     n += 1
#     print("This is number 2")
#     yield n 

#     n+=1
#     print("This is number 3")
#     yield n

# my_generator()

# my_dict = {"1st Hokage": "Hashirama",
#           "2nd Hokage": "Tobirama",
#           "3rd Hokage": "Hiruzen",
#           "4th Hokage": "Minato",
#           "5th Hokage": "Tsunade",
#           "6th Hokage": "Kakashi",
#           "7th Hokage": "Naruto"}

# print(my_dict.keys())



# x = lambda a : a + 10
# print(x(51))
# the_dict = {"car": "mustang"}

# number = [1,2,3]
# name = ["khan", "shiden", "yelly"]
# for i in name:
#         print(dict.fromkeys(number, i))

# def lambda_test(a):
#         return lambda n:n-a

# test_var = lambda_test(6)

# print(test_var(4))


# another_var = lambda_test(3)

# print(another_var(6))

# def iterator(n):
#         for i in range(n):
#          yield i*2
 
# print(iterator(3))

# Class = "okay"
# print(Class)

# print("Hello, 'Goodbye.'")
# class Solution:
#     def __init__(self):
#         print("initiating protocol")

#     def twoSum(self, list, target):
#         for i in range(len(list)):
#             for j in range(1, len(list)):
#                 if list[i] + list[j] == target:
#                     return[i, j]
# the_solution = Solution().twoSum([4,5,6,4,12], 11)
# print(the_solution)



# madeup_set = {2,2,2,3,5,6,8,(3,4,6),"dsds"}
# madeup_set2 = {123,132,2}
# print(madeup_set.isdisjoint(madeup_set2))


# for i in range(500, 510, 1): a = i; print ("%i: %s" % (i, a is int(str(i))))

# a_string = "derivative of cscx is -csc(x)cot(x)"
# reversed_string = a_string[::-1]
# print(reversed_string)
# numbers = [1,2,3,4,5,6,7]
# numbers = (int(number) for number in numbers)
# for i in list(numbers):
#     print(type(i))

# stringgg = [2,3,5,6]+[4,3,5,53,5]
# print(stringgg)

# my_num = 3.12122
# print("The number is %f" % my_num)
# # head = "\t\t---------    ---------    ---------    ---------    ---------    ---------    ---------    ---------    ---------\n"*5 
# # body =  "\t    ||||         ||||         ||||         ||||         ||||         ||||         ||||         ||||         ||||         ||||\n"*5
 

# # for i in range(100000):
# #     print(head, body, end = "")
    
# print(f"The lucky number is {2.1312314124:.5f}")   


# for i in range(10):
#     if i == 1:
#         print("    *")
#     if i == 2:
#         print(" ")
#     if i == 3:
#         print("   ***")
#     if i == 4:
#         print(" ")
#     if i == 5:
#         print(" *  *  *")
#     if i == 6:
#         print(" ")
#     if i == 7:
#         print("*********")

# def summ(my_nums):
#     total = 0
#     for i in my_nums:
#         total += i
#     return total


# print(summ([2,3,5,6,7]))


# def the_vehicles():
#     class Vehicle:
#         def __init__(self, Model, CC):
#             self.Model = Model
#             self.CC = CC
#         def consumption(self):
#             val_consump = self.CC*(10/1000)
#             return str(val_consump) + " Km/Liter"
#         def speed(self):
#             vehicle_speed = "42 mph"
#             return vehicle_speed
#     return Vehicle


# if __name__ == "__main__": 
#     the_vehicle = the_vehicles()
#     Vehicle = the_vehicle("Maserati", 650)
#     print(Vehicle.consumption())
#     print(f"Model: {Vehicle.Model}\nCC: {Vehicle.CC}")
# word = "Hello World"
# for i in range(1, len(word)+1):
#     print(word[-i])
# from itertools import product
# lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h",
#     "i", "j", "k", "l", "m", "n", "o", "p",
#     "q", "r", "s", "t", "u", 
#     "v", "w", "x", "y", "z"]

# letter_count = len(lower_letters)
# print(letter_count**6)

# def int_convert(x,y):
#     return int(x) + int(y)
# numbers = ("3", "4", "5")
# int_converter = list(map(int_convert, numbers, ["4", "12"]))
# for i in int_converter:
#     print(i)

from itertools import count
import logging 



logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file.log")

#level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.WARNING)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s - %(asctime)s", datefmt = "%m/%d/%Y  %H:%M:%S")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)



logger.warning("This is a warning.")
logger.error("This is an error.")
logger.critical("THIS IS A CRITICAL STATE")

import json

person = {
    "name": "Khan",
    "age": 24,
    "city": "Metropolitan City",
    "titles": ["Champion of the Great War", "The Great Khan", "Conqueror Khan"],
    "married": False
     }

my_json = json.dumps(person)

print(my_json)

my_json = json.loads(my_json)
print(my_json)

with open("khan.json", "w") as file:
    json.dump(person, file)

with open("khan.json", "r") as file:
    my_load = json.load(file)

print(my_load)

import datetime
x = datetime.datetime.now()
print(x.strftime("%I:%M:%S %p  %m/%d/%Y"))
print(x.strftime("%c"))

my_list = [2,3,4]
my_list.reverse()
print(my_list)



my_list = [20, 9994999, -32235, 10000]
def farthest(the_list):
    far = the_list[0]
    the_list.sort()
    second_low = the_list[1]
    lowest = the_list[0]
    second_high = the_list[-2]
    highest = the_list[-1]
    if (second_low - lowest) > (highest - second_high):
        far = lowest
    else:
        far = highest              
    return far
print(farthest(my_list))   

if 3 < 10:
    condition = 5
print(condition)