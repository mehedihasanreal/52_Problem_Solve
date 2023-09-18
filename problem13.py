t = int(input())
for _ in range(t):
    s = input()
    w = s.count(" ") + 1
    res = w * (w-1)
    print(f"1/{res}")
