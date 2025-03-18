
import random

def get_random_code():
    """Generate a random Python code"""
    # Generate a random integer between 1 and 10
    number = random.randint(1, 10)

    # Generate a random operation (either +, -, *, or /)
    operation = random.choice(['+', '-', '*', '/'])

    # Generate two random numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Use the random number and operation to generate a random equation
    equation = f"{num1} {operation} {num2}"

    # Evaluate the equation using eval()
    result = eval(equation)

    # Return the result
    return result

# Test the function with different inputs
print(get_random_code())