t = int(input())
for _ in range(t):
    s = input()
    v = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in s:
        if i in v:
            count += 1
    print(f"Number of vowels = {count}")