t = int(input())
for _ in range(t):
    n = int(input())
    factorial = 1
    if n == 0:
        print('1')
    else:
        for i in range(1, n+1):
            factorial = factorial * i
        print(factorial)

#using recursion

# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         return (x * factorial(x-1))

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     print(factorial(n))

