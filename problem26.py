t = int(input())
for _ in range(t):
    x = float(input())
    count = 0
    while(x>0):
        x = x // 2
        count += 1
    print(f"{count} days")