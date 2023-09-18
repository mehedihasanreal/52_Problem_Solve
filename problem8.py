t = int(input())
for case in range(1, t+1):
    a, b, c = map(int, input().split())
    n = [a,b,c]
    n.sort()
    print(f'Case {case}: {" ".join(map(str, n))}')