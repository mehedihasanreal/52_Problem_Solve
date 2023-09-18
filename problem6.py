t = int(input())
for _ in range(1, t+1):
    n = int(input())
    first_digit = n // 10000
    last_digit = n % 10
    sum = first_digit + last_digit
    print(f"Sum = {sum}")