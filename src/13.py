import random

def get_random_math_problem(n=2):
    """
    Generates a random math problem of the given difficulty level.

    Args:
        n (int, optional): Difficulty level. Defaults to 2.

    Returns:
        str: A string representing the math problem.
    """
    numbers = [random.randint(1, 9) for i in range(n)]
    operators = ["+", "-", "*", "/"]
    operator = random.choice(operators)
    problem = "".join([str(numbers[i]), operator, str(numbers[i + 1])])
    return problem