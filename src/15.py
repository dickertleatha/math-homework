import random

def get_random_math_problem(difficulty):
    if difficulty == "easy":
        operators = ["+", "-"]
        max_number = 10
    elif difficulty == "medium":
        operators = ["+", "-", "*", "/"]
        max_number = 20
    else:
        operators = ["+", "-", "*", "/", "%"]
        max_number = 30
    
    problem = {}
    problem["left"] = random.randint(1, max_number)
    problem["right"] = random.randint(1, max_number)
    problem["operator"] = random.choice(operators)
    
    return problem