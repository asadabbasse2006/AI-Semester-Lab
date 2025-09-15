# n = int(input("Enter number of terms: "))
# a = 0
# b = 1
# print("Fibonacci series:", end=" ")
# for i in range(n):
#     print(a, end=" ")
#     temp = a
#     a = b
#     b = temp + b

n = int(input("Enter a number: "))
x = 0
y = 1
z = 0
while z < n:
    print(z)
    x = y
    y = z
    z = x + y