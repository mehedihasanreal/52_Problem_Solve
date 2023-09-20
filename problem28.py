t = int(input())
for _ in range(t):
    n = int(input())
    list = []
    for i in range(0, n):
        list.append(int(input()))
    new_list = sorted(list)
    new_list_dsc= sorted(list,reverse=True)
    if list == new_list or list == new_list_dsc:
        print("YES")
    else:
        print("NO")