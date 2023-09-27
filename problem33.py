t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    for i in range(a, b):
        if i%c == 0:
            print(i)
