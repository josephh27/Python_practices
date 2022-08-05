# from email import header


class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)    
        cur = self.head 
        print(cur.next)           
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
       
        
        

    def length(self):
        cur = self.head 
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

my_list = linkedList()
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()
import sys
from numpy import * 
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,23,18],
   ['Sun',13,15,16,22]])

b = [['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,23,18],
   ['Sun',13,15,19,16]]


print(a)
print(sys.getsizeof(a))
print(sys.getsizeof(b))

sum = 0
countdown = 0

while countdown <= 100:
    sum += countdown
    countdown += 1
    
print(sum)
    












# class mode:
#     def __init__(self):
#         self.state = None

# class dog:
#     def __init__(self):
#         self.head = mode()

#     def attitude(self):
#         fur = self.head
#         fur.state = "calm"
#         print(fur.state)
#         fur = self.head
#         print(fur.state)

# dog_1 = dog()
# dog_1.attitude()





# import collections

# dict1 = {'day1': 'Mon', 'day2': 'Tue'}
# dict2 = {'day3': 'Wed', 'day1': 'Thu'}

# res = collections.ChainMap(dict1, dict2)

# # Creating a single dictionary
# print(res.maps,'\n')


# nums = [0,2,3,4,5,65,45,345,54,43,68,32]
# def eval(x):
#     if x % 2 == 0:
#         return x
#     else:
#         return ""
# sub_list = list(map(eval, nums))
# main_list = [i for i in sub_list if i]
# print(main_list)

# tup_1 = [30,10]
# tup_2 = [30,40]

# print(tup_1+tup_2)

# greater = 10 > 7
# str_num = str(73911)
# tup_str = tuple("Thank God It's Friday!")





# def truncate(n):
#     return int(n*1000)/1000

# print(truncate(0.343653))


# class guest:
#     def __init__(self, name, age, address, phone_num):
#         self.age = age 
#         self.name = name
#         self.address = address
#         self.phone_num = phone_num
#     def okay(self):
#         looks = "good"
    
# guest_1 = guest("Khan", 22, "Angono", "09393922931")




# class Customers:
#     greeting = "Welcome to the Coffee Palace!"
#     def __init__(self, name, beverage, food, total):
#         self.name = name
#         self.beverage = beverage 
#         self.food = food
#         self.total = total
    

# customer_1 = Customers("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
# customer_2 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)

# print(Customers.greeting)
# print(customer_1.beverage)
# print(customer_2.food)



# from decimal import Decimal
# x = 3.1237
# print(x)
# x = Decimal(3.1237)
# print(x)
# print(+x)




# x = ["red", "purple", "blue", "violet"]
# y = ["umbrella", "hat", "jacket", "sweater"]
# for i in x:
#     for o in y:
#         print(i, o)









# import sys
# my_list = ["okay", "na"]
# with open("useless_file.txt", "w") as f:
#     f.writelines(f"{i}\n"for i in range(10))

# my_loop = [str(i) for i in range(20, 30, 3)]
# print("\n".join(my_loop))

# from json import JSONEncoder
# import json

# class User:
#     def __init__(self, name, status):
#         self.name = name
#         self.status = status

# my_user = User("Shiden", "21")


# def evaluate(u):
#     if isinstance(u, User):
#         return {"name": u.name, "status": u.status, u.__class__.__name__: True}
#     else:
#         raise TypeError("The class is not user")

# userJSON = json.dumps(my_user, default= evaluate)
# print(userJSON)
    

# class UserEncoder(JSONEncoder):
#     def default(self, u):
#         if isinstance(u, User):
#             return {"name": u.name, "status": u.status, u.__class__.__name__: True}
#         else:
#             return JSONEncoder.default(self, u)


# userJSON = json.dumps(my_user, cls=UserEncoder)
# userJSON = UserEncoder().encode(my_user)
# print(userJSON)


# class Phone:
#     def __init__(self, ram, storage, cores, cam):
#         self.ram = ram
#         self.storage = storage
#         self.cores = cores
#         self.cam = cam

# class SmartPhone(Phone):
#     def __init__(self, ram, storage, cores, cam, internet):
#         super().__init__(ram, storage, cores, cam)
#         self.internet = internet

# Xiaomi = SmartPhone("32 GB", "128 GB", "Quadcore", "Quadcam", "5G")
# print(Xiaomi.internet)

# class Person:
#     age = 25

#     def printAge(self):
#         print('The age is:', self.age)

# # create printAge class method
# Person.printAge = classmethod(Person.printAge)

# Person.printAge()

# import tracemalloc

# def factorial(n):
#     product = 1
#     for i in range(2, n+1):
#         product *= i
#     return product
# tracemalloc.start()

# print(factorial(13))
# print(tracemalloc.get_traced_memory())

# tracemalloc.stop()

# print(int(37.9))



# my_str = "{}"
# for i in range(len(my_str)-1):
#     print(my_str[i] + my_str[i+1])
# if (i != 
#     10):
#     print("okay")
# print(bool([1]))