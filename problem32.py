t = int(input())
for _ in range(t):
    x, n = map(int,input().split())
    if x > n:
        print("Invalid!")
    else:
        s=''
        for i in range(x, n+1):
            if (i%x == 0):
                print(i)