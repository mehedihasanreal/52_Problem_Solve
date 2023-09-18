# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# def lcm(a, b):
#     return (a * b) // gcd(a, b)
# for _ in range(int(input())):
#     num1, num2 = map(int,input().split())
# result_lcm = lcm(num1, num2)
# print(f"LCM = {result_lcm}")

def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
t = int(input())
for _ in range(t):
    num1, num2 = map(int, input().split())

    print(f"LCM = {compute_lcm(num1, num2)}")