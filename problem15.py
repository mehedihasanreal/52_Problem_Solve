# t = int(input())
# for _ in range(t):
#     s = input()
#     c = set(s)
#     data_dict = []
#     for i in c:
#         val = {}
#         val[i] = s.count(i)
#         data_dict.append(val)
#     for item in data_dict:
#         for key,value in item.items():
#             print(f"{key} = {value}")


t=int(input())
for _ in range(t):
    s=input()
    s=s.replace(" ","")
    s1=set(s)
    s2=list(s1)
    s3=s2.sort()
    for i in s2:
        print(f"{i} = {s.count(i)}")