num1 = float(input("Enter 1st number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter 2nd number: "))




if  operator == "+":
    add = num1 + num2
    print(format(add, '.3f'))
elif operator == "-":
    difference = num1 - num2
    print(format(difference, '.3f'))
elif operator == "/":
    quotient = num1 / num2
    print(format(quotient, '.3f'))
elif operator == "*":
    product = num1*num2
    print(format(product, '.3f'))
else:
    print("Syntax Error")

number = 2.0009
print(format(3, '.2f'))






