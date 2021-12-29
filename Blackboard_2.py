#import random
#def dice_roll(sides):
#    result = random.randint(1, sides)
#    print(result)

#dice_roll(5)
#import keyword
#import random
#import sys
#print(keyword.iskeyword("try"))
#print(random.randrange(8, 10, 2))
#sys.stdout.write("print")
#sys.stdout.write("\nokay")
#valid = True
#import sys
#while valid:
#    try:
#        int(input("Input a number: "))
#        valid = False
#    except ValueError:
#        print("Please input an integer.")
    
#def user_input(prompt):
#    try:
#        return input(prompt)
#    except KeyboardInterrupt:
#        print("Please press CTRL + C again to exit the program.")
#user_input("Please enter something: ")

#def test(number):
#    try:
#        return int(input(number))
#    except ValueError:
#        print("Accepting integers only.")
        
#test("Input something for god's sake: ")
import sys
try:
    1/0
except ZeroDivisionError:
    sys.exit("You divided by zero")
while a1:
    print("Okay", "Nah", sep="^")
    a1 = False
print("Okay")

    
