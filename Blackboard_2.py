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

from blackboard import masterChef, doggo
class Chef(masterChef, doggo):
    def make_sandwich(self):
        print("*Sandwich made*")

    def make_adobo(self):
        print("*Adobo made*")

    def make_hotdog(self):
        print("*Hotdog made*")

    


the_chef = Chef()
the_chef.make_specialty()
the_chef.eat_poop()

random_list = ["dog", "cat", "alligator", "crocodile"]
random_list1 = random_list.copy()
random_list1.clear()
print(random_list)