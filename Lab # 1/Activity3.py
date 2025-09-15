isPrime = True
i = 2
n = int(input("Enter the number again: "))
while i < n:
    remainder = n % i
    if remainder == 0:
        isPrime = False
        break
    else:
        i = i + 1
if isPrime:
    print("The given number is prime")
else:
    print("The given number is not prime")