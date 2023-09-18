t = int(input())
for _ in range(t):
    s = input()
    s=s.split(" ")
    s1=""
    for i in s:
        x = i[::-1]
        s1=s1+x
        s1=s1+" "
    print(s1)