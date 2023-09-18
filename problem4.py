t = int(input())
for case in range(1, t + 1):
    n = int(input())
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    print(f'Case {case}: {" ".join(map(str, factors))}')