print("Enter the objects of list 1 -------")
myList = []
for i in range(5):
    value = int(input("Enter the value for " +  str(i) + " object: "))
    myList.append(value)
myList2 = []
for j in range(5):
    val = int(input("Enter the value for "+ str(j + 5) + " object: "))
    myList2.append(val)
myList3 = myList + myList2
print(myList3)
