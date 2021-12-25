try: 
    print(format(10/12,'.2f'))
    int(input("Please input an integer: "))
    a = 10/0
except ZeroDivisionError as errddd:
    print(errddd)
except ValueError:
    print("Please input integers only")



    