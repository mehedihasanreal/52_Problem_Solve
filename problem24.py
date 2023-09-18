t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    new_arr = []
    for currIndex in range(0, n, 2):
        new_arr.append(a[currIndex])

    s = " ".join(map(str, new_arr))
    print(s)
