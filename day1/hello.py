def find_middle_number(a, b, c):
    # If a is middle
    if (b <= a <= c) or (c <= a <= b):
        return a
    # If b is middle
    elif (a <= b <= c) or (c <= b <= a):
        return b
    # If c is middle
    else:
        return c

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find and display the middle number
middle = find_middle_number(num1, num2, num3)
print(f"The middle number is: {middle}")