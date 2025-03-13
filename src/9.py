# Function to generate a random number between 1 and 10
def get_random_number():
    import random
    return random.randint(1, 10)

# Function to calculate the sum of two numbers
def add(a, b):
    return a + b

# Function to calculate the difference of two numbers
def subtract(a, b):
    return a - b

# Function to calculate the product of two numbers
def multiply(a, b):
    return a * b

# Function to calculate the quotient of two numbers
def divide(a, b):
    if b == 0:
        print("Cannot divide by zero!")
        return None
    return a / b

# Driver code to test the above functions
if __name__ == "__main__":
    num1 = get_random_number()
    num2 = get_random_number()
    operation = input("Enter an operation (+, -, *, /): ")
    if operation == "+":
        print(f"{num1} {operation} {num2} = {add(num1, num2)}")
    elif operation == "-":
        print(f"{num1} {operation} {num2} = {subtract(num1, num2)}")
    elif operation == "*":
        print(f"{num1} {operation} {num2} = {multiply(num1, num2)}")
    elif operation == "/":
        print(f"{num1} {operation} {num2} = {divide(num1, num2)}")
    else:
        print("Invalid operation!")
