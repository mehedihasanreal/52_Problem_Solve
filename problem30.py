# t = int(input())
# list = []
# for _ in range(t):
#     s = input()
#     for n in s:
#         if n.isdidgit():
#             sum = 0
#             for i in range(1, n):
#                 if n%i == 0:
#                     sum += i
#             if sum == n:
#                 print(f"YES, {n} is a perfect number!")
#             else:
#                 print(f"NO, {n} is not a perfect number!")

def diagonalDifference(arr):
    left_to_right_diagonal = 0
    right_to_left_diagonal = 0
    n = len(arr)  # Assuming the matrix is square, so the number of rows and columns is the same

    for i in range(n):
        left_to_right_diagonal += arr[i][i]
        print(arr[i][i])
        right_to_left_diagonal += arr[i][n - 1 - i]

    return abs(left_to_right_diagonal - right_to_left_diagonal)

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

result = diagonalDifference(matrix)
print(result)