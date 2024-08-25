'''              
                          CALCULATOR

TASK 2

Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.
'''


def Sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print(f"The sum of {a} and {b} is: {Sum(a, b)}")
elif choice == 2:
    print(f"The difference of {a} and {b} is: {sub(a, b)}")
elif choice == 3:
    print(f"The product of {a} and {b} is: {mul(a, b)}")
elif choice == 4:
    print(f"The result of {a} divided by {b} is: {divide(a, b)}")
else:
    print("Invalid choice!")


 













