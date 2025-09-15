number = [1,2,3,4,5,6,7,8,9]
evenSum = 0
oddSum = 0
for num in number:
    if num % 2 == 0:
        evenSum += num
    else:
        oddSum += num
print("Even Sum is: ",evenSum)
print("Odd Sum is: ",oddSum)