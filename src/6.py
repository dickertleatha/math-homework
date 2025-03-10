
def solve_math_problem(problem):
    """
    Solves a math problem using Python.

    Args:
        problem (str): The math problem to be solved.

    Returns:
        int or float: The solution to the math problem.
    """
    # Split the problem into individual terms
    terms = problem.split(" ")

    # Evaluate each term and store the result in a variable
    result = 0
    for term in terms:
        if term.isdigit():
            result += int(term)
        else:
            result += eval(term)

    return result