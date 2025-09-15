a = []
b = []
for i in range(5):
    numbers = int(input("Enter the value " + str(i + 1) + ": "))
    a.append(numbers)
for i in range(5):
    number = int(input("Enter the value " + str(i + 5) + ": "))
    b.append(number)
c = a + b
c.sort()
print(c)