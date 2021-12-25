import array as arr

numbers = arr.array('i', [3, 6, 9, 12])
#print(numbers)
#print(numbers.buffer_info())
#print(numbers[1])
newArray = arr.array(numbers.typecode, (b for b in numbers))

#for i in numbers:
#    print(i)


#print(newArray)

#for i in newArray:
#    print(i)

c = 0 
index = 0
valid = True
while valid:
    print(newArray[index])
    index = index + 1
    c = c + 1
    if c == 4:
        break