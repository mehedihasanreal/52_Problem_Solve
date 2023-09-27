import math
test_cases = int(input())
for _ in range(test_cases):
    x_center, y_center = map(int, input().split())
    radius = int(input())    
    x_point, y_point = map(int, input().split())
    distance = math.sqrt((x_point - x_center)**2 + (y_point - y_center)**2) 
    if distance <= radius:
        print("The point is inside the circle")
    else:
        print("The point is not inside the circle")
