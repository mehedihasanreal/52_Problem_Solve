t = int(input())
for _ in range(t):
    s = input()
    s = s.lower()
    v = ['a', 'e', 'i', 'o', 'u']
    vowel=''
    cons=''
    for i in s:
        if i.isalpha():
            if i in v:
                vowel+=i
            else:
                cons+=i
    print(vowel)
    print(cons)