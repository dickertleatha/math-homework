def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Example usage
if __name__ == "__main__":
    print(add(3, 5))   # Output: 8
    print(subtract(10, -2))  # Output: 12
    print(multiply(4, 6))    # Output: 24
    try:
        print(divide(-5, 2))
    except ValueError as e:
        print(e)  # Output: Cannot divide by zero
