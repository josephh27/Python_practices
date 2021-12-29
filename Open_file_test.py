#Needs to be a raw string if outside the directory since single backslahes are ignored in normal strings.
#githubInstructions = open(r"C:\Users\Core i5 HB\OneDrive\Pictures\Important Files\git add instructions command.txt", encoding="Utf-8")
lockscreen = open(r"C:\Users\Core i5 HB\OneDrive\Pictures\Important Files\cellphone lock screen.txt", "a", encoding="Utf-8")
test1 = open("Python_proper_test_1.py", "r")
print(test1.read())
#lockscreen.write("\nokay")
#for directions in githubInstructions:
#    print(directions, end="")
#githubInstructions.close()
lockscreen.close()
