a = []
b = []
for i in range(5):
    numbers = int(input("Enter the value " + str(i + 1) + ": "))
    a.append(numbers)
for i in range(5):
    number = int(input("Enter the value " + str(i + 6) + ": "))
    b.append(number)
c = a + b
largestNumber = max(c)
smallestNumber = min(c)
print("Largest Number is: ",largestNumber)
print("Smallest Number is: ",smallestNumber)