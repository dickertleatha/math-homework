import random

def get_random_math_problem():
    """
    Generates a random math problem
    Returns: A tuple of (operation, operand1, operand2)
        - operation: A string representing the operation to perform
        - operand1: An integer representing the first operand
        - operand2: An integer representing the second operand
    """
    operations = ['+', '-', '*', '/']
    operand1 = random.randint(1, 10)
    operand2 = random.randint(1, 10)
    operation = random.choice(operations)
    return (operation, operand1, operand2)
