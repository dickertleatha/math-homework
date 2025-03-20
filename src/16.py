import random

def get_random_math_problem(difficulty):
    # Generate a random math problem based on the difficulty level
    if difficulty == "easy":
        # Easy math problems
        numbers = [2, 5, 8, 10]
        operators = ["+", "-"]
        answer = random.choice(numbers) + random.choice(operators) + random.choice(numbers)
        return "What is {}?".format(answer)
    elif difficulty == "medium":
        # Medium math problems
        numbers = [2, 5, 8, 10, 15]
        operators = ["+", "-", "*"]
        answer = random.choice(numbers) + random.choice(operators) + random.choice(numbers) + random.choice(operators) + random.choice(numbers)
        return "What is {}?".format(answer)
    else:
        # Hard math problems
        numbers = [2, 5, 8, 10, 15, 20]
        operators = ["+", "-", "*", "/"]
        answer = random.choice(numbers) + random.choice(operators) + random.choice(numbers) + random.choice(operators) + random.choice(numbers) + random.choice(operators) + random.choice(numbers)
        return "What is {}?".format(answer)