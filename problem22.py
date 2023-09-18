test_cases = int(input())
for _ in range(test_cases):
    start, end = map(int, input().split())
    count = 0
    for num in range(start, end + 1):
        flag = False
        if num <= 1:
            flag = True
        elif num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = True
                    break
        if not flag:
            count += 1
    print(count)