def get_random_math_problem():
    """
    Generates a random math problem and returns it as a string.
    """
    operands = ["+", "-", "*", "/"]
    operator = random.choice(operands)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    problem = f"{num1} {operator} {num2}"
    return problem
