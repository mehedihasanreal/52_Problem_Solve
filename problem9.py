t = int(input())
for _ in range(t):
    num = int(input())
    is_perfect_square = (int(num ** 0.5) ** 2 == num)
    if is_perfect_square:
        print("YES")
    else:
        print("NO")