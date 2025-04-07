import numpy as np

def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Parameters:
        radius (float): The radius of the circle.
        
    Returns:
        float: The area of the circle.
    """
    area = 3.14159 * (radius ** 2)
    return area

# Example usage
print("Area:", calculate_area(5))
