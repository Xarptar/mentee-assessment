# src/math_utils.py

# TODO: Implement the following functions with basic math operations.
# Each should handle invalid input gracefully.

def add(a, b):
    # TODO: Return the sum of a and b
    #a = input("Enter the first number: ")
    #b = input("Enter the second number: ")
    total = int(a + b)
    
    return (a+b)


def subtract(a, b):
    # TODO: Return the difference between a and b
    #a = input("Enter the first number: ")
    #b = input("Enter the second number: ")
    total = int(a - b)
    
    return (a-b)
    

def multiply(a, b):
    # TODO: Return the product of a and b
    #a = input("Enter the first number: ")
    #b = input("Enter the second number: ")
    total = int(a * b)
    
    return (a*b)
    

def divide(a, b):
    # TODO: Return the quotient of a / b, handle division by zero with ValueError
    #a = input("Enter the first number: ")
    #b = input("Enter the second number: ")
    total = int(a / b)
    return ValueError if b == 0 else (a/b)

