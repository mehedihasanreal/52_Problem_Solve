t = int(input())
for _ in range(t):
    s = input()
    c = input()
    x = s.count(c)
    if x:
        print(f"Occurrence of '{c}' in '{s}' = {x}")
    else:
        print(f"'{c}' is not present")