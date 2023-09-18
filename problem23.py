alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

t = int(input())
for _ in range(t):
    num = ""
    s = input()
    for i in s:
        num += str(alphabet.index(i)+1)
    print(num)