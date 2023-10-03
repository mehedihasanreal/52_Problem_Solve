t = int(input())
for _ in range(t):
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s.sort()
    for i in range(n):
        print(s[i])