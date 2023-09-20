test_cases = int(input())

for _ in range(test_cases):
    char = input()

    if char.isupper():
        print("Uppercase Character")
    elif char.islower():
        print("Lowercase Character")
    elif char.isdigit():
        print("Numerical Digit")
    else:
        print("Special Character")