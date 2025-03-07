import random

def get_random_math_problem(max_value=100):
    """
    Generates a random math problem with two numbers and an operator (+, -, *, /).
    :param max_value: the maximum value for the numbers in the problem
    :return: a string representing the problem
    """
    num1 = random.randint(1, max_value)
    num2 = random.randint(1, max_value)
    operator = random.choice(["+", "-", "*", "/"])
    problem = f"{num1} {operator} {num2} = "
    return problem