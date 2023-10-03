t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    for i in range(a):
        for j in range(0, i + 1):
            print(b, end = " ")
        print()
    for i in range(1, a):
        for j in range(i, a):
            print(b, end = " ")
        print()