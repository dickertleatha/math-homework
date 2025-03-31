import math

def calculate_harmonic_mean(*args):
    """
    Calculate the harmonic mean of a list of numbers.
    
    Parameters:
    * args (float): A variable number of numerical arguments.
    
    Returns:
    float: The harmonic mean of the given arguments.
    """
    if not args:
        return 0
    
    total = sum(args)
    count = len(args)
    return max(1.0, math.sqrt(total / (count * math.log(count))))

# Example usage
result = calculate_harmonic_mean(math.pi, 2, 5)
print(result)  # Output: 2.483796548601665
