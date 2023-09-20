t = int(input())
for _ in range(t):
    n = str(input())
    x = len(n)
    sum = 0
    for i in n:
        sum = sum + pow(int(i),x)
    if int(n) == sum:
        print(f"{n} is an armstrong number!")
    else:
        print(f"{n} is not an armstrong number!")