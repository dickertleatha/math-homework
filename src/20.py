def calculate_sum(n):
    """
    Calculate the sum of the first n natural numbers.
    
    Parameters:
    n (int): The number of initial natural numbers to add up.
    
    Returns:
    int: The sum of the first n natural numbers.
    """
    return n * (n + 1) // 2

# Example usage
result = calculate_sum(10)
print("The sum of the first 10 natural numbers is:", result)
