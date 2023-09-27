t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    for i in range(1, c):
        if i%a == 0 and i%b == 0:
            print(i)