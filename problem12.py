def find_trailing_zero(n):
    if n < 0:
        return -1
    count = 0
    while (n >= 5):
        n //= 5
        count += n
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    print(find_trailing_zero(n))