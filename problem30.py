t = int(input())
list = []
for _ in range(t):
    s = input()
    for n in s:
        if n.isdidgit():
            sum = 0
            for i in range(1, n):
                if n%i == 0:
                    sum += i
            if sum == n:
                print(f"YES, {n} is a perfect number!")
            else:
                print(f"NO, {n} is not a perfect number!")