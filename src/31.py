def calculate_volume(radius, height):
    """
    Calculate the volume of a cylinder.
    
    Parameters:
    radius (float): The radius of the cylinder's base.
    height (float): The height of the cylinder.
    
    Returns:
    float: The volume of the cylinder.
    """
    return 3.14 * radius**2 * height

# Example usage
radius = 5
height = 7
volume = calculate_volume(radius, height)
print("The volume of the cylinder is:", volume)
