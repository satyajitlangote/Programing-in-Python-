# Program to calculate factorial of given number. 
#Method 1
"""
def factorial(n):
    return 1 
if(n==1 or n==0)
else 
    factorial(n-1):
num=5;
print("Factorial of",num,"is",factorial(num))

"""

# Method 2: Iterative approach to calculate factorial
def factorial(n):
    result = 1
    for i in range(2, n + 1):  # Multiply from 2 to n
        result *= i
    return result

# Input number
num = 5

# Calculate and print the factorial
print("Factorial of", num, "is", factorial(num))